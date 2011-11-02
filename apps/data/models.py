from django.db import models

from apps.data.managers import EntryManager

class Entry(models.Model):
    
    def __unicode__(self):
        return u"%s - %s" % (self.title, self.created)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=64)
    text = models.TextField()
    published = models.BooleanField(db_index=True, default=True)

    objects = EntryManager()
