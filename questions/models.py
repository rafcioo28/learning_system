from django.db import models
from django.utils.translation import gettext_lazy as _


class Block(models.Model):
    block_name = models.CharField(max_length=150, verbose_name=_('block name'))
    block_description = models.TextField(
        blank=True, verbose_name=_('block description'))

    class Meta:
        verbose_name = _('block')
        verbose_name_plural = _('blocks')

    def __str__(self):
        return f'{self.block_name}'


class Category(models.Model):
    category_name = models.CharField(
        max_length=150, verbose_name=_('category name'))

    category_description = models.TextField(
        blank=True, verbose_name=_('category description'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return f'{self.category_name}'


class Question(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    question_text = models.TextField(verbose_name=_('question text'))
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category_questions',
        verbose_name=_('category')
    )
    questions_block = models.ForeignKey(
        Block, on_delete=models.CASCADE, related_name='block_questions',
        verbose_name=_('questions block')
    )

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')

    def __str__(self):
        return f'{self.title} [{self.questions_block}/{self.category}]'


class Answer(models.Model):
    answer = models.TextField(verbose_name=_('answer'))
    correct = models.BooleanField(default=False, verbose_name=_('correct'))
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers',
        verbose_name=_('question')
    )

    class Meta:
        verbose_name = _('answer')
        verbose_name_plural = _('answers')

    def __str__(self):
        return f'{self.answer[:100]}... [{self.correct}]'
