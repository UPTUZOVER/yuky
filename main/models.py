from django.db import models
from django.db import models

class File(models.Model):
    name = models.FileField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'files'
        ordering = ['created_at']

    def __str__(self):
        return str(self.name)
