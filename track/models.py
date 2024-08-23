from django.db import models
from django.core.exceptions import ValidationError

class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200, blank=True, null=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title

    def save_track(self, *args, **kwargs):
        """Save the track instance and handle additional logic."""
       
        self.save(*args, **kwargs)

    def delete_track(self):
        """Delete the track instance."""
        self.delete()

    @classmethod
    def get_all_tracks(cls):
        """Return all track instances."""
        return cls.objects.all()

    @classmethod
    def get_track_by_id(cls, track_id):
        """Get a track instance by its ID."""
        return cls.objects.get(id=track_id)
