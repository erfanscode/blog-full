# Form for blog
from django import forms
from blog.models import Comment, Post




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


class LoginForm(forms.Form):
    # form for login user
    username = forms.CharField(max_length=120, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
