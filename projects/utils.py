from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def validate_user(token):
    jwt_object = JWTAuthentication()
    #raw_token = jwt_object.get_raw_token(token)
    validated_token = jwt_object.get_validated_token(token)
    user = jwt_object.get_user(validated_token)
    return user


def refresh_validate(token):
    newtoken = RefreshToken(token)
    return str(newtoken.access_token)
