# Drillbit API Python Library

This module provides a Python interface to interact with the DrillBit Plagiarism Check API. It supports authentication, folder operations, file uploads, submissions, and file downloads.

# Setup

## Prerequisites

- Python 3.6+

- requests library

- python-dotenv library

- DrillBit API credentials (username and password)

- Installation

- Clone the repository or download the drillbit_api.py file.

- Install the required Python packages:


# Setup

Create a .env file in the same directory as drillbit_api.py and add your DrillBit API credentials:
```ini
DRILLBIT_USERNAME=your_username
DRILLBIT_PASSWORD=your_password
```

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

- Copy the drillbit_api.py file into your Frappe application directory, for example: your_app/your_app/api/drillbit_api.py.

- Add DrillBit credentials to your site configuration:

- Open your site's site_config.json file and add your DrillBit API credentials:

Note: this will be later handled within frappe. We would write the username and password in site's config using frappe API.

```json
{
    "db_name": "your_db_name",
    "db_password": "your_db_password",
    "drillbit_username": "your_username",
    "drillbit_password": "your_password"
}
```

## Use the DrillBit API module in your Frappe code:

Import and use the module in your Frappe application. For example, you can create a server script or custom app feature that interacts with the DrillBit API:


```python
from your_app.api.drillbit_api import DrillbitAPI
import frappe

def example_function():
    base_url = "https://s1.drillbitplagiarismcheck.com"
    api = DrillbitAPI(base_url)

    username = frappe.get_site_config().get('drillbit_username')
    password = frappe.get_site_config().get('drillbit_password')

    api.authenticate(username, password)

    if api.is_token_valid():
        folder_name = "Pro folder"
        api.create_folder(folder_name)
        # Add more method calls as needed
    else:
        frappe.throw("Unable to proceed, authentication failed.")
```
