from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, get_object_or_404
import time


# Create your views here.
def main(request):
    return render(request,'main.html')



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def Login_page(request):
    if request.method == "POST":
            data = request.POST 
            username = data.get('username')
            password = data.get('password')
            if not User.objects.filter(username = username).exists():
                messages.error(request,'Invalid Username')
                return redirect('/Login/')
            else:
                user = authenticate(username = username, password = password)
                if user is None:
                    print(user)
                    messages.error(request,'Invalid Password')
                    return redirect('/Login/')
                else:
                    login(request,user)
                    return redirect('/main/')
    
    
    return render(request,'Login.html')
                 

     

def Reg(request):
    if request.method == "POST":
            data = request.POST 
        
            username = data.get('username')
            email = data.get('email')
            password = data.get('user_pass')

            user = User.objects.filter(username = username)

            if user.exists():
                messages.info(request,'Username already Taken')
                
                return redirect('/register/')

            user = User.objects.create(
            
            username = username,
            email = email,
            password = password
            )

            user.set_password(password)
            user.save()
            messages.info(request,'Account created successfully')
            return redirect('/Login/')
       
    return render(request,'Reg.html')

       
@login_required
def addrecipe(request):
    
    recipe_user_name = request.user.username
    login_user = Recipe.objects.filter(recipe_user_name=recipe_user_name)


    if request.method == "POST":
        data = request.POST 
        recipe_image = request.FILES.get('receipe_image')
        recipe_name = data.get('receipe_name')
        recipe_type = data.get('type')
        recipe_user_name = recipe_user_name
        recipe_description = data.get('receipe_description')
        recipe_detail_description = data.get('recipe_detail_description')
        print(recipe_detail_description)
    
        Recipe.objects.create(
            recipe_user_name = recipe_user_name,
            recipe_type = recipe_type,
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_detail_description = recipe_detail_description,
            recipe_image = recipe_image
        )

        return redirect("/addrecipe/")

    queryset = Recipe.objects.all()
    context = {'recipe':queryset,
            'user_data': login_user
             }
    
    

    return render(request, 'addrecipe.html',context)

def delete(request,pk):
    ask = "Do you want to Delete this recipe"
    if request.method == "POST":
        ask
    
        
        recipe = get_object_or_404(Recipe,pk=pk)
        

        recipe.delete()
        
        return redirect('/addrecipe/')    
        
    return render(request,"addrecipe.html")

def main(request):
    data = Recipe.objects.all()
    
    if request.method == "GET":
        Search = request.GET.get('Search')
        
        if Search!=None:
            
            data = Recipe.objects.filter(recipe_name__icontains=Search)#__icontains can work with similar like data matches the database
    
        

    context = {'Recipes': data,
               'Recipe_count': data.count(),
                'Search_name': Search }
    
    
    return render(request,"main.html",context)


def tandc(request):
    return render(request,"tandc.html")


def contact(request):
    return render(request,"contact.html")
# @login_required
def Logout_page(request):
    logout(request)
    return redirect('/Login/')

def about(request):

    return render(request,"about.html")

def about1(request):

    return render(request,"about1.html")

    

@login_required
def Recipe_detail(request,pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
