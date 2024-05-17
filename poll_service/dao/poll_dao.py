from poll_service.entities.Option import Option
from poll_service.entities.Poll import Poll
from poll_service.services.database_handler import DatabaseHandler


class PollDAO:
       
    __database_handler: DatabaseHandler
    __collection_name: str = 'polls'
    __collection_name_option: str = 'options'
    
    def __init__(self):
        self.__databaseHandler = DatabaseHandler()
        
    
    def create(self, poll_object: any) -> Poll :
        try: 
            self.__databaseHandler.insert(poll_object, self.__collection_name)
            # get created item self.__databaseHandler.get()
            #return Poll.from_json(# add here last created object)
            return True
        except:
            return None
        
    def create_poll_options(self, option_object: any) -> bool : 
        #TODO create coding
        pass
    
    def get_poll(self, poll_id: str) -> Poll:
        try:
            get_result = self.__database_handler.get(self.__collection_name, {'id' : poll_id})
            
            if get_result is not None:
                return Poll.from_json(get_result)
                
            return get_result
        
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
        
