import elabapy
import json
from requests.exceptions import HTTPError

class Experiment:
    
    # Initialize the manager with an endpoint and your token
    def __init__(self):
        self.__manager = elabapy.Manager(endpoint="https://elabftw.tugraz.at/api/v1/",token="API_KEY")
  
    # Create a new experiment
    def create_experiment(self, title, date, body):
        self.__experiment = self.__manager.create_experiment()
        params = { "title": title,  "date": date, "body": body}
        print(f"Created experiment with id {self.__experiment['id']}.")
        print(self.__manager.post_experiment(self.__experiment['id'], params))
        
    # Upload a file to an experiment
    def upload_file(self,file):
        with open(file, 'r+b') as myfile:
            params = { 'file': myfile }
            print(self.__manager.upload_to_experiment(self.__experiment['id'], params))
            
class Database:
    
    # Initialize the manager with an endpoint and your token
    def __init__(self):
        self.__manager = elabapy.Manager(endpoint="https://elabftw.tugraz.at/api/v1/",token="API_KEY")
   
    # Create a new database item
    def create_database_item(self, title, date, body):     
        self.__item = self.__manager.create_item(1)
        params = { "title": title,  "date": date, "body": body}
        print(f"Created database item with id {self.__item['id']}.")
        print(self.__manager.post_item(self.__item['id'], params))
