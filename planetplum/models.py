from django.db import models
from django.conf import settings
from django.utils import timezone
from colorfield.fields import ColorField
from django.db.models.signals import post_save

class Venue(models.Model):
    name = models.CharField(max_length = 30, unique=True)

    ageRange_choices = [('A', 'All Ages'), ('8', '18+'), ('9', '19+'), ('2', '21+')]
    ageRange = models.CharField(max_length=1, choices = ageRange_choices, default='A')

    image = models.ImageField(upload_to="venueimages/", null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name="Information", help_text="Information on the venue or things people should know.")
    dm = models.BooleanField(default=False, verbose_name="Ask a punk for the address", help_text="Check the box if the address isn't public knowledge.")
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        try:
            this = Venue.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super(Venue, self).save(*args, **kwargs)
    
class Label(models.Model):
    name = models.CharField(max_length = 30, unique=True)
    color = ColorField(default='#FFFFFF')
    image = models.ImageField(upload_to="labelimages/", null=True, blank=True)
    description = models.TextField(null=True, blank=True, help_text="A description about the label")
    link = models.URLField(null=True, blank=True, help_text="Does the label have a website or main social media?")
    email = models.EmailField(null=True, blank=True, help_text="email for contacting the label")
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        try:
            this = Label.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super(Label, self).save(*args, **kwargs)
    
class Band(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="bandpfps/")
    description = models.TextField(blank=True, null=True)
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="bands", blank=True)
    associates = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="associated", blank=True)
    approved = models.BooleanField(default=False, null=True, blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        try:
            this = Band.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super(Band, self).save(*args, **kwargs)

class ShowVibe(models.Model):
    name = models.CharField(max_length=30)
    color = ColorField(default='#FFFFFF')

class Show(models.Model):
    approved = models.BooleanField(default=False)
    image = models.ImageField(upload_to="showposters/", verbose_name="Poster")
    name = models.CharField(max_length=45, verbose_name="Title", blank=True, null=True)
    date = models.DateField(default=timezone.now)
    venue = models.ForeignKey(Venue, on_delete=models.RESTRICT)
    price = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    pwyc = models.BooleanField(default=False)
    time = models.TimeField(blank=True, null=True)
    bands = models.ManyToManyField(Band, blank=True, verbose_name="Local Bands Playing:", help_text="(Not Required) choose which local bands are playing this show")
    class Meta:
        ordering = ["-date", "name"]
    def __str__(self):
        return f"{self.name}, {self.date}"
    def save(self, *args, **kwargs):
        try:
            this = Show.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super(Show, self).save(*args, **kwargs)

class Announcement(models.Model):
    image = models.ImageField(upload_to="announcementimgs/", null=True, blank=True)
    name = models.CharField(max_length=150, verbose_name="Title")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.name}"
    def save(self, *args, **kwargs):
        try:
            this = Announcement.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super(Announcement, self).save(*args, **kwargs)

class CommunitySection(models.Model):
    name = models.CharField(max_length=50, verbose_name="Title")

class CommunityLink(models.Model):
    section = models.ForeignKey(CommunitySection, on_delete=models.SET_DEFAULT, default=1)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="community/")
    link = models.URLField()
    description = models.TextField()

class Devlog(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    datetime = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title
