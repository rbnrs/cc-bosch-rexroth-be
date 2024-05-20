from poll_service.entities.Option import Option


class Question:
    
    def __init__(self, id:str, poll_id:str, text:str, language:str, question_type:str, options: list):
        self.__id = id
        self.__poll_id = poll_id
        self.__text = text
        self.__language = language
        self.__question_type = question_type
        self.__options = options
    
    @property
    def id(self):
        return self.__id
    
    @property
    def poll_id(self):
        return self.__poll_id

    @property
    def text(self):
        return self.__text

    @property
    def lanugage(self):
        return self.__language
    
    @property
    def question_type(self):
        return self.__question_type
    
    @property
    def options(self):
        return self.__options
    
    def add_option(self, option: Option):
        self.__options.append(option)
    
    def to_json(self):
        return {
            "_id": str(self.__id),
            "poll_id": str(self.__poll_id),
            "text": self.__text,
            "language": self.__language,
            "question_type": self.__question_type,
        }
        
    def to_expanded_json(self):
        question_json = self.to_json()
        options_json = []
        for option in self.__options:
            options_json.append(option.to_json())
            
        question_json['options'] = options_json
        
        return question_json
        
    @staticmethod
    def from_json(map):
        return Question(
            id=str(map['_id']),
            poll_id=map['poll_id'],
            text=map['text'],
            language=map['language'],
            question_type=map['question_type'],
            options=[]
        )