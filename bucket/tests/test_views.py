"""Import test tools from rest_framework."""
from rest_framework.test import APITestCase


class BucketListViewTestCase(APITestCase):
    """Test for actions on bucketlists."""

    def setUp(self):
        """Setup."""
        self.client.post('/api/auth/register/',
                         {
                             'username': 'jack',
                             'email': 'jack@gmail.com',
                             'password': 'passw',
                         },
                         format='json')

        response = self.client.post('/api/auth/login/',
                                    {
                                        'username': 'jack@gmail.com',
                                        'password': 'passw',
                                    },
                                    format='json')

        token = response.data["token"]

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def test_bucketlist_creation(self):
        """Test that user can create a bucketlist."""
        creation_response = self.client.post('/api/bucketlists/',
                                             {
                                                 'name': 'Travel',
                                             },
                                             format='json')

        self.assertEqual(creation_response.status_code, 201)

    def test_all_bucketlists_querying(self):
        """Test that a user can query all bucketlists."""
        creation_response = self.client.post('/api/bucketlists/',
                                             {
                                                 'name': 'Travel',
                                             },
                                             format='json')

        bucketlists = self.client.get('/api/bucketlists/', format='json')

        self.assertEqual(bucketlists.status_code, 200)
        self.assertEqual("Travel",
                         bucketlists.data[0]['name'])

    def test_bucketlists_querying_by_id(self):
        """Test that a user can query one bucketlist by id."""
        creation_response = self.client.post('/api/bucketlists/',
                                             {
                                                 'name': 'Travel',
                                             },
                                             format='json')

        bucketlist = self.client.get('/api/bucketlists/1/', format='json')

        self.assertEqual(bucketlist.status_code, 200)
        self.assertEqual("Travel", bucketlist.data['name'])

        non_existent_bucketlist = self.client.get(
            '/api/bucketlists/10/', format='json')
        self.assertEqual(non_existent_bucketlist.status_code, 404)

    def test_bucketlist_updating(self):
        """Test that a user can update a bucketlist."""
        creation_response = self.client.post('/api/bucketlists/',
                                             {
                                                 'name': 'Travel',
                                             },
                                             format='json')

        update_response = self.client.put('/api/bucketlists/1/',
                                          {
                                              'name': 'Skii',
                                          },
                                          format='json')

        self.assertEqual(update_response.status_code, 200)
        self.assertEqual("Skii",
                         update_response.data['name'])

    def test_bucketlist_deleting(self):
        """Test that a user can delete a bucketlist."""
        creation_response = self.client.post('/api/bucketlists/',
                                             {
                                                 'name': 'Travel',
                                             },
                                             format='json')

        delete_response = self.client.delete('/api/bucketlists/1/')

        self.assertEqual(delete_response.status_code, 200)


class BucketListItemViewTestCase(APITestCase):
    """Tests for actions on bucketlist items."""

    def setUp(self):
        """Setup."""

        self.client.post('/api/auth/register/',
                         {
                             'username': 'jack',
                             'email': 'jack@gmail.com',
                             'password': 'passw',
                         },
                         format='json')

        response = self.client.post('/api/auth/login/',
                                    {
                                        'username': 'jack@gmail.com',
                                        'password': 'passw',
                                    },
                                    format='json')

        token = response.data["token"]

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        creation_response = self.client.post('/api/bucketlists/',
                                             {
                                                 'name': 'Travel',
                                             },
                                             format='json')

    def test_creating_bucketlist_item(self):
        """Test creation of a bucketlist item."""
        item_creation_response = self.client.post('/api/bucketlists/1/items/',
                                                  {
                                                      'name': 'Beach Tour',
                                                  },
                                                  format='json')

        self.assertEqual(item_creation_response.status_code, 201)
        self.assertEqual("Beach Tour", item_creation_response.data['name'])
        self.assertEqual(False, item_creation_response.data['done'])

    def test_updating_bucketlist_item(self):
        """Test updating of a bucketlist item."""
        item_creation_response = self.client.post('/api/bucketlists/1/items/',
                                                  {
                                                      'name': 'Beach Tour',
                                                  },
                                                  format='json')

        item_updating_response = self.client.put('/api/bucketlists/1/items/1/',
                                                 {
                                                     'name': 'Great Wall of China',
                                                 },
                                                 format='json')

        self.assertEqual(item_updating_response.status_code, 200)
        self.assertIn("Great Wall of China",
                      item_updating_response.data['name'])

    def test_deleting_bucketlist_item(self):
        """Test updating of a bucketlist item."""
        item_creation_response = self.client.post('/api/bucketlists/1/items/',
                                                  {
                                                      'name': 'Beach Tour',
                                                  },
                                                  format='json')

        item_deletion_response = self.client.delete(
            '/api/bucketlists/1/items/1/')

        self.assertEqual(item_deletion_response.status_code, 200)
