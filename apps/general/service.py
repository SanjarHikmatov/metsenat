from django.utils.timezone import now

def user_photo_location(user, file):
    today = now()
    return f'users/{user.first_name}/photos/{today.year}/{today.month}/{today.day}/{file}'


