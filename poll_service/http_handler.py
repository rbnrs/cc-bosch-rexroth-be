from django.http import HttpRequest, HttpResponse

from poll_service.endpoints.answer_endpoint import AnswerEndpoint
from poll_service.endpoints.poll_endpoint import PollEndpoint
from poll_service.services.database_handler import DatabaseHandler

def answer(request: HttpRequest):
    
    # answer_endpoint = AnswerEndpoint()

    # if request.method == 'POST':
    #     return answer_endpoint.create_answer(request)        
    
    # return HttpResponse(status=501)
    
    DatabaseHandler()


def poll(request: HttpRequest, poll_id: str):
    
    poll_endpoint = PollEndpoint()
    
    if request.method == 'GET':
        return poll_endpoint.get_poll(request) 
    
    if request.method == 'POST':
        if poll_id != '' and poll_id is not None:
            return poll_endpoint.update_poll(request, poll_id)
        else:
            return poll_endpoint.create_poll(request)
    if request.method == 'DELETE':
       return poll_endpoint.delete_poll(request)
        
    return HttpResponse(status=501)