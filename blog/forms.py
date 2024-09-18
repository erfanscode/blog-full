# Form for blog
from django import forms
from blog.models import Comment, Post


class CreatePostForm(forms.ModelForm):
    # create post form
    def clean_description(self):
        description = self.cleaned_data['description']
        if description:
            if len(description) > 10:
                raise forms.ValidationError("توضیحات نباید از 10 کلمه بیشتر باشد!")
            else:
                return description

    class Meta:
        model = Post
        fields = ['title', 'description', 'slug']


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