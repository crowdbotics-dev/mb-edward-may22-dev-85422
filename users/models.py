from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # WARNING!
    """
    Some officially supported features of Crowdbotics Dashboard depend on the initial
    state of this User model (Such as the creation of superusers using the CLI
    or password reset in the dashboard). Changing, extending, or modifying this model
    may lead to unexpected bugs and or behaviors in the automated flows provided
    by Crowdbotics. Change it at your own risk.


    This model represents the User instance of the system, login system and
    everything that relates with an `User` is represented by this model.
    """
    name = models.CharField(null=True,blank=True,max_length=255,)
    bigIntegerField = models.BigIntegerField(null=True,blank=True,)
    binaryField = models.BinaryField(null=True,blank=True,)
    booleanField = models.BooleanField(null=True,blank=True,)
    dateField = models.DateField(auto_now=True,null=True,blank=True,)
    dateTimeField = models.DateTimeField(auto_now=True,null=True,blank=True,)
    decimalField = models.DecimalField(max_digits=30,decimal_places=10,null=True,blank=True,)
    durationField = models.DurationField(null=True,blank=True,)
    emailField = models.EmailField(max_length=254,null=True,blank=True,)
    floatField = models.FloatField(null=True,blank=True,)
    integerField = models.IntegerField(null=True,blank=True,)
    genericIPAddressField = models.GenericIPAddressField(protocol="both",unpack_ipv4=False,null=True,blank=True,)
    positiveIntegerField = models.PositiveIntegerField(null=True,blank=True,)
    positiveSmallIntegerField = models.PositiveSmallIntegerField(null=True,blank=True,)
    slugField = models.SlugField(max_length=50,null=True,blank=True,)
    smallIntegerField = models.SmallIntegerField(null=True,blank=True,)
    textField = models.TextField(null=True,blank=True,)
    timeField = models.TimeField(auto_now=True,null=True,blank=True,)
    urlField = models.URLField(null=True,blank=True,)
    uuiField = models.UUIDField(null=True,blank=True,)
    foreignKey = models.ForeignKey("users.Just_one_field",on_delete=models.CASCADE,null=True,blank=True,related_name="user_foreignKey",)
    one2oneField = models.OneToOneField("users.Model3",on_delete=models.CASCADE,null=True,blank=True,related_name="user_one2oneField",)
    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
class Model3(models.Model):
    'Generated Model'
    bigIntegerField = models.BigIntegerField()
    many2many = models.ManyToManyField("users.Model6",blank=True,related_name="model3_many2many",)
class Model4(models.Model):
    'Generated Model'
    urlField = models.URLField()
class Just_one_field(models.Model):
    'Generated Model'
    txt = models.TextField()
    edward = models.BooleanField(null=True,blank=True,)
    many2many = models.ManyToManyField("users.Model4",blank=True,related_name="just_one_field_many2many",)
    one2one = models.OneToOneField("users.Model5",on_delete=models.CASCADE,null=True,blank=True,related_name="just_one_field_one2one",)
class Model5(models.Model):
    'Generated Model'
    char = models.CharField(max_length=256,)
class Model6(models.Model):
    'Generated Model'
    date = models.DateField()
