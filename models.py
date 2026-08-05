from django.db import models

class Task(models.Model):
    title= models.CharField(max_length=200)
    description=models.TextField(blank=True)
    is_completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now=True)
    class Meta:
     ordering=['-created']
    def str(self):
        return self.title
     
        

