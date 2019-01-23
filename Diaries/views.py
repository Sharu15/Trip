from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.utils import timezone
# from .models import 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from Diaries.models import Plan,Post,Comment,Profile


# Create your views here.
def tripdiaries(request):
	if request.user.is_authenticated:
		return redirect("/home") 	
	return render(request, 'firstpage.html')

def signup(request):
	if request.method=="POST":
		username = request.POST.get('username',None)
		password = request.POST.get('password',None)
		email=request.POST.get("email")
		try:
			user = User.objects.get(username=username)
			print(user)
		except:
			user=None
		
		if user is not None:
			return render(request,'signup.html',{'show':'username.already.taken'})

		else:
			user=User.objects.create_user(username=username,email=email,password=password)	
			user.save()
			return redirect("/home/")
	return render(request, "signup.html")

def signin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("/home/")
	return render(request,"signin.html")    	

def signout(request):
	logout(request)
	return redirect("/login/")	

def home(request):
	posts = Post.objects.all().order_by('created_date')
	return render(request, 'post_list.html', {'posts': posts})   	

def new_post(request):
	if request.method == "POST":
		user_id = request.user.id
		title = request.POST.get('title')
		text = request.POST.get('text')
		author = request.user
		print(text)
		Post.objects.create(title=title,text=text, author=author)
		return redirect('/')
	
	return render(request, 'new_post.html')

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_details.html', {'post': post}) 

def plan_detail(request, pk):
	plan = get_object_or_404(Plan, pk=pk)
	return render(request, 'plan_detail.html', {'plan': plan}) 	

def plan(request):
	if request.method == "POST":
		place= request.POST.get('place')
		start_date= request.POST.get('start_date')
		end_date= request.POST.get('end_date')
		schedule = request.POST.get('schedule')
		to_do_list= request.POST.get('to_do_list')
		Plan.objects.create(place=place,start_date=start_date,end_date=end_date,schedule=schedule,to_do_list=to_do_list)
		return redirect("/plan_list/")
	return render(request, 'plan.html')
	


def post_list(request):
	post = Post.objects.all().order_by('created_date')
	return render(request, 'post_list.html', {'post': post}) 

def plan_list(request):
	plan = Plan.objects.all()
	return render(request, 'plan_list.html', {'plan': plan}) 	


def add_comment_to_post(request, pk):
	if request.method == "POST":
		post = get_object_or_404(Post, pk=pk)
		text= request.POST.get('text')
		Comment.objects.create(text=text)	
		return redirect('/post_detail/', pk=post.pk)
	return render(request, 'post_details.html', {'post': post})  	  	

def profile(request):
	user = request.user

	name= user.username
	# profile = Profile.objects.get(user=user)

	pro=get_object_or_404(Profile, user=user)
	print(pro)

	if request.method == "POST":

		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		# name = request.POST.get('username')
		# dob = request.POST.get('dob')
		email = request.POST.get('email')
		no = request.POST.get('no')
		
		# pro.username=name
		pro.email=email
		pro.phone_number = no 
		pro.first_name = firstname
		pro.last_name = lastname
		# pro.dob = dob
		pro.save()

		return redirect('/home/')


	return render(request, 'profile.html', {'profile': pro ,"name":name})

# def post_remove(request, pk):
# 	post = get_object_or_404(Post, pk=pk)
# 	post.delete()
# 	return redirect('post_list.html')     
# def profile(request):
# 	if request.method == "POST":
# 		image=request.FILES.get('image')
# 		username = request.POST.get('username',None)
# 		email=request.POST.get("email")
		
# 		image.save()
# 		return HttpResponse("Your profile was successfully updated!")           
# 	return render(request, 'blog/profile.html')	