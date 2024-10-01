# Form for blog
from django import forms
from django.core.exceptions import ValidationError

from blog.models import Comment, Post, User




class TicketForm(forms.Form):
    # form for ticket
    CHOICES_SUBJECT = (
        ('پیشنهاد', 'پیشنهاد'),
        ('انتقاد', 'انتقاد'),
        ('گزارش', 'گزارش')
    )
    message = forms.CharField(widget=forms.Textarea, required=True)
    name = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=11, required=True)
    subject = forms.ChoiceField(choices=CHOICES_SUBJECT, required=True)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if not phone.isnumeric():
                raise forms.ValidationError('شماره تلفن باید عدد باشد')
            else:
                return phone


class CommentForm(forms.ModelForm):
    # form for post comments
    class Meta:
        model = Comment
        fields = ('name', 'body')


class SearchForm(forms.Form):
    # form for search posts
    query = forms.CharField()


class CreatePostForm(forms.ModelForm):
    # form for create post
    image = forms.ImageField(label="تصویر")
    class Meta:
        model = Post
        fields = {'title', 'description', 'reading_time'}


class UserRegistrationForm(forms.ModelForm):
    # form for registration user
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('رمز عبور ها یکی نیستند!')
        return cd['password2']

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
