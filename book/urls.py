from rest_framework import routers
from book.viewsets import *


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'category', CategoryViewSets, base_name='category'),
router.register(r'shelf', ShelfViewSets, base_name='shelf'),
router.register(r'books', BookViewSets, base_name='book'),
router.register(r'checkout', CategoryViewSets, base_name='checkOut'),
router.register(r'comments', CommentViewSets, base_name='comment'),
router.register(r'notes', NoteViewSets, base_name='note'),
router.register(r'rents', RentViewSets, base_name='rent'),
router.register(r'shift', ShiftViewSets, base_name='shift'),
router.register(r'feedback', FeedBackViewSets, base_name='feedback'),
router.register(r'userprofile', UserProfileViewSets, base_name='userprofile'),

urlpatterns = [

]

urlpatterns += router.urls
