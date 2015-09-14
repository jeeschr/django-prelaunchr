from django.db.models.signals import post_save

def update_referrals(sender, **kwargs):
	# print 'We got it: ', instance
	print ' and also: ', kwargs['instance']
	# if referrer:
	# 	user = User.objects.get(referral_code=ref)
	# 	user.referrals = user.referrals + 1
	# 	user.save()