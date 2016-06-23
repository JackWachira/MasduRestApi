from bucket.serializers import BucketlistSerializer, BucketlistItemSerializer
from bucket.models import BucketList, BucketListItem
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from django.db import IntegrityError
from rest_framework import status
from bucket.permissions import IsOwner
from functools import wraps


def bucket_exists(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        pk = kwargs.get('pk', "")
        try:
            BucketList.objects.get(pk=pk)
            return f(*args, **kwargs)
        except BucketList.DoesNotExist:
            return Response({'error': 'The bucketlist does not exist'}, 404)
    return decorated


def item_exists(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        bucketlists_pk = kwargs.get('bucketlists_pk', "")
        pk = kwargs.get('pk', "")
        try:
            BucketList.objects.get(pk=bucketlists_pk)
        except BucketList.DoesNotExist:
            return Response({'error': 'The bucketlist does not exist'}, 404)
        try:
            bucketlist_item = BucketListItem.objects.get(pk=pk)
            return f(*args, **kwargs)
        except BucketListItem.DoesNotExist:
            return Response({'error': 'The bucketlist item does not exist'}, 404)
    return decorated


class BucketListView(viewsets.ModelViewSet):
    """
    Bucketlist View
    """
    queryset = BucketList.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def create(self, request):
        serializer = BucketlistSerializer(data=request.data)
        if serializer.is_valid():
            name = self.request.data['name']
            user = self.request.user
            try:
                BucketList.objects.create(
                    name=name, user=user)
                return Response({'message': 'BucketList created successfully'}, 201)
            except IntegrityError as e:
                return Response({'error': e.message}, 400)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        owner = request.user
        bucketlists = BucketList.objects.all().filter(user=owner)
        serializer = self.get_serializer(bucketlists, many=True)
        return Response(serializer.data)

    @bucket_exists
    def destroy(self, request, pk=None):
        bucketlist = BucketList.objects.get(pk=pk).delete()
        return Response({'Message': 'Bucketlist deleted successfully'}, 200)

    @bucket_exists
    def update(self, request, pk=None):
        serializer = BucketlistSerializer(
            BucketList.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 200)
        return Response(serializer.errors, 400)


class BucketListItemView(viewsets.ModelViewSet):
    """
    Bucketlistitem View
    """

    queryset = BucketListItem.objects.all()
    serializer_class = BucketlistItemSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def create(self, request, pk=None, bucketlists_pk=None):
        serializer = BucketlistItemSerializer(data=request.data)
        if serializer.is_valid():
            name = self.request.data['name']
            parent_bucket = BucketList(pk=bucketlists_pk)
            try:
                bucket_list_item = BucketListItem.objects.create(
                    name=name, done=False, bucketlist=parent_bucket)
                serializer = self.get_serializer(bucket_list_item)
                return Response(serializer.data, 201)
            except IntegrityError as e:
                return Response({'error': e.message}, 400)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @item_exists
    def update(self, request, pk=None, bucketlists_pk=None):
        serializer = BucketlistItemSerializer(
            BucketListItem.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 200)
        return Response(serializer.errors, 400)

    @item_exists
    def destroy(self, request, pk=None, bucketlists_pk=None):
        BucketListItem.objects.get(pk=pk).delete()
        return Response({'Message': 'Bucketlist item deleted successfully'}, 200)
