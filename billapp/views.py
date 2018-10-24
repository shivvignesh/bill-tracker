from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from billapp.models import Bill,Expense
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import pygal
from pygal.style import Style

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return redirect("/login/")

	bills=Bill.objects.filter(user=request.user).order_by('due_date')
	username=request.user.username
	if request.method=="POST":
		
		name=request.POST.get('name')
		amount=request.POST.get('amount')
		due_date=request.POST.get('due_date')
		
		


		Bill.objects.create(user=request.user,name=name,amount=amount,due_date=due_date)

		
		return HttpResponseRedirect("/")
		return render(request,"billapp/index.html",{'Bills':Bills})

	return render(request,'billapp/index.html',{'bills':bills,'username':username})

def add(request):

	if not request.user.is_authenticated:
		return redirect("/login/")

	if request.method=="POST":
		name=request.POST.get('name')
		amount=request.POST.get('amount')
		due_date=request.POST.get('due_date')
		

		Bill.objects.create(user=request.user,name=name,amount=amount,due_date=due_date)

		return HttpResponseRedirect("/")	

	return render(request,"billapp/form.html")

# def delete(request,pk):
	
# 		# entry=get_object_or_404(Entry,pk=pk)	
# 		# entry.delete()
# 	Bill.objects.get(pk=pk).delete()
# 		#entry=Entry.objects.get(pk=pk)
# 		#entry.delete()

# 	bill=Bill.objects.filter(user=request.user)
# 	return render(request,'billapp/index.html',{'bill':bill})




def signup(request):
	# if request.user.is_authenticated:
	# 	return 	redirect("/home/")

	if request.method=="POST":
		email=request.POST.get('email')
		password1=request.POST.get('password1')
		password2=request.POST.get('password2')
		
		try:
			user=User.objects.get(username=email)
			return render(request,"billapp/signup.html",{"error":"user with this email already exists"})
		except:
			if password1==password2:
				user=User.objects.create_user(username=email,email=email,password=password1,is_staff=True)

				login(request,user)

				return redirect("/")

			else:
				return render(request,"billapp/signup.html",{"error":" the passwords do not match "})	

	return render(request,"billapp/signup.html")			

def signin(request):
	
	if request.method=="POST":
		email=request.POST.get('email')
		print(email)
		password=request.POST.get('password')
		print(password)
		user=authenticate(request,username=email,password=password) 
		print(user)
		if user is not None:
			login(request,user)

			return redirect("/")	
		else:
			print("User is None")
	return render(request,"billapp/login.html")	

def signout(request):
	logout(request)
	return redirect('/login/')

def add_expense(request):
	if not request.user.is_authenticated:
		return redirect("/login/")

	if request.method=="POST":
		income=int(request.POST.get('income'))
		bill_1=int(request.POST.get('e_bill'))
		bill_2=int(request.POST.get('w_bill'))
		bill_3=int(request.POST.get('i_bill'))

		expense=Expense(user=request.user,income=income,bill_1=bill_1,bill_2=bill_2,bill_3=bill_3)
		expense.save()

		saving=expense.subtract()
		print(saving)
		savings=str(saving)

		percent_1=float((bill_1/income)*100)
		percent_2=float((bill_2/income)*100)
		percent_3=float((bill_3/income)*100)

		percent_4=float((saving/income)*100)

		pie_chart=pygal.Pie()
		pie_chart.title='expenses'
		pie_chart.add('electricity',percent_1)
		pie_chart.add('water',percent_2)
		pie_chart.add('internet',percent_3)
		pie_chart.add('savings',percent_4)
		chart=pie_chart.render_data_uri()

		return render(request,"billapp/expense.html",{'savings':savings,'chart':chart})



	return render(request,"billapp/expense.html")

def display(request):
	if not request.user.is_authenticated:
		return redirect("/login/")

	if request.method=="POST":
		due_date=request.POST.get('due_date')
		bills=Bill.objects.filter(user=request.user,due_date=due_date)

		return render(request,"billapp/display.html",{"bills":bills})		

	return render(request,"billapp/display.html")	

def monthly(request):
	if not request.user.is_authenticated:
		return redirect("/login/")

	if request.method=="POST":
		p_money=int(request.POST.get('pocket_money'))
		daily_expense=int(request.POST.get('daily_expense'))

		xaxis= []
		dataset= []

		for i in range(1,31,1):
			xaxis.append(str(i))
			moneyleft=p_money-(daily_expense*i)
			dataset.append(moneyleft)
			if moneyleft<0:
				break
					

		days=float((p_money)/(daily_expense))
		line_chart=pygal.StackedLine(fill=True, interpolate='cubic')
		line_chart.title='pocket money'
		line_chart.x_labels=xaxis
		line_chart.add('',dataset)
		chart=line_chart.render_data_uri()

		return render(request,"billapp/monthly.html",{'days':days,'chart':chart})	

	return render(request,"billapp/monthly.html")	

def delete(request,pk):

	Bill.objects.get(pk=pk,user=request.user).delete()

	bills=Bill.objects.filter(user=request.user)
	username=request.user.username
	return redirect('/')
	return render(request,'billapp/index.html',{'bills':bills,'username':username})



