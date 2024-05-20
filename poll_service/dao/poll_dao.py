from poll_service.entities.Option import Option
from poll_service.entities.Poll import Poll
from poll_service.entities.Question import Question
from poll_service.services.database_handler import DatabaseHandler


class PollDAO:
       
    __database_handler: DatabaseHandler
    __collection_name: str = 'polls'
    __collection_name_question: str = 'question'
    __collection_name_option: str = 'options'
    
    def __init__(self):
        self.__database_handler = DatabaseHandler()
        
    
    def create(self, poll_object: Poll) -> bool :
        try: 
                        
            self.__database_handler.insert(poll_object.to_json(), self.__collection_name) #insert header entry
            
            for question in poll_object.questions:
                self.__database_handler.insert(question.to_json(), self.__collection_name_question) # insert question entry
                
                for option in question.options:
                    self.__database_handler.insert(option.to_json(), self.__collection_name_option) # insert option entry
                
            return True
        except Exception as e:
            return False
        
    
    def get_options(self, poll_id, question_id) -> list:
        options = []
        get_result = self.__database_handler.get_multiple(self.__collection_name_option, {'question_id': question_id, 'poll_id': poll_id})
        
        for option_result in list(get_result):
            option = Option.from_json(option_result)
            options.append(option)
        
        return options
    

    def get_questions(self, poll_id) -> list:
        questions = []
        get_result = self.__database_handler.get_multiple(self.__collection_name_question, {'poll_id': poll_id})

        for question_result in list(get_result):
            question = Question.from_json(question_result)
            options = self.get_options(poll_id, question.id)
            
            for option in options:
                question.add_option(option)
            
            questions.append(question)
                
        return questions
            
    
    
    def get_polls(self) -> list:
        
        polls = []
        
        get_result = self.__database_handler.get_multiple(self.__collection_name, {})
        
        for poll_result in list(get_result):
            #poll_result
            poll = Poll.from_json(poll_result)
            questions = self.get_questions(poll.id)
            for question in questions:
                poll.add_question(question)
            
            polls.append(poll)
        
        return polls
            
    
    def get_poll(self, poll_id: str) -> Poll:
        try:
            get_result = self.__database_handler.get(self.__collection_name, {'_id' : poll_id})
            
            if get_result is not None:
                poll = Poll.from_json(get_result)
                questions = self.get_questions(poll.id)
                for question in questions:
                    poll.add_question(question)
                
                return poll
            
            return None        
        except:
            return None
    
    def update_poll(self, poll_id: str, poll_object: any) -> bool: 
        try:
            self.__database_handler.update(self.__collection_name_option, {'id': poll_id}, poll_object)
            return True
        except:
            return False
        
    def get_option(self, option_id: str) -> Option:
        try:
            get_result = self.__database_handler.get(self.__collection_name_option, {'id' : option_id})
            
            if get_result is not None: 
                return Option.from_json(get_result)
                
            return get_result
        except:
            return None
        
    
    def update_option(self, option_id:str, option_object: any) -> bool: 
        try:
            self.__database_handler.update(self.__collection_name_option, {'id': option_id}, option_object)
            return True
        except:
            return False
        
