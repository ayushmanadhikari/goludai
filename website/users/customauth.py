from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class EmailBackEnd(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
        except ObjectDoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
