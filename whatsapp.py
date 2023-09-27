from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

app = Flask(__name__)

# Your Twilio Account SID and Auth Token
account_sid = 'AC10aa0cbe30e8f024a98de88fe9879e32'
auth_token = '0937bff5ef2ef82662da3bf922d1d8e6'
# Create a Twilio client
client = Client(account_sid, auth_token)

# Your Twilio WhatsApp-enabled phone number
twilio_phone_number = '+16295002466'

# The link for "Find us here at Canal Walk" and other URLs
cw = "https://tinyurl.com/CW1FalcoMilano"
sw = "https://tinyurl.com/FalcoMilanoSW1"
apk = "https://tinyurl.com/1APKFalcoMilano"
gw = "https://tinyurl.com/GW1FalcoMilno"
ga = "https://tinyurl.com/GM1FalcoMilano"
mp = "https://tinyurl.com/MP1FalcoMilano"
bl = "https://tinyurl.com/BL1FalcoMilano"
tg = "https://tinyurl.com/TG1FalcoMilano"
ce = "https://tinyurl.com/CE1FalcoMilano"
wl = "https://tinyurl.com/Wood1andsMall"
sc = "https://tinyurl.com/SandtonCityMa11"
eg = "https://tinyurl.com/EG1FalcoMilano"
fw = "https://tinyurl.com/FW1FalcoMilano"
gl = "https://tinyurl.com/GL1FalcoMilano"

logo_url = "https://drive.google.com/uc?id=1m2ZC73oUa5pGj5hTb2QxmY-2f8dc1A1F"

# Your chatbot logic here
@app.route("/")
def hello():
    return "Hello, this is working"

@app.route("/bot", methods=["POST"])
def reply_to_message():
    incoming_message = request.values.get("Body", "").lower()
    response = MessagingResponse()
    msg = response.message()

    if 'hello' in incoming_message:
        reply_text = "Thank you for contacting Falco Milano, how can we assist you?\n" \
                     " \n" \
                     "*1* - Shop Online\n" \
                     "*2* - Follow us on Social Media\n" \
                     "*3* - Track my optic purchase\n" \
                     "*4* - Contact Us\n" \
                     "     *CPT*   Cape Town stores\n" \
                     "     *DBN*   Durban stores\n" \
                     "     *PTA*   Pretoria stores\n" \
                     "     *JHB*   Johannesburg stores\n" \
                     " \n" \
                     " *Please select an option for more assistance*"
        # Add the logo image as a thumbnail
        msg.media(logo_url)
        msg.body(reply_text)
    elif '1' in incoming_message:
        reply_text = "https://falcomilano.co.za\n"\
                     "Get Free delivery anywhere within South Africa"
        msg.body(reply_text)
    elif '2' in incoming_message:
        reply_text = "Follow us on social media:\n" \
                     " \n" \
                     "*Facebook*:\n"\
                     "https://www.facebook.com/FalcoMilanoSA/\n" \
                     " \n" \
                     "*Instagram*:\n"\
                     "https://www.instagram.com/falcomilano_sa/"\
                     " \n"
        msg.body(reply_text)
    elif '3' in incoming_message:
        reply_text = "This feature will be released soon and is currently not available yet."
        msg.body(reply_text)
    elif '4' in incoming_message:
        reply_text = "*Customer Care*:\n" \
                     "Email: hello@falcomilano.co.za\n" \
                     " \n" \
                     "*Accounts & Refunds*:\n" \
                     "Email: accounts@falcomilano.co.za\n" \
                     " \n"
        msg.body(reply_text)
    elif 'cpt' in incoming_message:
        # Cape Town (CPT) stores
        reply_text = "CAPE TOWN STORES\n" \
                     " \n" \
                     "*Access Park Kenilworth*\nEmail: accesspark@falcomilano.co.za\nPhone: +27210075885\n" \
                     f"Google Map Address: {apk} \n" \
                     " \n" \
                     "*Canal Walk Shopping Centre*\nEmail: cw@falcomilano.co.za\nPhone: +27210075817\n" \
                     f"Google Map Address: {cw} \n" \
                     " \n" \
                     "*Somerset West*\nEmail: sw@falcomilano.co.za\nPhone: +27210075819\n"\
                     f"Google Map Address: {sw} \n"
        msg.body(reply_text)
    # ... (similar logic for other locations)
    else:
        reply_text = "Sorry, I don't recognize that command. Type 'hello' for assistance."
        msg.body(reply_text)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
