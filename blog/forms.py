# Form for blog
from django import forms


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
