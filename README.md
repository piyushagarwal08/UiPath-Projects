# Back Admit Card Mailing Service

## Setup
* Create a folder in ```Packages``` folder named ```Team 7``` and inside it another folder named ```InputSetupFiles```
* Copy the ```Config.xlsx``` file stored in ```Data``` folder to ```InputSetupFiles``` folder
* ```UiPath.Forms.Activities``` should be installed (can be found in manage packages)

## UseCase
* The Problem was to send the Back Admit Cards generated by Back Admit Card to all the students
* The Bot is supposed to use gmail smtp server

## Process
* Select the same file given as input to ```BackAdmitCard_Generate``` bot
* A Form is opened, in which a user can give upto 4 Username and Password for gmail with subject and message to sent with
* {0} is used to get ```Name of the Student``` field from input excel file that is replace the text where you want data from excel file with {0} which will send customized mails
* The Mail content supports html coding

## Note
* Make sure ```less secure apps``` is on
* If Mail is not sent for any reason, then an ```AdmitCardNotSent.csv``` file is generated
