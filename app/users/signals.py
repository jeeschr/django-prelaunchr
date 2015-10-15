from django.db.models.signals import post_save
from django.dispatch import receiver

def update_referrals(sender, instance, created, **kwargs):
	if created:
		newUser = instance
		if newUser.referrer:
			user = User.objects.get(referral_code=newUser.referrer.referral_code)
			user.referrals = user.referrals + 1
			user.save()
	