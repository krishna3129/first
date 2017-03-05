from django.db import models

# Create your models here.

class Life(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')
    order= models.IntegerField(default = 0)
    life = models.ForeignKey(Life)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.title
