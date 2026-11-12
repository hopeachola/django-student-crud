from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically records when it was sent

    def __str__(self):
        return f"Message from {self.name} - {self.email}"


# 👇 New model for your CRUD operations
class Recipe(models.Model):
    title = models.CharField(max_length=150)
    ingredients = models.TextField()
    prep_time = models.IntegerField(help_text="Time in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Student(models.Model):
    full_name = models.CharField(max_length=150)
    reg_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.reg_number})"
