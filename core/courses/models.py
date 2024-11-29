from django.db import models
from users.models import User

class Courses:

    course_name = models.CharField(
        max_length=255,
        null=False,
    )

    course_speacker = models.ForeignKey(
        models = User,
        null = False,
    )

    course_price = models.FloatField(
    )