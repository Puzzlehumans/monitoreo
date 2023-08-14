import os
from dotenv import load_dotenv
# import email
# from email.message import EmailMessage
# import ssl
# import smtplib
import smtplib, getpass, ssl, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64


load_dotenv()
def send_mail(destino):
    password = os.getenv('MAIL_PASSWORD')
    email_sender = "pruebaspuzzlehumans@gmail.com"
    email_reciver = destino
    asunto = "Alerta de Alarma - Sistema de monitoreo "
    body = """
        <html>
        <body>
            <h1>¡Alerta! Sistema de monitero </h1>
            <h3>Proyecto: Sr. Bader</h3>
            <p>Este correo es un correo autogenerado para avisar de una alerta accionada en el sistema de monitoreo.
        </body>
        </html>
    """

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = asunto
    mensaje["From"] = email_sender
    mensaje["to"] = email_reciver


 
    parte_html = MIMEText(body,"html")
    mensaje.attach(parte_html)


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context =context) as server:
        server.login(email_sender, password)    
        server.sendmail(email_sender,email_reciver,mensaje.as_string())
        server.quit()

