from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse




class Topic(models.Model):
    
    title = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    
    
    class TagColor(models.TextChoices):
        BLUE = "BLUE", "blue"
        PRIMARY = "PRIMARY", 'primary'
        RED = 'RED', 'red'
        ORANGE = 'ORANGE', 'orange'
        YELLOW = "YELLOW", 'yellow'
        PURPLE = "PURPLE", 'purple'
        PINK = "PINK", "pink"
        GREN = "GREEN", "green"
        
    name = models.CharField(max_length=100)
    color = models.CharField(_("BACKGROUND COLOR"), max_length=50, choices=TagColor.choices, default=TagColor.PRIMARY)
    bg = models.ImageField(upload_to="tags/", blank=True, null=True)
    
    def __str__(self):
        return self.name.upper()
    
    
            
    def get_post_tag_list_url(self):
        return reverse("core:post_list_per_tag_name_view", kwargs={
            "tag":self.name,
        })


# class Flag(models.Model):
#     tag = models.ForeignKey(Tag, max_length=100)
    

    
    