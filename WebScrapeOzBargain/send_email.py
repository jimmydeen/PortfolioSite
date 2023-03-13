import smtplib, ssl

def push_email():
    sender_email = "joongdodev@gmail.com"
    receiver_email = "joongdojang@gmail.com"
    message = """\
    Subject: Bose 700 Listing!

    New Listing for Bose 700 Headphones !

    This message is sent from Python."""

# Send email here
    port = 465  # For SSL
    password = "eobyrjwcgaygtkzl"


    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("joongdodev@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)
        