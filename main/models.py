from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from authors.models import UserProfuile

# Create your models here.
class Blog_category(models.Model):
    name=models.CharField(max_length=250,null=False,default='technology')
    images=models.ImageField(upload_to="Category-images",null=True)

    def __str__(self):
        return self.name

class Blog(models.Model):

    STATUS=(
    ('pending','pending'),
    ('Verified','Verified')
    )

    POPUlAR=(
        ('True','True'),
        ('False',"False")

    )

   

    Blog_category=models.ForeignKey(Blog_category,on_delete=models.CASCADE,null=False,default="1")
    name = models.CharField(max_length=1000)
    blogs_image = models.ImageField(upload_to="blog-image/", blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = RichTextField(null=True)
    time_upload = models.DateTimeField(auto_now_add = True)
    is_verified=models.CharField(max_length=10,choices=STATUS)
    is_popular=models.CharField(max_length=10,choices=POPUlAR)
    mini_description = models.TextField(null=True)
    post_date = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)
    read = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + str(self.post_date))
        return super().save(*args, **kwargs)

class BlogComment(models.Model):
    description = models.TextField(help_text="Write your comment")
    # user= models.ForeignKey(UserProfuile, on_delete=models.CASCADE,blank=False,null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.blog)

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length=250)
    phone_number = models.IntegerField()
    contact_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return str(self.first_name + " " + self.last_name)