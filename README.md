# Drillbit API Python Library

This module provides a Python interface to interact with the DrillBit Plagiarism Check API. It supports authentication, folder operations, file uploads, submissions, and file downloads.

# Setup

## Prerequisites

- Python 3.6+

- requests library

- DrillBit API credentials (username and password)


# Setup


# Usage
```python
from drillbit_api import DrillbitAPI
import os

def main():
    base_url = "https://s1.drillbitplagiarismcheck.com"
    api = DrillbitAPI(base_url)

    username = os.getenv("DRILLBIT_USERNAME")
    password = os.getenv("DRILLBIT_PASSWORD")

    api.authenticate(username, password)

    if api.is_token_valid():
        folder_name = "Pro folder"
        api.create_folder(folder_name)
        # Add more method calls as needed for testing
    else:
        print("Unable to proceed, authentication failed.")

if __name__ == "__main__":
    main()
```


# Connecting to Frappe
To integrate this module into a Frappe application, follow these steps:

- Place drillbit_api.py in your Frappe app:

- Copy the drillbit_api.py file into your Frappe sites directory, for example: "/home/frappeuser/frappe-bench/sites/assets/drillbit/drillbit_api.py"

- Add DrillBit credentials to your site configuration.

- Open your site's site_config.json file and add your DrillBit API credentials:

## Use the DrillBit API module in your Frappe code:

Import and use the module in your Frappe application. For example, you can create a server script or custom app feature that interacts with the DrillBit API:


```python
import os
import frappe
from frappe.model.document import Document
from assets.drillbit.drillbit_api import DrillbitAPI


def get_absolute_path(file_name):
	if(file_name.startswith('/files/')):
		file_path = f'{frappe.utils.get_bench_path()}/sites/{frappe.utils.get_site_base_path()[2:]}/public{file_name}'
	if(file_name.startswith('/private/')):
		file_path = f'{frappe.utils.get_bench_path()}/sites/{frappe.utils.get_site_base_path()[2:]}{file_name}'
	return file_path

class Assignment(Document):
    def on_submit(self):
        #Authenticate with Drillbit API
        base_url = "https://s1.drillbitplagiarismcheck.com"
        api = DrillbitAPI(base_url)
        api.authenticate(username, password, frappe)
        api.create_folder("New Folder") # example of how to create a new folder using the drillbit API.

        frappe.msgprint(f"This is the Uploaded file: {get_absolute_path(uploaded_file)}")
        frappe.msgprint(f"Username: {username}, Password: {password}")

```
