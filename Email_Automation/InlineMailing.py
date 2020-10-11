import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def SendMail(From,Password,To,Message,Subject,ImgPath):
    strFrom = From
    strTo = To

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Subject
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    
    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)
    
    msgText = MIMEText(Message, 'html')
    msgAlternative.attach(msgText)

    
    fp = open(ImgPath, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)
    
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()
    smtp.login(strFrom,Password)
    smtp.sendmail(strFrom,strTo,msgRoot.as_string())
    smtp.quit()
    return "Mail Sent"
