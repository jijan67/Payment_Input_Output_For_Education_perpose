from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name


class Batch(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Course(models.Model):
    Course_Code = models.CharField(max_length=100)
    Course_Title = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    Batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    Credits = models.CharField(max_length=100, null=False)


    def __str__(self):
        return "%s %s %s" %(self.Course_Code, self.Course_Title, self.Batch)
