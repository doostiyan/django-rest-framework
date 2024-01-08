from django.contrib import admin

from home.models import Person, Answer, Question

admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Answer)
