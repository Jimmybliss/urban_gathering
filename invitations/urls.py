from django.urls import path
from .views import predict_invitation

urlpatterns = [
   path('predict/', predict_invitation, name='predict_invitation'),
   ]