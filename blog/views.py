from django.shortcuts import render,redirect
from blog.models import Posts
from .forms import PostForm
from django.views.generic import View
from django.shortcuts import get_object_or_404



# Create your views here.


class HomePage(View):
	template = "index.html"

	def get(self,request):
		post_lists = Posts.objects.all()

		context = {
			"posts": post_lists
		}

		return render(request, self.template,  context)




class CreatePost(View):

	form = PostForm

	template = "create.html"

	def get(self,request):

			context={
			"form":PostForm

			}
			return render(request, self.template, context)


	def post(self,request):

		form = PostForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect("index")

		return redirect("create")

class Details(View):

	def get(self,request, slug):

		task = get_object_or_404(Posts,slug=slug)

		form = PostForm(instance=task)

		context={

			"post": task,
			"form":form,

		}

		return render(request, 'details.html', context)

		
	def post(self,request,slug):
		task = get_object_or_404(Posts,slug=slug)


		form = PostForm(request.POST,instance = task)
		if form.is_valid():
			form.save()
			return redirect("index")

		context={
			"post": task,
			"form":form,
		}

		return render(request, 'details.html', context)


class Delete(View):

	def post(self,request,slug):
		obj = get_object_or_404(Posts,slug=slug)
		obj.delete()
		#redirect
		return redirect(request,"index.html",{})


class User_Registration(View):

	template = "registration.html"

	def get(self,request):
		if self.user.is_authenticated():
			return render("index")
		






		

