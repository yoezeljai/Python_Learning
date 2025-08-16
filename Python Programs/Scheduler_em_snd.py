#
import schedule
def snd_em():
    import smtplib
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('prakashjai12699@gmail.com','j@!685921K')
    message='hi this is a schedule text message'
    server.sendmail('prakashjai12699@gmail.com','prakashjai12699@gmail.com',message)
    server.quit()
schedule.every(1).minutes.do(snd_em)
while(True):
    schedule.run_pending()
    #print('EMAIL SEND')

