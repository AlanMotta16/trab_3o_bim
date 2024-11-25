from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=100, required=True)
    phone = forms.CharField(label="Telefone", max_length=15, required=False)
    email = forms.EmailField(label="Email", required=True)
    message = forms.CharField(
        label="Mensagem",
        widget=forms.Textarea(attrs={"rows": 4}),
        required=True,
    )