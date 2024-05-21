######## import libs
import requests
################


search_url = "https://api.rocketreach.co/api/v2/person/lookup"

# Search parameters
search_email = input('please type your email address:')
params = {
  
  "email": search_email
}

# Send the search request
response = requests.get(search_url, params=params, headers= {"Api-Key": "your-api-key"})

# Check for successful response
if response.status_code == 200:
  data = response.json()
  print('Responded Person Details From Rocketreach:','\n',data)

else:
  print(f"No data found or Error: {response.status_code}")
