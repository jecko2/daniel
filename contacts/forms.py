from django import forms
from contacts.models import Comment

class PostCommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control w-100",
        "placeholder":"Full Name"
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            "class":"form-control w-100",
            "placeholder":"Email Address"
        }))
    comment = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","rows":3, "placeholder":"your comment here..."}))
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']
        