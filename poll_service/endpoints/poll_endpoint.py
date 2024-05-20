from django.http import HttpRequest, HttpResponse, JsonResponse
import json
import uuid
from datetime import datetime

from poll_service.dao.poll_dao import PollDAO
from poll_service.entities.Option import Option
from poll_service.entities.Poll import Poll
from poll_service.entities.Question import Question


class PollEndpoint:
    
    def __init__(self):
        pass
    
    def get_polls(self, request: HttpRequest):
        poll_dao = PollDAO()    
        poll_json = []
    
        poll_list = poll_dao.get_polls()
        
        for poll in poll_list:
            poll_json.append(poll.to_expanded_json())
        
        return JsonResponse(poll_json, safe=False)
    
    def get_poll(self, request: HttpRequest, poll_id:str):
        poll_dao = PollDAO()
        
        poll = poll_dao.get_poll(poll_id)
        
        return JsonResponse(poll.to_expanded_json(), safe=False)
    
    
    def create_poll(self, request: HttpRequest):
        poll_dao = PollDAO()
        request_body = json.loads(request.body)
        
        poll_id = str(uuid.uuid4())
        
        poll = Poll(
            id=poll_id,
            poll_name=request_body['name'],
            poll_description=request_body['description'],
            timestamp= datetime.now()
        )
        
        if 'questions' in request_body:
            for request_question in request_body['questions']:
                
                options = []
                
                question_id = uuid.uuid4()
                
                if 'options' in request_question:
                    for option_request in request_question['options']:
                        option = Option(
                            id = uuid.uuid4(),
                            question_id=question_id,
                            poll_id=poll_id,
                            text=option_request['text']
                        )
                        
                        options.append(option)
                    
                question = Question(
                            id=question_id,
                            poll_id=poll_id,
                            text=request_question['text'],
                            language=request_question['language'],
                            question_type=request_question['type'],
                            options=options)
                
                poll.add_question(question)
                
        is_created = poll_dao.create(poll)
        
        if is_created == True:
            return HttpResponse(status=201)
        
        return HttpResponse(status=500)
                
    
    #TODO edit
    def update_poll(self, request: HttpRequest, poll_id: str):
        
        poll_dao = PollDAO()
        request_body = json.loads(request.body)
        
        poll = poll_dao.get_poll(poll_id)
        
        if poll is None: 
            return HttpResponse(status=500, content="Poll not found")
        
        if 'changed_fields' in request_body:
            change_fields = request['changed_fields']
            
            for field in change_fields:
                poll.set(field, request_body[field])
        
            poll_dao.update_poll(poll.to_json())
        
        if 'changed_polls' in request_body:
            change_polls = request['changed_polls']
            
            for poll_option in change_polls:
                if 'id' in poll_option:
                    if 'changed_fields' in poll_option:
                        option = poll_dao.get_option(poll_option['id'])
                        changed_fields = poll_option['changed_fields']

                        for field in changed_fields:
                            option.set(field, poll_option[field])
                        
                        poll_dao.update_option(option.to_json())
                    
                    
                    