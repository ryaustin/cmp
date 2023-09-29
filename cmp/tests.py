from django.contrib.auth import get_user_model
from django.test import TestCase

from cmp.views import original_unit, belongsTo

class TestOriginalUnit(TestCase):

    def test_original_unit_with_input_0(self):
        # Define the input
        input_value = 0

        # Define the expected output
        expected_output = "No Match Found"

        # Call the original_unit function with the input
        result = original_unit(None, input_value)

        # Use assert to check if the result matches the expected output
        self.assertContains(result, expected_output)

    def test_original_unit_with_input_2(self):
        # Define the input
        input_value = 2

        # Define the expected output
        expected_output = "Royal Army Service Corps (Block 1)"

        # Call the original_unit function with the input
        result = original_unit(None, input_value)

        # Use assert to check if the result matches the expected output
        self.assertContains(result, expected_output)

    def test_original_unit_with_input_1(self):
        # Define the input
        input_value = 1

        # Define the expected output
        expected_output = "Royal Army Service Corps (Block 1)"

        # Call the original_unit function with the input
        result = original_unit(None, input_value)

        # Use assert to check if the result matches the expected output
        self.assertContains(result, expected_output)


    def test_original_unit_with_input_22199408(self):
        # Define the input
        input_value = 22199408

        # Define the expected output
        expected_output = "Until October 1950"

        # Call the original_unit function with the input
        result = original_unit(None, input_value)

        # Use assert to check if the result matches the expected output
        self.assertContains(result, expected_output)


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="super@user.com", password="foo"
        )
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False
            )
