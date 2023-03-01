import os
from eLabFTW_api_config import Experiment

## Create a new extry in Experiments with optional file upload

title = "Test_Title"
date = "20230216"
body = "Test body"
local_folder_path = r"C:\path\to\folder"
#Initalize class as "exp"
exp = Experiment()
#Create new entry in Experiments
exp.create_experiment(title,date,body)
#Upload several file to this new entry
for filename in os.listdir(local_folder_path):
    local_file_path = os.path.join(local_folder_path, filename)
    if os.path.isfile(local_file_path):
        exp.upload_file(local_file_path)