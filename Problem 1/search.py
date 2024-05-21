"""
code to search for a phone number and get its details
"""


# import libs
import asyncio
from truecallerpy import search_phonenumber
#########


phone_number = "+989134415604"
country_code = "IR"
installation_id = "a1i0K-MnlsotJYGLUtzssqSKR8vjoJPQVQ9HAQHg9vOcPam7CG5VRW"

response = asyncio.run(search_phonenumber(phone_number, country_code, installation_id))
print(response)


# responded json (all details)
#{'status_code': 200, 'data': {'data': [{'id': 'J95QBhDTg2hYdhQI6JXDjg==', 'name': 'کسری کاظمی خدمت', 'score': 0.30672404, 'access': 'PUBLIC', 'enhanced': True, 'phones': [{'e164Format': '+989134415604', 'numberType': 'MOBILE', 'nationalFormat': '0913 441 5604', 'dialingCode': 98, 'countryCode': 'IR', 'carrier': 'MCI', 'type': 'openPhone'}], 'addresses': [{'area': 'IR', 'city': 'Area 3', 'countryCode': 'IR', 'timeZone': '+03:30', 'type': 'address'}], 'internetAddresses': [], 'badges': [], 'tags': [], 'nameFeedback': {'nameSource': 1, 'nameElectionAlgo': '20221010'}, 'cacheTtl': 1296000000, 'sources': [], 'searchWarnings': [], 'surveys': [{'id': '02eac7f6-3842-4d86-a45e-f2e2e23aa3a6', 'frequency': 3600, 'passthroughData': 'eyAiNCI6ICJ1Z2MiLCAiMiI6ICLaqdiz2LHbjCDaqdin2LjZhduMINiu2K/ZhdiqIiwgIjMiOiAiOTg5MTM0NDE1NjA0IiwgIjgiOiAiMSIsICI1IjogIjIwMjIxMDEwIiB9', 'perNumberCooldown': 31536000, 'dynamicContentAccessKey': ''}, {'id': '76a273b3-cc72-4646-89f3-487071a622cd', 'frequency': 3600, 'passthroughData': 'eyAiNCI6ICJ1Z2MiLCAiMiI6ICLaqdiz2LHbjCDaqdin2LjZhduMINiu2K/ZhdiqIiwgIjMiOiAiOTg5MTM0NDE1NjA0IiwgIjgiOiAiMSIsICI1IjogIjIwMjIxMDEwIiB9', 'perNumberCooldown': 31536000, 'dynamicContentAccessKey': ''}], 'commentsStats': {'showComments': False}, 'manualCallerIdPrompt': False, 'ns': 7}], 'provider': 'ss-nu', 'stats': {'sourceStats': []}}}