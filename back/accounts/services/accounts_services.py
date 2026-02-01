from django.contrib.auth.models import User

def create_user_service(validated_data) -> User:
    user = User.objects.create_user(
        validated_data['username'],
        validated_data['email'],
        validated_data['password']
    )
    return user