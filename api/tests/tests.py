from django.test import TestCase, Client
from api.models import Camera, Lens, LensMount, Manufacturer
import json

# Camera API tests


class APITests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        with open('api/tests/data/manufacturers.json') as file:
            cls.manufacturer_data = json.load(file)
        with open('api/tests/data/lens_mounts.json') as file:
            cls.lens_mount_data = json.load(file)
        with open('api/tests/data/cameras.json') as file:
            cls.camera_data = json.load(file)
        with open('api/tests/data/lenses.json') as file:
            cls.lens_data = json.load(file)
        client = Client()
        client.post('/manufacturers/', cls.manufacturer_data[0], 'application/json')
        client.post('/lens_mounts/', cls.lens_mount_data[0], 'application/json')
        client.post('/cameras/', cls.camera_data[0], 'application/json')
        client.post('/lenses/', cls.lens_data[0], 'application/json')

    def test_camera_get(self):
        response = self.client.get('/cameras/', HTTP_ACCEPT='application/json')
        json_content = json.loads(response.content)[0]
        # Convert nested objects to ids
        json_content['manufacturer'] = json_content['manufacturer']['id']
        json_content['mount'] = json_content['mount']['id']
        self.assertDictEqual(json_content, self.camera_data[0])

    def test_lens_get(self):
        response = self.client.get('/lenses/', HTTP_ACCEPT='application/json')
        json_content = json.loads(response.content)[0]
        # Convert nested objects to ids
        json_content['manufacturer'] = json_content['manufacturer']['id']
        json_content['mount'] = json_content['mount']['id']
        self.assertDictEqual(json_content, self.lens_data[0])

    def test_lens_compatibility_lookup(self):
        # Check first camera is compatible with first lens
        camera_id = self.camera_data[0]['id']
        response = self.client.get(f'/cameras/{camera_id}/compatible_lenses', HTTP_ACCEPT='application/json')
        json_content = json.loads(response.content)[0]
        self.assertEqual(json_content['id'], self.lens_data[0]['id'])

    def test_camera_compatibility_lookup(self):
        # Check first lens is compatible with first camera
        lens_id = self.lens_data[0]['id']
        response = self.client.get(f'/lenses/{lens_id}/compatible_cameras', HTTP_ACCEPT='application/json')
        json_content = json.loads(response.content)[0]
        self.assertEqual(json_content['id'], self.camera_data[0]['id'])
