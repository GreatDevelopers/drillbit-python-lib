# DrillbitAPI Class

This class represents the DrillbitAPI, which provides methods for interacting with the Drillbit Plagiarism Check API.

## Args:
- `base_url` (str): The base URL of the Drillbit Plagiarism Check API.

## Attributes:
- `base_url` (str): The base URL of the Drillbit Plagiarism Check API.
- `jwt_token` (str): The JWT token used for authentication.
- `jwt_expiry` (int): The expiration time of the JWT token.

## Methods:

### authenticate(username, password, frappe)
Authenticates the user with the Drillbit Plagiarism Check API.

#### Args:
- `username` (str): The username of the user.
- `password` (str): The password of the user.
- `frappe`: The frappe object.

### is_token_valid()
Checks if the JWT token is valid.

### create_folder(folder_name)
Creates a new folder in the Drillbit Plagiarism Check API.

#### Args:
- `folder_name` (str): The name of the folder to create.

### get_headers()
Returns the headers required for API requests.

### upload_file(author_name, title, document_type, guide_email, guide_name, plagiarism_check, grammar_check, language, file_path)
Uploads a file to the Drillbit Plagiarism Check API.

#### Args:
- `author_name` (str): The name of the author.
- `title` (str): The title of the document.
- `document_type` (str): The type of the document.
- `guide_email` (str): The email of the guide.
- `guide_name` (str): The name of the guide.
- `plagiarism_check` (str): The plagiarism check option.
- `grammar_check` (str): The grammar check option.
- `language` (str): The language of the document.
- `file_path` (str): The path to the file to upload.

### debug_request(request)
Prints debugging information about the API request.

#### Args:
- `request`: The API request object.

### debug_response(response)
Prints debugging information about the API response.

#### Args:
- `response`: The API response object.

### create_submission(folder_id, submission_id, name, title, assignment_id, doc_type, file_path)
Creates a new submission in a folder.

#### Args:
- `folder_id` (str): The ID of the folder.
- `submission_id` (str): The ID of the submission.
- `name` (str): The name of the submission.
- `title` (str): The title of the submission.
- `assignment_id` (str): The ID of the assignment.
- `doc_type` (str): The type of the document.
- `file_path` (str): The path to the file to upload.

### download_file(paper_id, d_key)
Downloads a file from the Drillbit Plagiarism Check API.

#### Args:
- `paper_id` (str): The ID of the paper.
- `d_key` (str): The download key.

### get_folders_list(page, size, field, order_by)
Retrieves a list of folders from the Drillbit Plagiarism Check API.

#### Args:
- `page` (int): The page number.
- `size` (int): The number of items per page.
- `field` (str): The field to sort by.
- `order_by` (str): The sort order.

### get_submissions_list(folder_id, page, size, field, order_by)
Retrieves a list of submissions from a folder in the Drillbit Plagiarism Check API.

#### Args:
- `folder_id` (str): The ID of the folder.
- `page` (int): The page number.
- `size` (int): The number of items per page.
- `field` (str): The field to sort by.
- `order_by` (str): The sort order.

### delete_folder(folder_id)
Deletes a folder from the Drillbit Plagiarism Check API.

#### Args:
- `folder_id` (str): The ID of the folder.

### edit_folder(folder_id, folder_name)
Edits a folder in the Drillbit Plagiarism Check API.

#### Args:
- `folder_id` (str): The ID of the folder.
- `folder_name` (str): The new name of the folder.

### delete_submission(folder_id, paper_id)
Deletes a submission from a folder in the Drillbit Plagiarism Check API.

#### Args:
- `folder_id` (str): The ID of the folder.
- `paper_id` (str): The ID of the submission.

