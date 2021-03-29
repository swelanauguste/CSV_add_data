from django.db import models
from django.utils.translation import activate



class Upload(models.Model):
    file = models.FileField(upload_to='uploads')
    uploaded = models.DateTimeField(auto_now_add=True)
    is_activated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


