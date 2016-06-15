from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from authentication import views

app_name = 'authentication'

router = DefaultRouter()
router.register(r'register', views.SignUpView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/', obtain_jwt_token),
]
