from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
class UserAPITest(APITestCase):

    def test_create_user(self):
        data = {
            "name": "Amit",
            "email": "amit@test.com",
            "age": 25
        }

        response = self.client.post(
            "/v1/users",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            User.objects.filter(email="amit@test.com").exists()
        )