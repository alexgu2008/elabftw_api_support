import os
import elabapy
import json
from requests.exceptions import HTTPError
manager = elabapy.Manager(endpoint="https://elabftw.tugraz.at/api/v1/",token="API_KEY")

local_folder_path = r"C:\Path\to\folder"
id_experiment = 100

## Upload several files to an existing experiment entry. "100" is the ID of the experiment. Change to the desired one.

for filename in os.listdir(local_folder_path):
    local_file_path = os.path.join(local_folder_path, filename)
    if os.path.isfile(local_file_path):
        with open(local_file_path, 'r+b') as myfile:
            params = { 'file': myfile }
            print(manager.upload_to_experiment(id_experiment, params))