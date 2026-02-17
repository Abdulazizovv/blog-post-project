from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    
    discount_type_choices = (
        ("percent", "Foizli"),
        ("flex", "Aniq")
    )
    
    discount_type = models.CharField(max_length=15, choices=discount_type_choices)

    discount = models.IntegerField(default=0)

    def final_price(self):
        if self.discount:
            if self.discount_type == "percent":
                return self.price - (self.price / 100 * self.discount)
            return self.price - self.discount
        return self.price

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    courses = models.ManyToManyField(Course, blank=True)

    # VAQT UCHUN
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return self.first_name + " " + str(self.last_name) if self.last_name else self.first_name


class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True)
    ...


