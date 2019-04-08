from django import forms

from contact.models import Contact


class ContactForm(forms.Form):
  fullname = forms.CharField(
   widget=forms.TextInput(
      attrs={
        "class": "stext-111 cl2 plh3 size-116 p-l-62 p-r-30",
        "placeholder": "Your Full Name",
      }
    )
  )
  email = forms.EmailField(
    widget=forms.EmailInput(
      attrs={
        "class": "stext-111 cl2 plh3 size-116 p-l-62 p-r-30",
        "placeholder": "Your Email Address"
      }
    )
  )
  content = forms.CharField(
    widget=forms.Textarea(
      attrs={
        "class": "stext-111 cl2 plh3 size-120 p-lr-28 p-tb-25",
        "placeholder": "How Can We Help?"
      }
    )
  )

  