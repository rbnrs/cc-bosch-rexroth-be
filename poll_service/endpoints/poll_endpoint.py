from django.http import HttpRequest, HttpResponse
import json

from poll_service.dao.poll_dao import PollDAO


class PollEndpoint:
    
    def __init__(self):
        pass
    
    def update_poll(self, request: HttpRequest, poll_id: str):
        
        poll_dao = PollDAO()
        request_body = json.dumps(request.body)
        
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
                    
                    
                    