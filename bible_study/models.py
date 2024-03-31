from django.db import models
from django.contrib.auth.models import User


class BibleStudy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="studies")
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Scripture(models.Model):
    study = models.ForeignKey(
        BibleStudy, related_name="scriptures", on_delete=models.CASCADE
    )
    verse = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.verse[:50]  # Show the first 50 characters


class Note(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    study = models.ForeignKey(
        BibleStudy,
        related_name="notes",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    scripture = models.ForeignKey(
        Scripture, related_name="notes", null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.content[:50]  # Show the first 50 characters
