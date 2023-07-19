from django.contrib import admin


# Register your models here.
admin.site.site_header = "POLLSTERS ADMIN "
admin.site.site_title = "POLLSTER ADMIN AREA"
admin.site.index_title = "welcome to the POLLSTER ADMIN AREA "
from  .models import Question, Choice

class ChoiceINLine(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':[ 'question_text']}),
                ("Date information ",{'fields': ['pub_date'],'classes':
                ['collapse']}),]
    inlines = [ChoiceINLine]

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)