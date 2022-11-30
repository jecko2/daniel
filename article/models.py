from django.db import models
from django.utils.translation import gettext_lazy as _
from django_editorjs import EditorJsField
from account.models import Profile
from django.urls import reverse
from tags.models import Tag, Topic

class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs)
    
    def top_stories(self):
        return self.filter(category="TOP").all()
        
            

class Post(models.Model):
    
    
    class Category(models.TextChoices):
        
        TOP = "TOP", "Top Stories"
        POPULAR = "POPULAR", "Popular"
        MEDICAL = "MEDICAL", "Medical"
    
    
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="post_tag")
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True, related_name="post_topic")
    title = models.CharField(_("Post Title"), max_length=150)
    category = models.CharField(_("Category"), max_length=20, choices=Category.choices, default=Category.TOP)
    slug = models.SlugField(unique_for_date="pub_date", max_length=150)
    cover = models.ImageField(upload_to="post/", blank=True, null=True)
    body = EditorJsField()
    pub_date = models.DateTimeField(_("Date Published"),auto_now_add=True)
    
    
    objects = PostManager()
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-title', '-pub_date']
        get_latest_by = "-pub_date"
        
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:post_detail", kwargs={
            "slug": self.slug,
            "year":self.pub_date.year,
            "month":self.pub_date.month,
            "day":self.pub_date.day,
            })

