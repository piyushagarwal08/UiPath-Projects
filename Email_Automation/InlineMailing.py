import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders


def SendMail(From,Password,To,Message,Subject,ImgPath,attachment_path_list=None):
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

        
    if attachment_path_list is not None:
            attachment_list = attachment_path_list.split(",")
            for each_file_path in attachment_list:
                try:
                    file_name=each_file_path.split("\\")[-1]
                    part = MIMEBase('application', "octet-stream")
                    part.set_payload(open(each_file_path, "rb").read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment' ,filename=file_name)
                    msgRoot.attach(part)
                except:
                    continue
                
    ImgPath_List = ImgPath.split(",")
    counter = 0
    for eachImage in ImgPath_List:
        try:
            counter = counter+1
            fp = open(eachImage, 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()
            msgImage.add_header('Content-ID', '<image'+str(counter)+'>')
            msgRoot.attach(msgImage)
        except:
            continue
    
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()
    smtp.login(strFrom,Password)
    smtp.sendmail(strFrom,strTo,msgRoot.as_string())
    smtp.quit()
    return "mail send"


