from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render
from django.core.mail import send_mail
from mysite.forms import ContactForm
import datetime
#from django.template import Context


def hello(request):
	return HttpResponse("1")

def current_datetime(request):
	now = datetime.datetime.now()
	'''
	t = get_template('current_datetime.html')
	#html = "It is now %s" % now
	html = t.render({'current_date': now})
	return HttpResponse(html)
	'''
	return render(request, 'current_datetime.html', {'current_date': now})#改版v1.0

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	t = get_template('Future_hours.html')
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	#html = "In %s hour(s), it will be %s" % (offset, dt)
	html = t.render({'hour_offset': offset, 'next_time': dt})
	return HttpResponse(html)
	#return HttpResponse(request, 'Future_hours.html', {'hour_offset': offset, 'next_time': dt}) 

def display_meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.appened('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@example.com'),
				['siteowner@example.com']
				)
			return HttpResponseRedirect('/contact/thanks')
	else:
		form = ContactForm(
			initial = {'subject': 'My site'}
			)
	return render(request, 'contact_form.html', {'form': form})

