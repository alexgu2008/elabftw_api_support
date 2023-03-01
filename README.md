eLabFTW is an electronic solution to the classic lab notebook and offers many additional practical features (schedular, collaborative working, lab equipment management, etc.). It is an open source solution that is already in use at many research institutions worldwide.

The page is intended to provide support for the use of eLabFTWs API feature. You will find a guide to prepare your system and simple scripts that you can integrate into your code.. If you have a question or request about eLabFTW (e.g. create a team or add a user) please contact the SysAdmin.

# REST API Version 1

## Setup
Since it is an HTTP REST API, the tool used only needs to understand HTTP. In this setup we use python as the tool. For this purpose, a library has already been set up with the name elabapy, which we simply install with pip. To do this, we work in the shell and use, for example: the Anaconda Prompt Shell and enter the following in the console:<br>

```

pip install --user -U elabapy

```

In the next step we need the address of our interface and our personal API key:
1. https://elabftw.tugraz.at/api/v1/
2. We can create a new API Key in the User Panel of the eLABFTW instance under "API KEYS". There we name the new key and choose whether it should have viewing rights only or viewing and writing rights. <b>Please note: The key itself is only displayed once. Please save it separately in a safe place.</b>

Now we need the python files with the corresponding instructions to trigger certain actions in eLabFTW locally.

## Python Files

We will deal with two cases here. In the first case, we have already created an experiment in eLabFTW and we now want to attach different files to this entry. The following short script ([existing_entry.py](https://github.com/alexgu2008/elabftw_api_support/blob/main/existing_entry.py)) is sufficient for this:

```

import elabapy
import json
from requests.exceptions import HTTPError
manager = elabapy.Manager(endpoint="https://elabftw.tugraz.at/api/v1/",token="API_KEY")

## Upload a file to an existing experiment entry. "100" is the ID of the experiment. Change to the desired one.
id_experiment = 100
with open("your-file.jpg", 'r+b') as myfile:
    params = { 'file': myfile }
    print(manager.upload_to_experiment(id_experiment, params))

```

In the second case, we want to create a new experiment with the possibility to attach directly to this experiment and/or to create a new database element. To do this, we first create a configuration file ([eLabFTW_api_config.py](https://github.com/alexgu2008/elabftw_api_support/blob/main/eLabFTW_api_config.py)) that can trigger the desired commands in eLabFTW ...

```

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

```
... and a second file ([new_entry.py](https://github.com/alexgu2008/elabftw_api_support/blob/main/new_entry.py)) in which we transfer the content of the new experiment:

```

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

```
<b>Please note that in the second case all files, i.e. the scipts and the files to be uploaded, must be in the same folder.</b>

## Modify and execute files

In both cases, we still need to pass the scripts the address and our API-KEY that we had previously created in the eLabFTW User Panel. With this we initialise the elabapy manager which does the jobs for us. Search for "elabapy.manager" in both the [existing_entry.py](https://github.com/alexgu2008/elabftw_api_support/blob/main/existing_entry.py) and [eLabFTW_api_config.py](https://github.com/alexgu2008/elabftw_api_support/blob/main/eLabFTW_api_config.py) files and replace the term with your generated key in the "API_KEY" field.

Our files are now ready for use and we have to specify which content we want to create and/or which files we desire to upload. Again we will split this part in the two avaiable cases:

1. Existing Experiment: In this case we just have to change "id_experiment" to the ID of our already existing experiment. You will find the ID number of your desired experiment as the last value in the URL when you check the experiment entry in the webbrowser. After that you just change "your-file.jpg" to the file you want to upload. For several files repeat this step or use a for-loop.

2. New Experiment/Database Item: To create a new experiment or database item we have to specify the content for "title", "date" and "body" in the file [new_entry.py](https://github.com/alexgu2008/elabftw_api_support/blob/main/new_entry.py). This is the same procedure for an experiment entry and database item. In the case of an experiment you can also directly defina a file that is also uploaded to the new experiment.

### Upload several files at once

If you want to upload the contents of an entire folder, you can alternatively use the following functions. Again, this is the case of the already existing experiment and the new one to be created.

[existing_entry_serveral_files.py](https://github.com/alexgu2008/elabftw_api_support/blob/main/existing_entry_serveral_files.py)
```

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
            
```

[new_entry_several_files.py](https://github.com/alexgu2008/elabftw_api_support/blob/main/new_entry_several_files.py)
```

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
        
```

## Additional functions

You can find further usage options in the [official documentation](https://doc.elabftw.net/api/) of the eLabFTW API features. In the meantime, a new version of the API interface has been released, more about this in the future.

# REST API Version 2

<b>Guide is in progress!</b>

## Contact
*RDM* *Team*<br>
<rdmteam@tugraz.at>

*SysAdmin:* *Alexander* *Gruber*<br>
<alexander.gruber@tugraz.at>

