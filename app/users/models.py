from django.db import models
from .signals import *
import os
from binascii import hexlify
# from django.contrib.sites.models import Site

class Referrer(models.Model):
	referral_code = models.CharField(blank=True,null=True, max_length=18)

	def __unicode__(self):
		return self.referral_code

class User(models.Model):
	email = models.EmailField(unique=True, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	referral_code = models.CharField(blank=True, max_length=10, unique=True)
	referrer = models.ForeignKey('Referrer', blank=True, null=True)
	repeat_ip = models.BooleanField(default=False)
	ip_address = models.CharField(max_length=120, blank=True)
	referrals = models.IntegerField(default=0)

	def save(self, *args, **kwargs):
		new_code = hexlify(os.urandom(4))
		collision = User.objects.filter(referral_code=new_code).exists()
		while collision:
			new_code = hexlify(os.urandom(4))
			collision = User.objects.filter(referral_code=new_code).exists()
		self.referral_code = new_code
		super(User, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.email

post_save.connect(update_referrals, sender=User)

class IP_Address(models.Model):
	address = models.CharField(max_length=120,unique=True)
	count = models.IntegerField(blank=False,default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = 'IP Addresses'

	def __unicode__(self):
		return self.address

