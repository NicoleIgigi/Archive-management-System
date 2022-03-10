from django.db import models

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Doc(models.Model):
    title = models.CharField(max_length=150)
    Categories = models.ForeignKey(Categories, related_name= 'documents', on_delete=models.CASCADE)
    cover = models.FilePathField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    private = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title