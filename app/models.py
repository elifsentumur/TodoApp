from django.db import models
from django.utils.text import slugify

Provider= (
    ('Provider 1', 'Provider 1'),
    ('Provider 2', 'Provider 2'),
)
# Create your models here.
class ProviderModel(models.Model):
    name = models.CharField(max_length=60, choices=Provider,null=True, blank=True)
    endpoint = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name

class DeveloperModel(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    task = models.CharField(max_length=60, null=True, blank=True,default='None')
    level = models.CharField(max_length=100,null=True, blank=True,default='None')
    duration = models.CharField(max_length=10,null=True, blank=True,default='None')
    slug = models.SlugField(unique=True,null=True, blank=True,editable=False)

    def get_slug(self):
        slug= slugify(self.name.replace("ı","i"))
        unique =slug
        number = 1

        while DeveloperModel.objects.filter(slug=unique).exists():
            unique = '{}-{}'.format(slug,number)
            number +=1
        return unique

    def save(self,*args,**kwargs):
        self.slug = self.get_slug()
        return super(DeveloperModel,self).save(*args,**kwargs)
   
    def __str__(self):
        return self.name
    
class TaskModel(models.Model):
    provider = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=60, null=True, blank=True)
    level = models.CharField(max_length=100,null=True, blank=True,default='None')
    duration = models.CharField(max_length=10,null=True, blank=True,default='None')
    
    def __str__(self):
        return self.name
    