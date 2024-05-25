from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import timedelta,datetime

# Create your models here.

class Person(models.Model):
    image = models.ImageField(blank=False,null=False)
    unique_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100,blank=False,null=False)
    designation = models.CharField(max_length=100,blank=False,null=False)
    phone = models.CharField(max_length=10)
    district = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    validity_date = models.DateField()
    
    def save(self, *args, **kwargs):
        if not self.unique_id:
            last_person = Person.objects.order_by('id').last()
            if last_person:
                last_id = int(last_person.unique_id.split('-')[1].split('/')[0])
                new_id = f"KL-{last_id + 1:04d}/TVM"
            else:
                new_id = "KL-0001/TVM"
            self.unique_id = new_id
        super().save(*args, **kwargs)

    @property
    def is_valid(self):
        # Check if validity_date is greater than or equal to today's date
        return self.validity_date >= datetime.now().date()

@receiver(pre_save, sender=Person)
def set_validity_date(sender, instance, **kwargs):
    if instance.validity_date:
        if instance.pk:  # Check if the instance is being updated
            previous_instance = sender.objects.get(pk=instance.pk)
            if instance.validity_date != previous_instance.validity_date:
                instance.validity_date = instance.validity_date + timedelta(days=365)
        else:
            instance.validity_date = instance.validity_date + timedelta(days=365)

class Meta:
    verbose_name = 'Person'

def __str__(self):
    return self.name