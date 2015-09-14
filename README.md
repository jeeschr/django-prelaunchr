# PRELAUNCHER #

Test for market interest and make product adjustments before a launch by running an email collection campaign. Users can refer friends using a unique referral code and earn prizes. This is an application for email referral based on the likes of Harry's Prelaunchr and websites such as Kickofflabs. 

## Running a Django web application for new users ##

Run pip install -r requirements.txt in the folder. Run python manage.py runserver command. Access the website via localhost:8000 in browser.

## How it works ##

Users are prompted to enter their email address to find out more about an upcoming product or service. Every user is given a unique referral code and tracked by ip address. The user is then taken to a page with which they may share their given referral code or see how they rank in terms of prize winning. Users must earn more referrals in order to win prizes. This application makes use of a few outside components: templated_email, ipware, and facebook applications

## IP address tracking ##

The python package ipware is used in order to save each user's ip address along with each sign up. The count of each unique ip address address signup is also saved. When an ip address is found to have been saved more than 2 times, then that user and all subsequent referred users are flagged as a suspicious user.

## Setup ##

Depending on whether you want to run this application in development or production mode, the according change must be made in the main manage.py file. It is also possible for this application to send an initial notificaiton email after signup. Then it is necessary to be sure all email settings are correct in the settings file. This application makes use of the templated_email app in order to accomplish any email sending.

## To do ##

Code needs to be cleaned up

CSS needs to be fixed

Settings file needs to be added 
