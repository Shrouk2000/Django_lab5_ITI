# myapp/models.py
from django.db import models

class Trainee(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()  
    progress = models.TextField()  

    def __str__(self):
        return self.name

    @classmethod
    def get_all_trainees(cls):
        """Returns all Trainee instances."""
        return cls.objects.all()

    @classmethod
    def get_trainee_by_id(cls, id):
        """Returns a Trainee instance by id."""
        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None
