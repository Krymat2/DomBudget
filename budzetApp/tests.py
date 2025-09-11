"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase, Client
from django.urls import reverse

from budzetApp.models import Budzety, Uzytkownicy, Kategorie, Transakcje

# TODO: Configure your database in settings.py and sync before running tests.

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase, Client
from django.urls import reverse

from budzetApp.models import Budzety, Uzytkownicy, Kategorie, Transakcje

# TODO: Configure your database in settings.py and sync before running tests.

class UserRegistrationTest(TestCase):
    def test_register_user(self):
        response = self.client.post(reverse('budzetApp:register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'confirm_password': 'testpass123',
        })
        self.assertEqual(response.status_code, 302)  # przekierowanie po sukcesie
        self.assertTrue(Uzytkownicy.objects.filter(username='testuser').exists())

class UserLoginTest(TestCase):
    def setUp(self):
        self.user = Uzytkownicy.objects.create(username='testuser', email='test@example.com', password='testpass123')

    def test_login_user(self):
        response = self.client.post(reverse('budzetApp:login'), {
            'username': 'testuser',
            'password': 'testpass123',
        })
        #self.assertEqual(response.status_code, 302)  # przekierowanie po sukcesie

class BudgetTest(TestCase):
    def setUp(self):
        self.user = Uzytkownicy.objects.create(username='testuser', email='test@example.com', password='testpass123')
        self.client = Client()
        session = self.client.session
        session['user_id'] = self.user.id
        session.save()

    def test_create_budget(self):
        response = self.client.post(reverse('budzetApp:create_budget'), {
            'name': 'Budżet testowy',
            'budget_amount': 1000,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Budzety.objects.filter(name='Budżet testowy').exists())

    def test_budget_list_view(self):
        Budzety.objects.create(name='Budżet testowy', budget_amount=1000)
        response = self.client.get(reverse('budzetApp:budget_list'))
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, "Budżet testowy")

class TransactionTest(TestCase):
    def setUp(self):
        self.user = Uzytkownicy.objects.create(username='testuser', email='test@example.com', password='testpass123')
        self.budget = Budzety.objects.create(name='Budżet testowy', budget_amount=1000)
        self.category = Kategorie.objects.create(category_name='Zakupy', budget=self.budget)
        self.client = Client()
        session = self.client.session
        session['user_id'] = self.user.id
        session.save()

    def test_add_transaction(self):
        response = self.client.post(reverse('budzetApp:addtransaction'), {
            'budget': self.budget.id,
            'category': self.category.id,
            'amount': 200,
            'description': 'Testowa transakcja'
        })
        self.assertEqual(response.status_code, 200)
        #self.assertTrue(Transakcje.objects.filter(description='Testowa transakcja').exists())

    def test_transaction_list_view(self):
        Transakcje.objects.create(
            budget=self.budget,
            category=self.category,
            amount=100,
            description='Test',
            user=self.user
        )
        response = self.client.get(reverse('budzetApp:index'))
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, "Test")


# class UserRegistrationInvalidTest(TestCase):
#     def test_register_with_password_mismatch(self):
#         response = self.client.post(reverse('budzetApp:register'), {
#             'username': 'testuser',
#             'email': 'test@example.com',
#             'password1': 'testpass123',
#             'password2': 'differentpass123',
#         })
#         self.assertEqual(response.status_code, 200)  # Re-rendered with errors
#         self.assertFormError(response, 'form', 'password2', "Hasła się nie zgadzają.")
#         self.assertFalse(Uzytkownicy.objects.filter(username='testuser').exists())

class UserLoginInvalidTest(TestCase):
    def setUp(self):
        self.user = Uzytkownicy.objects.create(username='testuser', password='correctpassword')

    def test_login_with_wrong_password(self):
        response = self.client.post(reverse('budzetApp:login'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)  # Błąd, więc brak przekierowania
        #self.assertContains(response, "Proszę podać poprawną nazwę użytkownika i hasło.")



# class PasswordChangeInvalidTest(TestCase):
#     def setUp(self):
#         self.user = Uzytkownicy.objects.create(username='testuser', password='correctpass')
#         self.client.login(username='testuser', password='correctpass')

#     def test_wrong_old_password(self):
#         response = self.client.post(reverse('budzetApp:change_password'), {
#             'old_password': 'wrongoldpass',
#             'new_password1': 'newpass123',
#             'new_password2': 'newpass123',
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertFormError(response, 'form', 'old_password', "Twoje stare hasło jest nieprawidłowe.")




