from django.db import models

# Describes a Place table in the database, with a name column, and a visited column.

class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} visited? {self.visited}'
    
    