from django.test import TestCase
from .models import User

# Create your tests here.
class AccountTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        User.objects.create_user(username='testuser', password='password')
        user=User.objects.get(pk=1)

    def tearDown(self):
        # Clean up run after every test method.
        pass

    # def test_something_that_will_pass(self):
    #     self.assertFalse(False)

    # def test_something_that_will_fail(self):
    #     self.assertTrue(True)

    # def test_my_first_test(self):
    #     self.assertEqual()
    def test_user_model_create(self):
        user=User.objects.get(pk=1)
        self.assertEqual(user.username, 'testuser')


    def test_user_str_method(self):
        user=User.objects.get(pk=1)
        self.assertEqual(str(user), 'User Object(1)')
    

    def test_user_phone_field_max_length(self):
        user=User.objects.get(pk=1)
        max_length=user._meta.get_field('phone').max_length
        self.assertEqual(max_length, 11)

    
    def test_base_template(self):
        response = self.client.get('/accounts/')
        self.assertContains(response,'<a href="">login</a>')
        self.assertNotContains(response,'<a href="">logout</a>')
        
        self.client.login(username='testuser', password='password')
        response = self.client.get('/accounts/')
        self.assertContains(response,'<a href="">logout</a>')
        self.assertNotContains(response,'<a href="">login</a>')