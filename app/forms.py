from django import forms

from .models import Contact, ProviderOrganization


class EmailForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "name@example.com",
            }
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class ProviderOrganizationForm(forms.ModelForm):
    class Meta:
        model = ProviderOrganization
        fields = "__all__"
