"""
code to login to the truecaller and get the request id in response
"""


# import libs
import asyncio
from truecallerpy import login
##########


phone_number = "+989111111111"
response = asyncio.run(login(phone_number))
print(response)


# responded json :
# {'status_code': 200, 'data': {'status': 1, 'message': 'Sent', 'domain': 'noneu', 'parsedPhoneNumber': 989111111111, 'parsedCountryCode': 'IR', 'requestId': '01ee4927-07d5-bc8f-d7f4228af65c', 'method': 'sms', 'tokenTtl': 300}}