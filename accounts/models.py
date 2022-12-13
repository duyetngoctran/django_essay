from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.IntegerField(default=0)
    

    def __str__(self):
        return self.user.username

def post_save_student_create(sender, instance, created, *args, **kwargs):
    if created:
        Student.objects.get_or_create(user=instance)
    # free_membership = Membership.objects.get_or_create(membership_type='Free', slug='free')
    student, created = Student.objects.get_or_create(user=instance)


  



class Essay(models.Model):    
    student = models.ForeignKey(Student,
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    result_description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
   


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    
def post_save_essay_create(sender, instance, created, *args, **kwargs):
    if not instance.result_description:
        print("blank")
    else:
        print(instance.result_description)    
    


   
post_save.connect(post_save_student_create, sender=User)
post_save.connect(post_save_essay_create, sender=Essay)
