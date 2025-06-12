from common_fun.models import LoginIdCred
import bcrypt

class MongoLoginBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = LoginIdCred.objects.get(login_id=username)
            if bcrypt.checkpw(password.encode(), user.login_password.encode()):
                return user
        except LoginIdCred.DoesNotExist:
            return None
