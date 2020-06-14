from django.contrib import admin
from .models import Block, Category, Question, Answer
from django.utils.translation import gettext_lazy as _


admin.site.index_title = _('RODO questions')
admin.site.site_header = _('Infinityloop learning system')
admin.site.site_title = _('RODO questions')


class AnswersInline(admin.TabularInline):
    model = Answer
    extra = 0


class AnswersAdmin(admin.ModelAdmin):
    inlines = [
        AnswersInline,

    ]


admin.site.register(Block)
admin.site.register(Category)
admin.site.register(Question, AnswersAdmin)
