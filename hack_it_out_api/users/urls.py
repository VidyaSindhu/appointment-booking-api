from django.urls import path
from django.urls.conf import include
from .views import ChangePasswordView, GetUsersDetail, RegisterUser, GetUsersList, check_user_existence
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import ObtainJSONWebToken, VerifyJSONWebToken

urlpatterns = [
    path('login/', ObtainJSONWebToken.as_view()),
    path('verify/', VerifyJSONWebToken.as_view()),
    path('register/', RegisterUser.as_view()),
    path('', GetUsersList.as_view()),
    path('<int:pk>/', GetUsersDetail.as_view()), #GET, PUT
    path('exists/', check_user_existence),
    path('changepassword/<int:pk>/', ChangePasswordView.as_view()), #PUT


]