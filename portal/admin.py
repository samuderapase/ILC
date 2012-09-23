from django.contrib import admin
from models import Author, Schedule, Blog

class AuthorAdmin(admin.ModelAdmin):
	list_display = ['user_name', 'first_name', 'last_name', 'email']
	search_fields = ['user_name', 'first_name']

class ScheduleAdmin(admin.ModelAdmin):
	list_display =['schedule', 'trainer_name', 'date_schedule']
	list_filter = ['date_schedule']
	 
class BlogAdmin(admin.ModelAdmin):
	list_display = ['name_post', 'writer', 'date_post'] 
	
admin.site.register(Author, AuthorAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Blog, BlogAdmin)
