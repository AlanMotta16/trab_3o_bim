from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .forms import ContactForm
from .models import Contact

class ContactViewTests(TestCase):
    def test_get_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/form.html')

    def test_post_valid_data(self):
        response = self.client.post(reverse('contact'), {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Test message',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/success.html')
    
    def test_post_invalid_data(self):
        response = self.client.post(reverse('contact'), {})  # Sem dados
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Este campo é obrigatório.')
        self.assertFormError(response.context['form'], 'name', 'Este campo é obrigatório.')

    # def test_post_invalid_data(self):
    #     response = self.client.post(reverse('contact'), {
    #         'name': '',
    #         'email': 'invalid-email',
    #         'message': '',
    #     })
    #     self.assertEqual(response.status_code, 200)
    #     self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')

class ContactFormTests(TestCase):
    def test_valid_form(self):
        form = ContactForm(data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Test message',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())

class ContactModelTest(TestCase):
    def test_create_contact(self):
        contato = Contact.objects.create(
            nome="Test User",
            email="test@example.com",
            mensagem="Mensagem de teste",
        )
        self.assertEqual(contato.respondido, False)

class AdminTest(TestCase):
    def setUp(self):
        # Criação de um superusuário para o login no admin
        self.user = get_user_model().objects.create_superuser('admin', 'admin@example.com', 'password')

    def test_admin_contact_list(self):
        # Fazendo login como admin
        self.client.login(username='admin', password='password')

        # Acessando a lista de contatos no admin
        response = self.client.get(reverse('admin:contact_contact_changelist'))

        # Verificando se a resposta foi 200 (sucesso)
        self.assertEqual(response.status_code, 200)