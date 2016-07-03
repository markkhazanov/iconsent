from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EmailForm, JoinForm
from .models import Join
import uuid
# Create your views here.

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip

def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id


def home(request):
	try:
		join_id = request.session['join_id_ref']
		obj = Join.objects.get(id=join_id)
	except:
		obj = None

	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		#new_join.ip_address = get_ip(request)
		#new_join.save()
		if created:
			new_join_old.ref_id = get_ref_id()
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
			return HttpResponseRedirect("")
	context = {"form": form}
	template = "home.html"
	return render(request, template, context)

def about(request):
	context = {}
	template = "about.html"
	return render(request, template, context)

def methodology(request):
	context = {}
	template = "methodology.html"
	return render(request, template, context)

def advisors(request):
	context = {}
	template = "advisors.html"
	return render(request, template, context)

def contact(request):
	context = {}
	template = "contact.html"
	return render(request, template, context)

