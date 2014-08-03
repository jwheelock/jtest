import json
import requests

# New ticket info
subject = 'My printer is on fire!'
body = 'The smoke is very colorful.'

# Package the data in a dictionary matching the expected JSON
data = {'ticket': {'subject': subject, 'comment': {'body': body}}}

# Encode the data to create a JSON payload
payload = json.dumps(data)

# Set the request parameters
url = 'https://jwheelocklol.zendesk.com/api/v2/tickets.json'
user = 'your_email_address'
pwd = 'your_password'
headers = {'content-type': 'application/json'}

# Do the HTTP post request
response = requests.post(url, data=payload, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 201 (Created)
if response.status_code != 201:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Report success
print('Successfully created the ticket.')
