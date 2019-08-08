from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'proposal', views.ProposalViewSet, 'proposal')
router.register(r'response', views.ResponseViewSet, 'response')
router.register(r'user', views.UserViewSet, 'user')
router.register(r'product', views.ProductViewSet, 'product')
router.register(r'client', views.ClientViewSet, 'client')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]




