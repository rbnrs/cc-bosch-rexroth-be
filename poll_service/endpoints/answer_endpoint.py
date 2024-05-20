import json
import uuid
from django.http import HttpRequest, HttpResponse, JsonResponse

from poll_service.dao.answer_dao import AnswerDAO
from poll_service.entities.Answer import Answer


class AnswerEndpoint:
    
    def __init__(self):
        pass
    
    def create_answer(self, request):
        answerDAO = AnswerDAO()
        request_json = json.loads(request.body)
        answer = Answer(
            answer_id=str(uuid.uuid4()),
            question_id=request_json['questionId'],
            poll_id=request_json['pollId'],
            answer=request_json['answer'],
            answer_by=request_json['answerBy']
        )
        
        is_created = answerDAO.create_answer(answer)   
        
        if is_created == True:
            return HttpResponse(status=201)  
        else:
            return HttpResponse(status=500)
    
    def check_answer(self, user_id: str, poll_id: str):
        answerDAO = AnswerDAO() 
        has_voted = answerDAO.check_answer(user_id, poll_id)
        
        return JsonResponse(data={
            'hasVoted': has_voted
        })
        
    def get_answers_for_poll(self, poll_id:str):
        answerDAO = AnswerDAO()
        answers_json = []
        answers = answerDAO.answers(poll_id)
        
        for answer in answers:
            answers_json.append(answer.to_json())
            
        return JsonResponse(
            data=answers_json,
            safe=False
        )
    