from bucket.models import BucketList, BucketListItem

from django.contrib.auth.models import User
from django.test import TestCase


class BucketListModelTestCase(TestCase):
    """ Tests the BucketList Model """

    def setUp(self):
        user = User.objects.create(
            username="testuser", password="testpassword")
        bucketlist = BucketList.objects.create(name="TestBucket", user=user)
        item = BucketListItem.objects.create(name="TestItem",
                                             bucketlist=bucketlist)

    def test_bucketlist_model(self):
        user = User.objects.get(username="testuser")
        bucketlist = BucketList.objects.get(id=1)
        self.assertEqual(str(bucketlist), 'TestBucket')
        self.assertEqual(bucketlist.id, 1)
        self.assertEqual(bucketlist.user, user)
        self.assertEqual(BucketList.objects.count(), 1)


class BucketListItemModelTestCase(TestCase):
    """ Tests the BucketListItem Model """

    def setUp(self):
        user = User.objects.create(
            username="testuser", password="testpassword")
        bucketlist = BucketList.objects.create(name="TestBucket", user=user)
        item = BucketListItem.objects.create(name="TestItem",
                                             bucketlist=bucketlist)

    def test_bucketlist_item_model(self):
        bucketlist = BucketList.objects.get(id=1)
        item = BucketListItem.objects.get(id=1)
        self.assertEqual(str(item), "TestItem")
        self.assertEqual(item.id, 1)
        self.assertEqual(item.bucketlist, bucketlist)
        self.assertEqual(BucketListItem.objects.count(), 1)
