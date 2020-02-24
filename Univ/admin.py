from django.contrib import admin

# Register your models here.
from .models import Home, Dept, CompRel, Branch, StudentInfo, Course  # Relative import

admin.site.register(Home)
admin.site.register(Dept)
admin.site.register(CompRel)
admin.site.register(Branch)
admin.site.register(StudentInfo)
admin.site.register(Course)

