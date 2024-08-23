from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    @classmethod
    def get_all_tracks(cls):
        """Returns all Track instances."""
        return cls.objects.all()

    @classmethod
    def get_track_by_id(cls, id):
        """Returns a Track instance by id."""
        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None

    def delete_track(self):
        """Deletes the current Track instance."""
        self.delete()
