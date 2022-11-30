from django.shortcuts import render, redirect
from contacts.utils.forms import SubscriptionForm

def subscribe(request):
    if request.method == 'POST':
        if "subscribe" in request.POST:
            print("Yess")
            form = SubscriptionForm(request.POST)
            if form.is_valid():
                form.save()
            
                return redirect("core:home_view")
            print("not valid")
            
