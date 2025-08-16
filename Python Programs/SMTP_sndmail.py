#
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('prakashjai12699@gmail.com','j@!685921K')
message='hi this is a text message'
server.sendmail('prakashjai12699@gmail.com','prakashjai12699@gmail.com',message)
server.quit()
