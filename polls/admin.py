from django.utils import timezone
import datetime
from django.contrib import admin
from .models import Question,Choices
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choices
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
   @admin.display(
      boolean= True,
      ordering="pub_date",
      description="Published recently?"

   )
   def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
   list_filter = ["pub_date"]
   search_fields = ["question_text"]
   inlines = [ChoiceInline]


admin.site.register(Question,QuestionAdmin)
