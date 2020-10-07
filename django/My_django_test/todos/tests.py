from django.test import TestCase
from accounts.models import User
from .models import Todo
# Create your tests here.
class TodoTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        User.objects.create_user(username='testuser', password='password')


    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_todo_index(self):
        response=self.client.get('/todos/')
        print(response)
        self.assertEqual(response.status_code,302)
        self.assertEqual(response.url, '/accounts/login/?next=/todos/')

        # User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        response=self.client.get('/todos/')
        self.assertTemplateUsed(response,'todos/index.html')


    def test_todo_create_get(self):
        self.client.login(username='testuser', password='password')
        response=self.client.get('/todos/create/')
        self.assertTemplateUsed(response,'todos/form.html')
        self.assertEqual(response.status_code,200)

    def test_todo_create_post(self):
        self.client.login(username='testuser', password='password')
        invalid_data={
            # 'content':None,
        }
        response=self.client.post('/todos/create/', invalid_data)
        self.assertEqual(response.status_code, 200)

        valid_data={
            'content': 'test_content',
        }
        response=self.client.post('/todos/create/', valid_data)
        todos=Todo.objects.all()
        self.assertEqual(len(todos),1)
