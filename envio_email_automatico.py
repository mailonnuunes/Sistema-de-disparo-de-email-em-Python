from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_to = "dbdacosta7@gmail.com"
email_from = "hack3rbr4sil@outlook.com.br"
paswd = "familia1212"
mensagem_corpo = '''olá, esse é um teste e eu sou o mailon'''
mensagem_titulo = "teste de titulo"

host = "smtp.office365.com"



try:
    msg = MIMEMultipart()
    msg['Subject'] = mensagem_titulo
    msg['From'] = email_from
    msg['To'] = email_to
    message = "here is the email"
    msg.attach(MIMEText(message))
    with SMTP(host,587) as smtp:
       smtp.starttls()
       smtp.login(email_from,paswd)
       print("consegui me logar com sucesso")
       smtp.sendmail(email_from,email_to,msg.as_string())
       print(f"email para {email_to} enviado com sucesso ")

except:
    print("não consegui me logar")

