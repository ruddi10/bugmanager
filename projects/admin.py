from django.contrib import admin
from .models import Project, Issue, Tag, Comment
# Register your models here.
admin.site.register(Project)
admin.site.register(Issue)
# admin.site.register(IssueAssign)
admin.site.register(Tag)
admin.site.register(Comment)


# class ProjectAdmin(admin.ModelAdmin):
#     def save_related(self, request, form, formsets, change):
#         super(GroupAdmin, self).save_related(request, form, formsets, change)
#         # do something with the manytomany data from the admin
#         form.instance.team.add(form.instance.creator)
