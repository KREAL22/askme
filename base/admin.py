from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from base.models import Theme, Question, Answer, Like, Attachment


class AttachmentInlineAdmin(GenericTabularInline):
    model = Attachment


class AnswerInlineAdmin(admin.TabularInline):
    model = Answer


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')
    search_fields = ('title', )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInlineAdmin,
        AttachmentInlineAdmin,
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass
