from django.contrib import admin
from .models import Student, Course, Profile

class ProfileInlineAdmin(admin.TabularInline):
    model = Profile
    max_num = 1
    can_delete=False

class StudentAdmin(admin.ModelAdmin):
    inlines = [ProfileInlineAdmin]
    list_display = ["id", "full_name", "phone_number", "created_at", "updated_at"]
    list_display_links = ["full_name"]
    list_filter = ["created_at", "courses"]
    search_fields = ["phone_number", "first_name", "last_name"]
    fields = ["first_name", "last_name", "phone_number", "courses", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at", "id",]


class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "discount", "discount_type", "final_price"]
    search_fields = ["title", "description"]
    list_filter = ["discount_type"]
    ordering = ["-price"]



admin.site.register(Student, StudentAdmin)

admin.site.register(Course, CourseAdmin)