eLabFTW is an electronic solution to the classic lab notebook and offers many additional practical features (schedular, collaborative working, lab equipment management, etc.). It is an open source solution that is already in use at many research institutions worldwide.

The page is intended to provide support for the use of eLabFTWs API feature. You will find a guide to prepare your system and simple scripts that you can integrate into your code. If you have a question or request about eLabFTW (e.g. create a team or add a user) please contact the SysAdmin.

# REST API Version 2

## Setup
Since it is an HTTP REST API, the tool used only needs to understand HTTP. In this setup we use python as the tool. For this purpose, a library has already been set up with the name elabapy, which we simply install with pip. To do this, we work in the shell and use, for example: the Anaconda Prompt Shell and enter the following in the console:<br>

```

# create a virtual environment
python -m venv elab
# activate it
# on Linux
source elab/bin/activate
# on Windows
# C:\> elab\Scripts\activate.bat     
# install the library
pip install elabapi-python

```

In the next step we need our personal API key:
1. We can create a new API Key in the User Panel of the eLABFTW instance under "API KEYS". There we name the new key and choose whether it should have viewing rights only or viewing and writing rights. <b>Please note: The key itself is only displayed once. Please save it separately in a safe place.</b>

Now we need the python files with the corresponding instructions to trigger certain actions in eLabFTW locally.

## Python Files

In order to be able to use various functions of the API interface, we create a configuration file which we use as the basis for all other files. Here you only need to replace the value 'API_KEY' at the position " API_KEY = 'API_KEY' " with the generated KEY in the User Panel and save the file. It is important for all other files that all scripts are in the same folder.

```

import os
import time
import datetime
import elabapi_python
from elabapi_python.rest import ApiException

#########################
#         CONFIG        #
#########################
API_HOST_URL = 'https://elabftw.tugraz.at/api/v2'
# replace with your api key
API_KEY = 'API_KEY'
#########################
#      END CONFIG       #
#########################
class Helper_elabftw:
    def __init__(self):
        # Configure the api client
        self.configuration = elabapi_python.Configuration()
        self.configuration.api_key['api_key'] = API_KEY
        self.configuration.api_key_prefix['api_key'] = 'Authorization'
        self.configuration.host = API_HOST_URL
        self.configuration.debug = False
        self.configuration.verify_ssl = True
        #create an instance of the API class
        self.api_client = elabapi_python.ApiClient(self.configuration)
        # fix issue with Authorization header not being properly set by the generated lib
        self.api_client.set_default_header(header_name='Authorization', header_value=API_KEY)

```

We will deal with two cases here. In the first case, we have already created an experiment in eLabFTW and we now want to attach different files to this entry. If you want to upload the content of an entire folder, this is also included in the example. The following short script ([existing_entry.py](https://github.com/alexgu2008/elabftw_api_support/blob/main/existing_entry.py)) is sufficient for this:

```

import os
import elabapi_python
from eLabFTW_config_api2 import Helper_elabftw

helper = Helper_elabftw()
api_client = helper.api_client

# create an instance of Experiments and another for Uploads
experimentsApi = elabapi_python.ExperimentsApi(api_client)
uploadsApi = elabapi_python.UploadsApi(api_client)

# upload a file in a specific directory to a existing experiment entry (e.g. with ID 399)
local_file_path = r"C:\path\to\file"
uploadsApi.post_upload('experiments', 399, file=local_file_path, comment='Uploaded with APIv2')

# upload the content of a folder in a specific directory
local_folder_path = r"C:\path\to\folder"
for filename in os.listdir(local_folder_path):
    local_file_path = os.path.join(local_folder_path, filename)
    if os.path.isfile(local_file_path):
        uploadsApi.post_upload('experiments', 399, file=local_file_path, comment='Uploaded with APIv2')

```

In the second case, we want to create a new experiment with the possibility to attach files directly to this experiment. If you want to upload the content of an entire folder, this is also included in the example.

```

import os
import elabapi_python
from eLabFTW_config_api2 import Helper_elabftw

helper = Helper_elabftw()
api_client = helper.api_client

# create an instance of Experiments and another for Uploads
experimentsApi = elabapi_python.ExperimentsApi(api_client)
uploadsApi = elabapi_python.UploadsApi(api_client)

# create a blank new experiment
# exp = experimentsApi.post_experiment()

# create a new experiment and get back additional information (e.g. ID)
response_body, status_code, response_headers = experimentsApi.post_experiment_with_http_info()

# Search for "Location" anf returns a URL, splits in several parts and looks for the last element, which is ID
id = response_headers["Location"].split("/")[-1]

# upload a file in a specific directory
local_file_path = r"C:\path\to\file"
uploadsApi.post_upload('experiments', id, file=local_file_path, comment='Uploaded with APIv2')

# upload the content of a folder in a specific directory
local_folder_path = r"C:\path\to\folder"
for filename in os.listdir(local_folder_path):
    local_file_path = os.path.join(local_folder_path, filename)
    if os.path.isfile(local_file_path):
        uploadsApi.post_upload('experiments', id, file=local_file_path, comment='Uploaded with APIv2')

```

## Additional functions

You can find further usage options in the [official documentation](https://doc.elabftw.net/api/) of the eLabFTW API features.

## Contact
*Ticket*<br>
<elabftw-support@tugraz.at>

*SysAdmin:* *Alexander* *Bardel*<br>
<alexander.bardel@tugraz.at>

