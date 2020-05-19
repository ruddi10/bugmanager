from rest_framework_jwt.settings import api_settings


from django.utils import timezone
expire = api_settings.JWT_EXPIRATION_DELTA


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'expire': timezone.now()+expire}
