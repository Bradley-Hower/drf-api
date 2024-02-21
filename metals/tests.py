from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Metal


class MetalTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_metal = Metal.objects.create(
            name="uranium",
            owner=testuser1,
            description="Danger. Danger",
            symbol ="U",

        )
        test_metal.save()

    def test_metals_model(self):
        metal = Metal.objects.get(id=1)
        actual_owner = str(metal.owner)
        actual_name = str(metal.name)
        actual_description = str(metal.description)
        actual_symbol = str(metal.symbol)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "uranium")
        self.assertEqual(
            actual_description, "Danger. Danger"
        )
        self.assertEqual(actual_symbol, "U")
        

    def test_get_metal_list(self):
        url = reverse("metal_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        metals = response.data
        self.assertEqual(len(metals), 1)
        self.assertEqual(metals[0]["name"], "uranium")

    def test_get_metal_by_id(self):
        url = reverse("metal_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        metal = response.data
        self.assertEqual(metal["name"], "uranium")

    def test_create_metal(self):
        url = reverse("metal_list")
        data = {"owner": 1, "name": "gallium", "description": "Like butter.", "symbol": "Ga"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        metals = Metal.objects.all()
        self.assertEqual(len(metals), 2)
        self.assertEqual(Metal.objects.get(id=2).name, "gallium")

    def test_update_metal(self):
        url = reverse("metal_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "uranium",
            "description": "Danger. Danger.",
            "symbol": "U",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        metal = Metal.objects.get(id=1)
        self.assertEqual(metal.name, data["name"])
        self.assertEqual(metal.owner.id, data["owner"])
        self.assertEqual(metal.description, data["description"])
        self.assertEqual(metal.description, data["symbol"])

    def test_delete_metal(self):
        url = reverse("metal_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        metals = Metal.objects.all()
        self.assertEqual(len(metals), 0)

    def test_authentication_required(self):
        self.client.logout()
        url = reverse("metal_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)