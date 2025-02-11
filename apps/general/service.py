from django.utils.timezone import now
from rest_framework.exceptions import ValidationError

from apps.sponsors.models import StudentSponsor

def user_photo_location(user, file):
    """
    It is for user photo location
    """
    today = now()
    return f'users/{user.first_name}/photos/{today.year}/{today.month}/{today.day}/{file}'



def allocate_founds(sponsor, student, amount):
    """
       Allocates the specified amount to the student by processing the sponsor's appeals using FIFO (First In, First Out) method.

       The function goes through the sponsor's appeals in the order they were created, deducting from the oldest appeal until
       the full amount is allocated. If the available appeal amount is less than the required amount, it moves on to the next
       appeal. If there's any remaining amount after processing all the appeals, it raises an error.

       Once the amount is successfully allocated, the student's available balance is increased, and the sponsor's available balance
       is decreased. The allocation is then saved, and a record is created in the StudentSponsor table.

       Parameters:
       sponsor (Sponsor): The sponsor from whom funds are being allocated.
       student (Student): The student who will receive the allocated funds.
       amount (float): The amount to be allocated to the student.

       Raises:
       ValueError: If there is not enough amount in the sponsor's appeals to allocate to the student.
    """

    appeals = sponsor.appeals_sponsor.order_by('created_at')
    cache_amount = amount

    for appeal in appeals:
        if cache_amount <= 0:
            break


        if appeal.amount <= cache_amount and appeal.amount != 0:
            cache_amount -= appeal.amount
            appeal.amount = 0

        elif appeal.amount >= cache_amount:
            appeal.amount -= cache_amount
            cache_amount = 0
        appeal.save()

    student.available += amount
    sponsor.available -= amount

    sponsor.save()
    student.save()

    StudentSponsor.objects.create(sponsor=sponsor, student=student, amount=amount)



def validate_student_sponsor_balance(sponsor, student, amount):


    """
    sponsor va student balance validatsiya qiladi
    """

    sponsor_available = sponsor.available
    student_available = student.available
    student_balance = student.balance

    if amount > sponsor_available:
        raise ValidationError({'sponsor balance': 'This is more than sponsor available balance'})

    if student_balance <= student_available:
        more_money = student_available - student_balance
        if student_balance < student_available:
            raise ValidationError(
                {'sponsor available balance': f'This is more {more_money} than student contract amount of university'}
            )
        raise ValidationError({'student contract': "student has enough money"})

    if student_balance == 0 or student_balance < amount:
        raise ValidationError({'excess money': f'This added amount greater than student contract balance'})

    return True


def validate_user(attrs):
    from apps.users.models import CustomUser

    """
       Custom validation for user role-related fields.
       Ensures that required fields are provided based on the selected user role
       and that unnecessary fields are not included.
    """

    user_role = attrs['role']
    student_university = attrs['university']
    student_degree = attrs['student_degree']
    user_type = attrs['type']
    if user_role == CustomUser.Role.STUDENT:
        # If the user is a student, they cannot have a user type of 'juridic' or 'physical'.
        if user_role == CustomUser.Role.STUDENT and user_type in ['juridic', 'physical']:
            raise ValidationError({'user type': 'you can not add this field.'})

        # If the user is a student, they must provide a university.
        if user_role == CustomUser.Role.STUDENT and not student_university:
            raise ValidationError({'university': 'This field required.'})

        # If the user is a student, their degree cannot be 'empty' and must be either 'bachelor' or 'master'.
        if user_role == CustomUser.Role.STUDENT and student_degree == CustomUser.StudentDegree.EMPTY:
            raise ValidationError({'student degree': 'This field will be bachelor or master.'})


    if user_role == CustomUser.Role.SPONSOR:
        # If the user is a sponsor, they should not have university or student degree fields set.
        if user_role == CustomUser.Role.SPONSOR and student_university:
            raise ValidationError({'university or student degree': 'you can not add university or student degree.'})

        if user_role == CustomUser.Role.SPONSOR and student_degree in ['bachelor', 'master']:
            raise ValidationError({'university or student degree': 'you can not add university or student degree.'})

        # If the user is a sponsor, they must provide a user type.
        if user_role == CustomUser.Role.SPONSOR and not user_type:
            raise ValidationError({'user type': 'This field required.'})
    if user_role == CustomUser.Role.ADMIN:
        # If the user is an admin, they should not have university or student degree fields set.
        if user_role == CustomUser.Role.ADMIN and student_university:
            raise ValidationError({'university or student degree': 'you can not add university or student degree.'})

        if user_role == CustomUser.Role.ADMIN and student_degree in ['bachelor', 'master']:
            raise ValidationError({'user type': 'This field required.'})

        if user_role == CustomUser.Role.ADMIN and user_type in ['juridic', 'physical']:
            raise ValidationError({'user type': 'you can not add this field.'})

    return attrs