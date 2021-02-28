import smtplib
import os
import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

addr_to = 'ves039a@gmail.com'

def send_email(addr_to, dir_name):
    login = '999klad@gmail.com'
    passwort = 'lexusis50'
    msg_text = "Sehr geehrte Damen und Herren,\n\nin den Anlagen finden Sie meine Bewerbung.\n\nMit freundlichen Grüßen\nIgor Engler "
    theme = 'Bewerbung Engler'
    msg = MIMEMultipart()
    msg['From']    = login
    msg['To']      = addr_to
    msg['Subject'] = theme

    body = msg_text
    msg.attach(MIMEText(body, 'plain'))
    
    process_attachement(msg,files)

    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.starttls()
    smtpObj.login(login,passwort)
    smtpObj.send_message(msg)
    smtpObj.quit()

def process_attachement(msg,files):

    for a_file in files:
        attachment = open(a_file, 'rb')
        file_name = os.path.basename(a_file)
        part = MIMEBase('application','octet-stream')
        part.set_payload(attachment.read())
        part.add_header('Content-Disposition',
                        'attachment',
                        filename=file_name)
        encoders.encode_base64(part)
        msg.attach(part)

    # files = os.listdir(dir_name)
    # f = open("A:\it\Bewerbung_1-1.pdf", "rb")
    # encoders.encode_base64(f)
    # msg.set_payload(f.read())
    # msg.attach(MIMEText(f.read()))
    
    
# def attach_file(msg,filepath):
#     filename = os.path.basename(filepath)
#     ctype, encoding = mimetypes.guess_type(filepath)
#     if ctype is None or encoding is not None:
#         ctype = 'application/octet-stream'
#     maintype,subtype = ctype.split('/',1)
#     if maintype == 'text':
#         with open(filepath) as fp:
#             file = MIMEText(fp.read(), _subtype = subtype)
#             fp.close()
#     else:
#         with open(filepath,'rb') as fp:
#             file = MIMEBase(maintype,subtype)
#             file.set_payload(fp.read())
#             fp.close()
#             encoders.encode_base64(file)
#     file.add_header('Content-Disposition', 'attachment', filename = filename)        



def starting():
    dir_name = "A:\it\it_firmen\\"
    fil = os.listdir(dir_name) 
    files = []
    for i in fil:
        k = dir_name + i
        files.append(k)
    
send_email(addr_to,files)


