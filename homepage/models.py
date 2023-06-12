from django.db import models
from django.core.validators import EmailValidator
from django.utils.text import slugify
from PIL import Image as PilImage
from django.conf import settings


class ContactRequest(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(validators=[EmailValidator], null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class Page(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class PageContent(models.Model):
    LEFT = 1
    CENTER = 2
    RIGHT = 3

    POSITION_CHOICES = [
        (LEFT, 'Left'),
        (CENTER, 'Center'),
        (RIGHT, 'Right'),
    ]

    text = models.TextField()
    picture = models.ImageField(upload_to='images', blank=True, null=True)
    text_position = models.IntegerField(choices=POSITION_CHOICES)
    order = models.IntegerField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=settings.LANGUAGES, default='tr')

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if self.picture:
            img = PilImage.open(self.picture.path)

            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.picture.path)

        if is_new:
            for language, _ in settings.LANGUAGES:
                if language != 'tr':
                    TranslatedPageContent.objects.create(language=language, page_content=self)

    class Meta:
        ordering = ['order']


class TranslatedPageContent(models.Model):

    language = models.CharField(max_length=2, choices=settings.LANGUAGES)
    translated_text = models.TextField()
    page_content = models.ForeignKey(PageContent, on_delete=models.CASCADE, related_name='translations')

    def __str__(self):
        return f'{self.page_content.text} ({self.language})'

    class Meta:
        unique_together = ['language', 'page_content']



class Image(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = PilImage.open(self.image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)