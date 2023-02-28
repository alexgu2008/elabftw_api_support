from eLabFTW_api_config import Experiment

## Create a new extry in Experiments with optional file upload

title = "Test_Title"
date = "20230216"
body = "Test body"
file_1 = "your_file.png"
#Initalize class as "exp"
exp = Experiment()
#Create new entry in Experiments
exp.create_experiment(title,date,body)
#Upload a file to this new entry
exp.upload_file(file_1)


from eLabFTW_api_config import Database

## Create a new item in Database

title = "Test_Title"
date = "20230216"
body = "Test body"
#Initalize class as "item"
item = Database()
#Create new item in Database
item.create_database_item(title,date,body)
