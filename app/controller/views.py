from django.shortcuts import render, redirect
from users.models import *
from users.forms import ContestForm
from django.views.generic import View

# USE FUNCTION get_real_ip FOR PROD
from ipware.ip import get_real_ip, get_ip

from django.conf import settings
from django.core.mail import send_mail
from templated_email import send_templated_mail

def contest_landing_page(request,ref=None):

	# redirect to referral page is user has already signed up
	if 'h_email' in request.session:
		email = request.session['h_email']
		try:
			user = User.objects.get(email=email)
			if user:
				return redirect('thanks-share-us')
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
	# if 'form_data' in request.session:
	# 	form_errors = request.session['form_data']
	# else:
	# 	form_errors='' 

	# return render(request, 'contest_landing_page.html', {'errors': form_errors})
	return render(request, 'contest_landing_page.html', {})
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

						# increment referring users count
						referring_user = User.objects.get(referral_code=ref)
						referring_user.referrals += 1
						referring_user.save()

						# store referral codes in db
						refer, newRefer = Referrer.objects.get_or_create(referral_code=ref)
						user.referrer = refer
						if referred_by.repeat_ip:
							user.repeat_ip = True
						user.save()
						
				except:
					del request.session['h_ref']
			return redirect('thanks-share-us')
		else:
			# request.session['form_data'] = form.errors['email'][0]
			# return redirect('contest-landing-page')
			return render(request, 'contest_landing_page.html', {'errors': form.errors['email']})

def thanks_share_us(request):

	true5 = ''
	true10 = ''
	true15 = ''
	true25 = ''

	if 'h_email' in request.session:
		email = request.session['h_email']
		request.session.set_expiry(800000)
		try:
			user = User.objects.get(email=email)
			if user:
				ref = user.referral_code
				numreferrals = user.referrals
				numentries = numreferrals + 2
				if numentries >= 0:
					width = 23
					height = 23
				if numentries >= 5:
					width = 44
					height = 47
					true5 = 'in-selection'
				if numentries >= 10:
					width = 63
					height = 75
					true10 = 'in-selection'
				if numentries >= 15:
					width = 63
					height = 100
					true15 = 'in-selection'
				if numentries >= 25:
					width = 100
					true25 = 'in-selection'
		except:
			del request.session['h_email']
			return redirect('contest-landing-page')
	else:
		return redirect('contest-landing-page')

	return render(request, 'social_share_contest.html', {'ref_code': ref, 'referrals': numreferrals, 
		'entries': numentries, 'width': width, 'height':height,'true5':true5, 'true10':true10, 'true15':true15,'true25':true25})











