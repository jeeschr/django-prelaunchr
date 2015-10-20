# Prelauncher #

Test for market interest and make product adjustments before a launch by running an email collection campaign. Users can refer friends using a unique referral code and earn prizes. This is an application for email referral based on the likes of Harry's Prelaunchr and websites such as Kickofflabs. 

[See it in action](http://www.boozepigeon.com)

## How it works ##

Users are prompted to enter their email address to find out more about an upcoming product or service. Every user is given a unique referral code and tracked by ip address and Django's cookie-based sessions. Upon form completion, the user is taken to a page with which they may share their given referral code or see how they rank in terms of number of referrals generated. 

Users must earn more referrals in order to win prizes. This is stressed by bouncing users who have already signed up to the referral page, should they attempt to go to the original URL again.

This application makes use of a few outside components: templated_email, ipware, and facebook applications - so be sure to set all these up

## IP address tracking ##

The ipware package is used in order to save each user's ip address along with each sign up. The count of each unique ip address address signup is also saved. When an ip address is found to have been saved more than 2 times, that user and all subsequent referred users are flagged as suspicious.

## Followup email ##

After the user has signed up and is taken to the referral page, an email is sent through Django using the templated_email package. This email makes use of a facebook application in order for easier sharing of the referral link.

## Setup ##

Head to the application folder and run "pip install -r requirements.txt"

Run python manage.py runserver command and access the website via localhost:8000 in browser.

In order to use the email functionality, you need to head over to the settings files and make sure everything is correct with that. It's also necessary to setup a facebook application if you want to enable easy social sharing.

CSS needs to be fixed
