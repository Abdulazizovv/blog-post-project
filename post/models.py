from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ("title",)


class Post(models.Model):
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    author = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    status_choices = (
        ("draft", "Qoralama"),
        ("public", "Ommaviy"),
        ("deleted", "O'chirilgan"),
        ("archived", "Arxivlangan")
    )

    status = models.CharField(max_length=15, choices=status_choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:50] + "..." if len(self.body) > 50 else self.body  