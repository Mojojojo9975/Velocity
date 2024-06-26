from django.db import models
from django.urls import reverse

# Manually added imports
from django.utils import timezone
from django.contrib.auth.models import User

#Model Managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
        self).get_queryset().filter(status='published')


# Create your models here.

class Post( models.Model ):

    STATUS_CHOICES=(
        ('draft' , 'Draft'),
        ('published' , 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=150 , unique_for_date='publish')
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10 , choices=STATUS_CHOICES , default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])



    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title




