from django.db import models
import uuid
# Create your models here.

def photo_upload(instance, filename):
    return 'news_{0}/{1}'.format(instance.id, filename)


class News(models.Model):

    title = models.CharField(max_length=60,blank=False)
    text = models.TextField()
    photo = models.ImageField(upload_to=photo_upload,blank=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self) -> str:
        return self.title

    