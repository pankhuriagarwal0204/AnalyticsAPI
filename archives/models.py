from __future__ import unicode_literals
import uuid as uuid
from django.db import models
from django.template.defaultfilters import slugify


class Geospace(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = 'geospaces'

    def __str__(self):
        return str(self.latitude) + ',' + str(self.longitude)


class Battalion(models.Model):
    name = models.CharField(max_length=250, verbose_name='Name of Battalion')
    geospace = models.OneToOneField('Geospace', on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    slug = models.SlugField(null=True, editable=False)

    class Meta:
        db_table = 'battalions'

    def __str__(self):
        return self.name

    def save(self, *args):
        self.slug = slugify(self.name)
        super(Battalion, self).save(*args)


class Post(models.Model):
    name = models.CharField(max_length=250, verbose_name='name of post')
    geospace = models.OneToOneField('Geospace', on_delete=models.CASCADE)
    battalion = models.ForeignKey('Battalion', related_name='posts', on_delete=models.CASCADE, null=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    slug = models.SlugField(null=True, editable=False)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.name

    def save(self, *args):
        self.slug = slugify(self.name)
        super(Post, self).save(*args)


class Morcha(models.Model):
    name = models.CharField(max_length=250, verbose_name='name of morcha')
    geospace = models.OneToOneField('Geospace', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='morchas', on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    qrt_id = models.OneToOneField('Device', related_name='qrt', null=True)
    units = models.ManyToManyField('Device', related_name='units', null=True)
    slug = models.SlugField(null=True, editable=False)

    class Meta:
        db_table = 'morchas'

    def __str__(self):
        return self.name + ":" + str(self.uuid)

    def save(self, *args):
        self.slug = slugify(self.name)
        super(Morcha, self).save(*args)


class Device(models.Model):
    repr = models.CharField(max_length=250, verbose_name='id of unit')
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        db_table = 'devices'

    def __str__(self):
        return self.repr


class Intrusion(models.Model):
    morcha = models.ForeignKey('Morcha', on_delete=models.CASCADE, related_name='morcha')
    detected_datetime = models.DateTimeField()
    verified_datetime = models.DateTimeField(null=True, blank=True)
    neutralized_datetime = models.DateTimeField(null=True, blank=True)
    non_human_intrusion_datetime = models.DateTimeField(null=True, blank=True)
    duration = models.FloatField()

    class Meta:
        db_table = 'intrusions'

    def __str__(self):
        return str(self.detected_datetime) + '-' + self.morcha.name


class Offline(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    unit = models.ForeignKey('Device', on_delete=models.CASCADE, related_name='offlineunit')

    class Meta:
        db_table = 'offline'

    def __str__(self):
        return self.unit.repr


class Backup(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    unit = models.ForeignKey('Device', on_delete=models.CASCADE, related_name='backupunit')
    battery_level = models.IntegerField()

    class Meta:
        db_table = 'backup'

    def __str__(self):
        return self.unit.repr


class Weaksignal(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    unit = models.ForeignKey('Device', on_delete=models.CASCADE, related_name='weaksignalunit')

    class Meta:
        db_table = 'weaksignal'

    def __str__(self):
        return self.unit.repr


