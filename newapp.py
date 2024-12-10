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