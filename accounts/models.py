from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save


TAGS = TaggableManager(
    verbose_name="programming languages", help_text="A comma-separated list of Programming Languages.")
HITS = GenericRelation(HitCount, object_id_field='object_pk',
                       related_query_name='hit_count_generic_relation')


class CustomUser(AbstractUser):

    LEVELS = (
        ('JR', 'Junior'),
        ('MID', 'Mid-Level'),
        ('SR', 'Senior'),

    )
    national_id = models.PositiveIntegerField(null=True)
    city = models.CharField(max_length=50, null=True)
    bio = models.TextField(null=True)
    experience_level = models.CharField(
        choices=LEVELS, max_length=3, default='JR',)
    programming_languages = TAGS


class Profile(models.Model):
    employee = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE, related_name='profile'
    )

    number_of_views = HITS

    # Create a profile when a new user is created

    @receiver(post_save, sender=get_user_model())
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(employee=instance)

    @receiver(post_save, sender=get_user_model())
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.employee.username
