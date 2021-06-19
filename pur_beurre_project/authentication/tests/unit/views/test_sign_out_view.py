from django.test import TestCase

from authentication.tests.unit.models.test_custom_user import CustomUserTest


class SignOutViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        CustomUserTest.emulate_custom_user()
    
    def setUp(self):
        self.user_session = self.client.login(
            email='testuser@email.com',
            password='_Xxxxxxx'
        )
        
    # def test_get_with_redirect(self):
    #     print (self.user_session)