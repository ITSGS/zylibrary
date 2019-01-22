# -*- coding: utf-8 -*-
from book.models import *
from book.serializers import *
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

import logging
log = logging.getLogger()


class CategoryViewSets(viewsets.ModelViewSet):
    """
    图书分类的增删改查
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            log.info('查询图书分类列表成功')
            return Response({'code': status.HTTP_200_OK, 'data': serializer.data},
                            status=status.HTTP_200_OK)

        except Exception as e:
            log.error('查询图书分类列表出错' + str(e))
            return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': ' ' + str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({'code': status.HTTP_200_OK, 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': ' ' + str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({'code': status.HTTP_200_OK, 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': ' ' + str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response({'code': status.HTTP_200_OK, 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': ' ' + str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            ids = request.data['ids']
            id_list = ids.replact('[', ' ').replace(']', ' ').split(',')
            for id in id_list:
                book_queryset = Book.objects.filter(status='RE').count()
                if book_queryset > 0:
                    return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': 'Please clear the category all book'})
                result = Category.objects.filter(id=id).update(status='RE')
            return Response({'code': status.HTTP_200_OK, 'data': result},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'code': status.HTTP_400_BAD_REQUEST, 'msg': ' ' + str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class ShelfViewSets(viewsets.ModelViewSet):
    queryset = Shelf.objects.filter(status='AC').all()
    serializer_class = ShelfSerializer


class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.filter(status='AC').all()
    serializer_class = BookSerializer


class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.filter(status='AC').all()
    serializer_class = UserProfileSerializer


class CheckOutViewSets(viewsets.ModelViewSet):
    queryset = CheckOut.objects.filter(status='AC').all()
    serializer_class = CheckOutSerializer


class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(status='AC').all()
    serializer_class = CommentSerializer


class NoteViewSets(viewsets.ModelViewSet):
    queryset = Note.objects.filter(status='AC').all()
    serializer_class = NoteSerializer


class RentViewSets(viewsets.ModelViewSet):
    queryset = Rent.objects.filter(status='AC').all()
    serializer_class = RentSerializer


class ShiftViewSets(viewsets.ModelViewSet):
    queryset = Shift.objects.filter(status='AC').all()
    serializer_class = ShiftSerializer


class FeedBackViewSets(viewsets.ModelViewSet):
    queryset = FeedBack.objects.filter(status='AC').all()
    serializer_class = FeedBackSerializer
