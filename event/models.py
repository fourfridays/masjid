from django.db import models

from wagtail.core.blocks import RichTextBlock, StructBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from django.utils import timezone
from page.models import BasePage

class EventIndexPage(BasePage):
    hero_image = models.ForeignKey(
        'images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='2400X858px'
    )
    hero_heading = models.CharField(
        null=True,
        blank=True,
        max_length=140,
        help_text='40 character limit.'
        )
    hero_caption = models.CharField(
        null=True,
        blank=True,
        max_length=140,
        help_text='140 character limit.'
        )

    subpage_types = ['EventPage']

    content_panels = BasePage.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('hero_image'),
            FieldPanel('hero_heading', classname='full'),
            FieldPanel('hero_caption', classname='full'),
            ], heading='Hero Image'),
    ]

    def get_context(self, request):
        context = super(EventIndexPage, self).get_context(request)
        context['events'] = EventPage.objects.all()

        return context


class EventPage(BasePage):
    hero_image = models.ForeignKey(
        'images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='2400X858px'
    )
    body = StreamField([
        ('description', RichTextBlock()),
    ], default='')
    start_time = models.DateTimeField(default=timezone.now())
    end_time = models.DateTimeField(default=timezone.now())

    content_panels = BasePage.content_panels + [
        ImageChooserPanel('hero_image'),
        StreamFieldPanel('body'),
        FieldPanel('start_time'),
        FieldPanel('end_time'),
    ]
