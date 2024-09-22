# Drillbit API Python Library

This module provides a Python interface to interact with the DrillBit Plagiarism Check API. It supports authentication, folder operations, file uploads, submissions, and file downloads.

## Prerequisites

- Python 3.6+

- requests library

- DrillBit API credentials (username and password)


# Connecting to Frappe
To integrate this module into a Frappe application, follow these steps:

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
