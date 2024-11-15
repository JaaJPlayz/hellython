from django.test import TestCase
from api.models import User


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="test", email="test", password="test")

    def test_user(self):
        user = User.objects.get(name="test")
        self.assertEqual(user.name, "test")
        self.assertEqual(user.email, "test")
        self.assertEqual(user.password, "test")
        self.assertEqual(user.__str__(), "test")

        user.name = "test2"
        user.save()
        self.assertEqual(user.name, "test2")

        user.delete()
        self.assertEqual(User.objects.count(), 0)
