class Option:
    
    def __init__(self, id:str, poll_id: str, option_type: str, language: str, option_descr: str, votes: list): 
        self.__id = id
        self.__poll_id = poll_id
        self.__option_type = option_type
        self.__language = language
        self.__option_descr = option_descr
        self.__votes = votes
        

    @property
    def id(self):
        return self.__id
    
    @property
    def poll_id(self):
        return self.__poll_id
    
    @property
    def option_type(self):
        return self.__option_type
    
    @property
    def language(self):
        return self.__language
    
    @property
    def option_descr(self):
        return self.__option_descr
    
    @property
    def votes(self):
        return self.__votes
    
    def to_json(self): 
        return {
            'id': self.__id,
            'poll_id': self.__id,
            'type': self.__option_type,
            'language': self.__language,
            'description': self.__option_descr,
            'votes': self.__vote_count
        }
        
    @staticmethod
    def from_json(map):
        return Option(
            id=map['id'],
            poll_id=map['poll_id'],
            option_type=map['type'],
            language=map['language'],
            option_descr=map['description'],
            votes=map['votes']
        )
    