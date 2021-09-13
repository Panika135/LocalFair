from django.urls import path, include
from django.conf.urls import url    # аналог path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'dich', DichViewSet)
router.register(r'dich2', Dich2ViewSet)


urlpatterns = [
    url('', include(router.urls)),  # отплавяет искать в router, основание является router.register
    path('qwe/', dich_list),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # позволяет логинится в
                                                                                    # предсталении rest
    path('products/', ProductsViewSet.as_view({'get': 'list'})),
    path('products2', ProductViewSet2.as_view()),
]