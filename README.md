# Whatsapp Automation

## Setup
* Create a folder named ```Whatsapp Bot``` in ```Packages``` folder
* Copy the ```Data``` folder inside it

## Process
* Before running the bot, open the ```Whatsapp Desktop``` application manually
* When you run the bot,it will ask for message.txt file and contacts.xlsx file
* The format of ```contact.xlsx``` file is same as ```contacts.csv``` file that can be downloaded from ```contacts.google.com``` with sheet name ```contacts```
* The whatsapp receivers are searched using ```Additional Name``` + ```Name``` column field values and customized name is used from ```Given Name``` field
* If a user is not found on ```whatsapp``` then the message is delivered to first number in your contact list (A bug still working on)

## Note
* A Sample input file can be find in ```Data/Input``` folder named ```contact.xlsx```
