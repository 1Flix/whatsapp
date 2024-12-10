import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/run-script', methods=['GET', 'POST'])
def run_script():


    from twilio.rest import Client

    account_sid = "AC92208f644247640d7c087a7fe2b8c2b6"
    auth_token = "09e03ff13455728074ab08164749737e"


    client = Client(account_sid, auth_token)


    from_whatsapp_number = "whatsapp:+14155238886"


    to_whatsapp_number = "whatsapp:+4915750955234"

    client.messages.create(
        body="Hello, How are you?",
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )


    result = "Das Python-Skript wurde erfolgreich ausgeführt!"
    return jsonify({"status": "success", "result": result})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)