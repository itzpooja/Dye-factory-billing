from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from billing.models import mt_type,received_details,bill


def signup(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		email = request.POST.get("email")

		user = User.objects.create_user(
				username=username,
				password=password,
				email=email
			)
		login(request, user)

		return redirect("/home/")

	return render(request, "signup.html")

def signin(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(username=username, password=password)

		if user != None:
			login(request, user)
			return redirect("/dashboard/")

	return render(request, "signin.html")

def signout(request):
	logout(request)
	return redirect("/signin/")

def dashboard(request):
	all_details=received_details.objects.all().order_by("dc_no")
	mtype=mt_type.objects.all()

	if request.method == "POST":
		dc_no=request.POST.get("dc_no")
		m_name=request.POST.get("m_name")
		m_length=request.POST.get("m_length")

		myobject=received_details.objects.create(
			dc_no=dc_no,
			m_name=m_name,
			m_length=m_length
			)

	return render(request,"dashboard.html",{"mtype":mtype,"all_details":all_details})

def material(request):
	all_material=mt_type.objects.all()
	if request.method == "POST":
		m_name=request.POST.get("m_name")
		mt_price=request.POST.get("mt_price")

		myobject=mt_type.objects.create(
			m_name=m_name,
			mt_price=mt_price
			)
	return render(request,"material.html",{"all_material":all_material})

def create_list(request):
	if request.method == "POST":
		m_name = request.POST.get("m_name")
		mt_price = request.POST.get("mt_price")

		
		mt_type.objects.create(
			m_type=m_name,
			mt_price=mt_price
			      )
		return redirect("/material/")

def create_details(request):
	if request.method == "POST":
		dc_no=request.POST.get("dc_no")
		m_id = request.POST.get("m_id")
		print(m_id)
		m_length= request.POST.get("m_length")
		m_name=mt_type.objects.get(pk=m_id)
		
		received_details.objects.create(
			dc_no=dc_no,
			m_name=m_name,
			m_length=m_length
		)

		return redirect("/dashboard/")
def bill(request):
	bill_details = received_details.objects.all().order_by("dc_no").values('dc_no').distinct()
	print((bill_details[0]['dc_no']))
	return render(request,"bill.html",{"bill_details":bill_details})

def generate(request,numb):
	myobject=received_details.objects.filter(dc_no=numb)
	
	items_price = []
	for i in myobject:
		items_price.append(i.m_name.mt_price * i.m_length)
		print(items_price)

	my_object = zip(myobject, items_price)
	total_price = sum(items_price)

	return render(request,"generate.html",{"my_object":my_object, "total_price":total_price})
