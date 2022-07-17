from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def signup_view(request):
    if request.method == 'POST': #validate the data submmited by signup form
        form = UserCreationForm(request.POST)  #request.post gets all the data from the signup form
        if form.is_valid():
            user = form.save()  #makes a variable out of newly created account
            login(request, user)    #auto signs in when you make an account
            return redirect('notes:sticky')   #redirects to notes->urls =>> sticky
            
    
    else:   #For GET requests just create empty form
        form = UserCreationForm()
      
    #if you mess up creating an account it renders the form you filled out but doesnt save account bc it failed to create  
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    #POST request when you actually submit the login
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:  #if you want to create but arent logged in, login and then go to create tab
                return redirect(request.POST.get('next'))  
            else:
                return redirect('notes:sticky') #else you are just logging in, go to main page

    #GET request if you go to login url
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('notes:sticky')
