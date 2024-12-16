from django.shortcuts import render
# from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Obtém os dados do formulário
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone'] or 'Não informado'
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Monta o corpo do e-mail com todos os dados
            email_body = f"""
            Novo contato recebido:

            Nome: {name}
            Telefone: {phone or 'Não informado'}
            Email: {email}
            
            Mensagem:
            {message}
            """

            # Configura o e-mail
            email_message = EmailMessage(
                subject=f"Novo contato de {name}",
                body=email_body,
                from_email='contato@eventif.com.br',
                # from_email=email,
                to=['contato@eventif.com.br'],
                cc=[email],  # Adiciona o remetente em CC
                reply_to=[email]
            )

            #Envia o e-mail
            email_message.send()

            #Retorna a página de sucesso
            return render(request, 'contact/success.html', {
                'name': name,
                'phone': phone,
                'email': email,
                'message': message,
                })
        # if form.is_valid():
        #     name = form.cleaned_data['name']
        #     phone = form.cleaned_data['phone']
        #     email = form.cleaned_data['email']
        #     message = form.cleaned_data['message']

        #     # Enviar o e-mail
        #     subject = "Novo contato recebido"
        #     email_message = f"""
        #     Nome: {name}
        #     Telefone: {phone or 'Não informado'}
        #     Email: {email}
        #     Mensagem: {message}
        #     """
        #     send_mail(
        #         subject,
        #         email_message,
        #         email,
        #         ['contato@eventif.com.br'],
        #         fail_silently=False,
        #         cc=[email]
        #     )
        #     return render(request, 'contact/success.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact/form.html', {'form': form})
