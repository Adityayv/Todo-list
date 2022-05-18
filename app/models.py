from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    status_choices = [
    ('C', 'Completed'),
    ('P', 'Pending'),
    ]
    status_priority = [
    ('1', '𝟏'),
    ('2', '𝟐'),
    ('3', '𝟑'),
    ('4', '𝟒'),
    ('5', '𝟓'),
    ('6', '𝟔'),
    ('7', '𝟕'),
    ('8', '𝟖'),
    ('9', '𝟗'),
    ('10', '𝟏𝟎'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=status_choices)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=2, choices=status_priority)
