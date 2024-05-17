from poll_service.entities.Option import Option
from datetime import datetime


class Poll:     
    
    def __init__(self, id:str, poll_name:str, poll_description: str, timestamp: datetime):
        self.__id = id
        self.__poll_name = poll_name
        self.__poll_description = poll_description
        self.__timestamp = timestamp
        self.__options = []
        
    def add_option(self, option:Option):
        self.__options.append(option)
        
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
    
    def set(self, field, value):
        
        if field == 'poll_name':
            self.__poll_name
            self.__timestamp = datetime.now()
        
        if field == 'poll_description':
            self.__poll_description
            self.__timestamp = datetime.now()        

    def to_json(self):
        return {
            'id': self.__id,
            'name': self.__poll_name,
            'description': self.__poll_description,
            'timestamp': self.__timestamp.strftime('%Y-%m-%d %H:%M:%m'),
        }

    @staticmethod
    def to_json(map):
        return Poll(
            id=map['id'],
            poll_name=map['name'],
            poll_description=map['description'],
            timestamp=map['timestamp'],            
        ) 
    