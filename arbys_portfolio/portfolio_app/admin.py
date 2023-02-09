from django.contrib import admin
from .models import Home,About,Profile,Category,Skills,Portfolio
# Register your models here.

# HOME
admin.site.register(Home)

# about
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)

class AboutAdmin(admin.ModelAdmin):
    inlines = [ProfileInline,
        ]
    
# skills
class skillsInline(admin.TabularInline):
    model =Skills
    extra = 2

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        skillsInline,
    ]

# portfolio
admin.site.register(Portfolio)

