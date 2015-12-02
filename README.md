# Django Prelaunchr #

Test the market before launch by running an email collection campaign. Users can refer friends using a unique referral code and earn prizes. This application is based on the likes of [Harry's Prelaunchr](https://github.com/harrystech/prelaunchr) and websites such as [Kickofflabs](https://kickofflabs.com/).

## How it works ##

Users are prompted to enter their email address. This generates a unique referral code, saves the ip address, and creates a cookie-based session. 

Upon form completion, the user is taken to a page with which they may share their given referral code or see how they rank in terms of number of referrals generated. 

Users must earn more referrals in order to win prizes. This is stressed by bouncing users who have already signed up to the referral page, should they attempt to go to the original URL again.

This application makes use of a few outside components: templated_email, ipware, and facebook applications.

[See it in action](http://www.boozepigeon.com)

## Referrer tracking ##

Each user may have 1 unique referrer linked to his or herself. The corresponsing referral code is generated using the hexlify function until the unique constraint is met.

## IP address tracking ##

The ipware package is used in order to save each user's ip address along with each sign up. The count of each unique ip address address signup is also saved. When an ip address is found to have been saved more than 2 times, that user and all subsequent referred users are flagged as suspicious.

## Followup email ##

After the user has signed up and is taken to the referral page, an email is dispatched through Django using the templated_email package. This email makes use of a facebook application in order for easier sharing of the referral link.

## Setup ##

Setup is typical Django. Make sure you create the database and install all requirements. If you like, you may run the development environment using Grunt.

Email functionality requires setup as well. Make sure that the settings files are correct for that.

A Facebook application ID needs to be setup in both the templates/social_share_contest.html and the templates/templated_email/welcome.email files.

## Note ##

The css is still a little funny for the mobile view. The prize progress does not display correctly for that case.

## Credits ##
[django-ipware](https://github.com/un33k/django-ipware)
[django-templated-email](https://github.com/BradWhittington/django-templated-email)

