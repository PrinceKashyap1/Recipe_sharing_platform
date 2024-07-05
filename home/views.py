from django.shortcuts import render

from django.http import HttpResponse
# from django.contrib import authenticate,login,logout
# Create your views here.

def home(request):
    # to make a dictationary to store key value pair in list function
    peoples = [
    {'name': 'Abhijeet Gupta','age':26},
    {'name': 'Rohan Sharma','age':23},
    {'name': 'Vicky Kaushal Gupta','age':17},
    {'name': 'Deepanshu Chaurashiya','age':16},
    {'name': 'Sandeep pal','age':25},
    ]

    
    text=""" Lorem ipsum, dolor sit amet consectetur adipisicing elit. Non cumque enim natus provident ullam ducimus amet eos? 
    Quidem corporis provident aspernatur similique ad eveniet eum, ullam quas, voluptatibus harum vero.
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Non cumque enim natus provident ullam ducimus amet eos? 
    Quidem corporis provident aspernatur similique ad eveniet eum, ullam quas, voluptatibus harum vero.
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Non cumque enim natus provident ullam ducimus amet eos? 
    Quidem corporis provident aspernatur similique ad eveniet eum, ullam quas, voluptatibus harum vero.
"""
    
    vegetables =['Pumpkin','Tomato', 'Potato']
    return render(request, "index.html",context={
        'page': "main",
        'peoples' : peoples,
        'text':text,
        'vegetables':vegetables
        })

def about(request):
    return render(request,"about.html",context={'page': "about"})


def contact(request):
    context= {'page': "contact"}
    return render(request,"contact.html",context)
def Success_page(request):
    print("*" * 10)
    return HttpResponse("This is a Success Page.")


