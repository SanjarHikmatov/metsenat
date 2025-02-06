from decimal import Decimal

from django.utils.timezone import now
from apps.sponsors.models import StudentSponsor
from rest_framework.exceptions import ValidationError


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