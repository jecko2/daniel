from django import forms
from contacts.models import Subscription


class SubscriptionForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={ "class":"form-control", "placeholder":"E-Mail Address"}))
    class Meta:
        model = Subscription
        fields = ['email']