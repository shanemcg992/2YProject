from django.shortcuts import render
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Group

# Create your views here.
def signupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = CustomUser.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})