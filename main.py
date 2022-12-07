#import necessary libraries
import requests
import json

#define the base URL
base_url = 'https://app.schoology.com/api/v1/'

#define the API key
api_key = 'YOUR_API_KEY'

#define the headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

#define the endpoint
endpoint = 'courses'

#construct the request
request = requests.get(base_url + endpoint, headers=headers)

#parse the response
response = json.loads(request.text)

#print the response
print(response)
