from django.contrib import admin
from .models import  (Skill, Education,Experience,Language,Courses)


class EducationAdmin(admin.ModelAdmin):
    list_display = ["university_name", "start_date", "end_date", "grade", "created_on"]
    list_filter = ["start_date"]


class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "value"]
    list_filter = ["value"]
    search_fields = ["name"]


class LanguageAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "created_on"]


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["job_possition", "start_date",
                    "end_date","is_current","addres" ,"job_description","company_name", ]
    list_filter = ["start_date"]

# class TestimonialAdmin(admin.ModelAdmin):
#     list_display = ["name", "job_position", "created_on"]
    
    
class CoursesAdmin(admin.ModelAdmin):
    list_display = ["program", "program_name", "cours_nam"]    

# Register your models here.
admin.site.register(Skill,SkillAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Language,LanguageAdmin)
# admin.site.register(SocialMedia)
# admin.site.register(Testimonial,TestimonialAdmin)
# admin.site.register(Service)
admin.site.register(Courses,CoursesAdmin)


