from django.db import models

# Create your models here.

class Bookmarks(models.Model):
    alias = models.CharField(max_length=100)
    destination = models.CharField(max_length=300)
    mod_date = models.DateTimeField('date modified') #can be used for display purposes
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.alias + " (" + str(self.is_deleted) + ") : " + self.destination
    
