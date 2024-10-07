import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('othor3422@gmail.com', 'just$for$demo')

server.sendmail('othor3422@gmail.com', 'sinahanbilly@gmail.com', 'Mail sent from Python code')
print("Mail Sent")

