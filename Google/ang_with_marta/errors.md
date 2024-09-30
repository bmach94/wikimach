

(game) mach@mach-thinkpad:~/Dokumenty/PYTHON/Review/Google/wikimach/Google/ang_with_marta$ python g_sheets.py 
An error occurred: ('invalid_grant: Invalid JWT Signature.', {'error': 'invalid_grant', 'error_description': 'Invalid JWT Signature.'})
Traceback (most recent call last):
  File "/home/mach/Dokumenty/PYTHON/Review/Google/wikimach/Google/ang_with_marta/g_sheets.py", line 267, in <module>
    listener = KeyboardActions()
  File "/home/mach/Dokumenty/PYTHON/Review/Google/wikimach/Google/ang_with_marta/g_sheets.py", line 144, in __init__
    self.all_values = self.sheet.get_all_values() # dataframe
AttributeError: 'NoneType' object has no attribute 'get_all_values'

Resolution:


To generate a new service account key for Google Cloud or Google APIs, follow these steps. This key is used for programmatic access and contains private information, so handle it carefully.

Steps to Create a New Service Account Key:
Go to the Google Cloud Console:

Visit Google Cloud Console.
Select or Create a Project:

In the top bar, select the project for which you want to create a service account key.
If you don’t have a project yet, click "New Project" and create one.
Open the IAM & Admin Page:

On the left-hand menu, go to IAM & Admin > Service Accounts.
Create a New Service Account (if you don’t have one):

Click the "+ CREATE SERVICE ACCOUNT" button at the top.
Provide a Service account name, and optionally, a description. Click Create.
Assign Roles:

In the next step, assign the appropriate role(s) for the service account. For example, if your service account needs to access Google Cloud Storage, you might assign it the "Storage Admin" role.
Click Continue.
Create the Key:

On the next screen, check Create Key.
Select JSON as the key type.
Click Create. A .json file containing the new private key will be automatically downloaded to your computer.
Save the JSON Key:

The downloaded JSON file contains all the information needed, including the private_key, client_email, client_id, etc. This is your new service account key.
Example of a Newly Generated Service Account JSON:
After downloading, the key file will look like this (but with actual values):

json
Skopiuj kod
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "some-private-key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANB ... \n-----END PRIVATE KEY-----\n",
  "client_email": "your-service-account@your-project-id.iam.gserviceaccount.com",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account@your-project-id.iam.gserviceaccount.com"
}
Important Notes:
Secure Storage: Store the key file in a secure location and do not share it publicly (e.g., in repositories).
Permissions: Ensure the service account has the appropriate permissions for the resources it needs to access.
Key Rotation: If you need to rotate or regenerate keys, you can always go back to the Google Cloud Console and create new keys for the existing service account.
This process will generate a new service account key that you can use in your application.