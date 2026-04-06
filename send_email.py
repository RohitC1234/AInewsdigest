import os
import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "rohitshbx@gmail.com"
    password = os.getenv("SchedulePass")

    receiver = "4rohitc@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)