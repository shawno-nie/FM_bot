from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, Response
from googlesearch import search

# Your Twilio Account SID and Auth Token from twilio.com/console
account_sid = 'AC10aa0cbe30e8f024a98de88fe9879e32'
auth_token = '0937bff5ef2ef82662da3bf922d1d8e6'
twilio_phone_number = '+16295002466'

client = Client(account_sid, auth_token)

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hello' in incoming_msg:
        msg.body("Hello! How can I assist you?")
    elif 'help' in incoming_msg:
        msg.body("I'm here to help. What do you need?")
    else:
        msg.body("Sorry, I didn't understand that. Type 'help' for assistance.")

    return str(resp)

if __name__ == "__main__":
    app.run()
