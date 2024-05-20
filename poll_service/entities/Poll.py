from datetime import datetime

from poll_service.entities.Question import Question


class Poll:     
    
    def __init__(self, id:str, poll_name:str, poll_description: str, timestamp: datetime):
        self.__id = id
        self.__poll_name = poll_name
        self.__poll_description = poll_description
        self.__timestamp = timestamp
        self.__question = []
        
    def add_question(self, question:Question):
        self.__question.append(question)
        
    @property
    def id(self):
        return self.__id

    @property
    def poll_name(self):
        return self.__poll_name
    
    @property
    def poll_description(self):
        return self.__poll_description
    
    @property
    def options(self):
        return self.__options
    
    @property
    def timestamp(self):
        return self.__timestamp
    
    @property
    def questions(self):
        return self.__question
    
    def set(self, field, value):
        
        if field == 'poll_name':
            self.__poll_name
            self.__timestamp = datetime.now()
        
        if field == 'poll_description':
            self.__poll_description
            self.__timestamp = datetime.now()        

    def to_json(self):
        return {
            '_id': str(self.__id),
            'name': self.__poll_name,
            'description': self.__poll_description,
            'timestamp': self.__timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        }
        
    def to_expanded_json(self):
        poll_json = self.to_json()
        questions_json = []
        for question in self.__question:
            questions_json.append(question.to_expanded_json())
            
        poll_json['questions'] = questions_json
    
        return poll_json
            
            

    @staticmethod
    def from_json(map):
        timestamp = datetime.strptime(map['timestamp'], '%Y-%m-%d %H:%M:%S')
        return Poll(
            id=map['_id'],
            poll_name=map['name'],
            poll_description=map['description'],
            timestamp=timestamp,            
        ) 
    