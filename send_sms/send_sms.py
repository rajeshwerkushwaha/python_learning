# send SMS using twilio
# https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python?code-sample=code-send-an-sms-using-the-programmable-sms-api&code-language=Python&code-sdk-version=6.x

# pre-requisite
# pip install twilio


# Download the helper library from https://www.twilio.com/docs/python/install
# from twilio.rest import Client


# # Your Account Sid and Auth Token from twilio.com/console
# # DANGER! This is insecure. See http://twil.io/secure
# account_sid = '1111111111111111111111111111111'
# auth_token = '2222222222222222222222222222222'
# client = Client(account_sid, auth_token)

# message = client.messages \
#     .create(
#          body='This is the ship that made the Kessel Run in fourteen parsecs?',
#          from_='999999999999',
#          to='999999999999'
#      )

# print(message.sid)



# using fast2sms
# importing the requests library 
import requests 
  
# api-endpoint 
url = "https://www.fast2sms.com/dev/bulk"
headers = {
    'authorization': "API_Authorization_Key",
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }
payload = "sender_id=FSTSMS&language=english&route=qt&numbers=".urlencode('9999999999')."&message=YOUR_QT_SMS_ID&variables=".urlencode('{#AA#}|{#CC#}')."&variables_values=".urlencode('12345|asdaswdx').""

# sending get request and saving the response as response object 
response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)


