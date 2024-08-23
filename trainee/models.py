from django.db import models
from django.core.exceptions import ValidationError

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    enrolled_date = models.DateField()

    def __str__(self):
        return self.name

    def save_trainee(self, *args, **kwargs):
        """Save the trainee instance."""
       
        self.save(*args, **kwargs)

    def delete_trainee(self):
        """Delete the trainee instance."""
        self.delete()

    @classmethod
    def get_all_trainees(cls):
        """Return all trainee instances."""
        return cls.objects.all()

    @classmethod
    def get_trainee_by_id(cls, trainee_id):
        """Get a trainee instance by its ID."""
        return cls.objects.get(id=trainee_id)
