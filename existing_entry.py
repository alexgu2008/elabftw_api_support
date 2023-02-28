import elabapy
import json
from requests.exceptions import HTTPError
manager = elabapy.Manager(endpoint="https://elabftw.tugraz.at/api/v1/",token="API_KEY")

## Upload a file to an existing experiment entry. "100" is the ID of the experiment. Change to the desired one.
id_experiment = 100
with open("your-file.jpg", 'r+b') as myfile:
    params = { 'file': myfile }
    print(manager.upload_to_experiment(id_experiment, params))
