from poll_service.dao.poll_dao import PollDAO
from poll_service.entities.Poll import Poll
from datetime import datetime
import uuid

class poll_service:
    
    def __init__(self):
        pass
    
    def create_poll(poll: Poll) -> bool:
        
        try:
            poll_dao = PollDAO()
            poll.id = uuid.uuid1()
            poll.timestamp = datetime.now()
            poll_json = poll.to_json()
            
            poll:Poll = poll_dao.create_poll(poll_json)
            
            if poll is not None:  
        
                for option in poll.options:
                    option.poll_id = Poll.id #set poll id from creation
                    option_json = option.to_json()
                    poll_dao.create_poll_option(option_json)                      
    
                return True       
                 
            else:
                return False
        
        except:
            return False
        
        