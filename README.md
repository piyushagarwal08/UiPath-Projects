# Email Automation
* Create an Excel file with headers Name and Email
* Save the Email_Automation folder and ```.nupkg``` file in the path ```C:\ProgramData\UiPath\Packages```
* The attachments folder path and error file path can be configured in the text file present in this folder

## Note
* Before using this bot, please open ```https://myaccount.google.com/lesssecureapps```
* And turn on the toggle
* If two way authentication is set in account then please generate an 3rd party app passwords and use it to send mails ```https://support.google.com/mail/answer/185833?hl=en-GB```

## Process
* Click on run button in Bot Assistant
* A Form appears on Screen which is to be filled to send mail just like one would have send using Gmail / Outlook
* Read the Note written in the form before sending mail
* After filling the form, select the Excel file with Email list containing two excel headers (atleast) :- "Name" and "Email"
* To send any attachments, just save all the files in the attachments folder whose path is given in the ```AttachmentsFolderPath.txt``` during the Setup Process




