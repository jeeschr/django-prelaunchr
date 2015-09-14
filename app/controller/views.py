from django.shortcuts import render, redirect
from users.models import *
from users.forms import ContestForm
from django.http import JsonResponse
from django.views.generic import View
# USE FUNCTION get_real_ip FOR PROD
from ipware.ip import get_real_ip, get_ip

from django.conf import settings
from django.core.mail import send_mail
from templated_email import send_templated_mail

def contest_landing_page(request,ref=None):

	if 'h_email' in request.session:
		email = request.session['h_email']
		try:
			user = User.objects.get(email=email)
			# if user:
			# 	return redirect('thanks-share-us')
		except:
			del request.session['h_email']	
	if ref:
		try:
			user = User.objects.get(referral_code=ref)
			if user:
				request.session['h_ref'] = user.referral_code
				request.session.set_expiry(600000)
		except:
			pass
	else:
		ref = ''
	return render(request, 'contest_landing_page.html', {'ref_code':ref})

class createUser(View):

	def post(self, request):
		form = ContestForm(request.POST)
		if form.is_valid():
			userEmail = request.POST['email']
			user = User.objects.create(email=userEmail)

			# CONFIGURE TO SEND EMAIL
			# send_templated_mail(
		 #        template_name='welcome',
		 #        from_email='Booze Pigeon <TEST@TEST.com>',
		 #        recipient_list=[userEmail],
		 #        context={
		 #            'ref_code':user.referral_code
		 #        }
			# )

			request.session['h_email'] = userEmail
			request.session.set_expiry(800000)
			

			# USE FUNCTION get_real_ip FOR PROD, get_ip FOR DEV
			ip=get_ip(request)
			# ip=get_real_ip(request)	
			
			# returns True if new obj newIP is created
			curr_ip, newIP = IP_Address.objects.get_or_create(address=ip)
			if newIP:
				pass
			else:
				if curr_ip.count > 2:
						user.repeat_ip = True
						user.save()
				curr_ip.count = curr_ip.count + 1
				curr_ip.save()
			if 'h_ref' in request.session:
				ref = request.session['h_ref']
				try:
					referred_by = User.objects.get(referral_code=ref)
					if referred_by:
						refer, newRefer = Referrer.objects.get_or_create(referral_code=ref)
						user.referrer = refer
						if referred_by.repeat_ip:
							user.repeat_ip = True
						user.save()
				except:
					del request.session['h_ref']
			return redirect('thanks-share-us')
		else:
			return render(request, 'contest_landing_page.html', {'errors': form.errors})

def thanks_share_us(request):

	if 'h_email' in request.session:
		email = request.session['h_email']
		request.session.set_expiry(800000)
		try:
			user = User.objects.get(email=email)
			if user:
				ref = user.referral_code
				try:
					isreferrer = Referrer.objects.get(referral_code=ref)
					if isreferrer:
						numreferrals = User.objects.filter(referrer=isreferrer).count()
						numentries = numreferrals + 2
				except:
					numreferrals = 0
					numentries = 2
		except:
			del request.session['h_email']
			return render(request, 'contest_landing_page.html', {})
	else:
		return render(request, 'contest_landing_page.html', {})

	return render(request, 'social_share_contest.html', {'ref_code': ref, 'referrals': numreferrals, 
		'entries': numentries})

















