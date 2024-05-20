from poll_service.entities.Answer import Answer
from poll_service.services.database_handler import DatabaseHandler


class AnswerDAO: 
    
    __database_handler: DatabaseHandler
    __collection_name: str = 'answer'  
    
    def __init__(self):
        self.__database_handler = DatabaseHandler()
    
    def check_answer(self, user_id: str, poll_id):
        try:
            check_result = self.__database_handler.get(self.__collection_name, {
                'answer_by': user_id,
                'poll_id': poll_id,
            })
            
            if check_result is not None:
                return True
            else: 
                return False
            
        except Exception as e:
            return False
        
    def create_answer(self, answer:Answer):
        try:          
            create_result = self.__database_handler.insert(answer.to_json(), self.__collection_name)
            if create_result is not None:
                return True
            else: 
                return False
            
        except Exception as e:
           return False
       
    def answers(self, poll_id: str):
        answers = []
        get_result = self.__database_handler.get_multiple(self.__collection_name, {
            'poll_id': poll_id,
        })
        
        if get_result is not None:
            for answer_result in list(get_result):
                answer = Answer.from_json(answer_result)
                answers.append(answer)
                
        return answers
    