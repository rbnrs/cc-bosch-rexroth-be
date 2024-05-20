class Answer:
    
    def __init__(self, answer_id:str, question_id:str, poll_id:str, answer_by:str, answer:str):
        self.__answer_id = answer_id
        self.__question_id = question_id
        self.__poll_id = poll_id
        self.__answer = answer
        self.__answer_by = answer_by
        
    @property
    def answer_id(self):
        return self.__answer_id
    
    @property
    def question_id(self):
        return self.__question_id
    
    @property
    def poll_id(self):
        return self.__poll_id
    
    @property
    def answer(self):
        return self.__answer
    
    @property
    def answer_by(self):
        return self.__answer_by

    
    def to_json(self):
        return {
            '_id': self.__answer_id,
            'question_id': self.__question_id,
            'poll_id': self.__poll_id,
            'answer': self.__answer,
            'answer_by': self.__answer_by
        }
    
    @staticmethod
    def from_json(map):
        return Answer(
            answer_id=map['_id'],
            question_id=map['question_id'],
            poll_id=map['poll_id'],
            answer=map['answer'],
            answer_by=map['answer_by']
        )
        