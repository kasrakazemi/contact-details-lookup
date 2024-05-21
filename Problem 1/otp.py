"""
code to verify otp and get installation id
"""


# import libs
import asyncio
from truecallerpy import verify_otp
##########


phone_number = "+989111111111"
json_data =  {'status': 1, 'message': 'Sent', 'domain': 'noneu', 'parsedPhoneNumber': 989111111111, 'parsedCountryCode': 'IR', 'requestId': '01ee4927-07d5-bc8f-d7f4228af65c', 'method': 'sms', 'tokenTtl': 300}

otp = "555555"

response = asyncio.run(verify_otp(phone_number, json_data, otp))
print(response)


# responded json 
# {'status_code': 200, 'data': {'status': 3, 'message': 'Already verified', 'installationId': 'a1i0K-MnlsotJYGLUtzssqSKR8vjoJPQVQ9HAQHg9vOcPam7CG5VRW', 'ttl': 259200, 'userId': 14011696151724544, 'suspended': False, 'phones': [{'phoneNumber': 989131973287, 'countryCode': 'IR', 'priority': 1}]}}