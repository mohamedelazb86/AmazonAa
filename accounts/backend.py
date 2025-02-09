from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class Login_Username_Email(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user=User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user=user=User.objects.get(username=username)
            except User.DoesNotExist:
                return None
            
        if user.check_password(password):
            return user
        return None