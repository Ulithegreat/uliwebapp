from django.db import models

#title of the todo
#description of the todo
#status of the todo
# Create your models here.
#when a new model is created makemigrations of model
#then apply changes to database

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title