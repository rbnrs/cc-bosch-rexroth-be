class Option:
    
    def __init__(self, id:str, question_id:str, poll_id: str, text: str): 
        self.__id = id
        self.__question_id = question_id
        self.__poll_id = poll_id
        self.__text = text
        

    @property
    def id(self):
        return self.__id
    
    @property
    def question_id(self):
        return self.__question_id
    
    @property
    def poll_id(self):
        return self.__poll_id
    
    @property
    def text(self):
        return self.__text
    
    def to_json(self): 
        return {
            '_id': str(self.__id),
            'question_id': str(self.__question_id),
            'poll_id': str(self.__poll_id)   ,
            'text': self.__text
        }
        
    @staticmethod
    def from_json(map):
        return Option(
            id=str(map['_id']),
            question_id=map['question_id'],
            poll_id=map['poll_id'],
            text=map['text'],
        )
    