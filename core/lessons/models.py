from django.db import models
from requests_courses.models import RequestCourses
from courses.models import Courses

class User:
    
    full_name = models.CharField(
        max_length = 255,
        null = False,
    )

    request_courses = models.ForeignKey(
        models = RequestCourses,
        null = False,
    )

    course = models.ForeignKey(
        models = Courses,
        null = True
    )