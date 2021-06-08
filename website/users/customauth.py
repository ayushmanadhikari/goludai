from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist



class EmailBackEnd(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except ObjectDoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
