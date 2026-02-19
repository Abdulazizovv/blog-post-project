from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Category

def post_list(request):

    if request.method == "POST":
        author = request.POST.get("author")
        body = request.POST.get("body")
        status = request.POST.get("status")
        category_id = request.POST.get("category")

        categories = Category.objects.all()

        category = Category.objects.get(id=category_id)

        post = Post.objects.create(
            author=author,
            body=body,
            category=category,
            status=status
        )
        return redirect("post_list")

    posts = Post.objects.all()
    categories = Category.objects.all()
    import random

    return render(request,"main/index.html", context={"posts": posts, "categories": categories, "name": random.randint(1, 999)})



def test_view(request):
    context = {
        "mylist": list(range(10))
    }
    return render(request, "main/test.html", context=context)