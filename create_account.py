# The SDK does not have tools for creating test accounts, so you'll have to
# make your own HTTP request.

# if you're trying this on Python, install the `requests` library.
import requests

public_key = "GDJNTEOKKOU6QNS6WEP7Z6SVR3ORB3DQ3V4NAUSNPDZ7WFGMN4ZUCXIT"
response = requests.get(f"https://friendbot.stellar.org?addr={public_key}")
if response.status_code == 200:
    print(f"SUCCESS! You have a new account :)\n{response.text}")
else:
    print(f"ERROR! Response: \n{response.text}")
