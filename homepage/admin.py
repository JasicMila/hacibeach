from django.contrib import admin
import nested_admin
from .models import ContactRequest, Page, PageContent, Image, TranslatedPageContent

class TranslatedPageContentInline(nested_admin.NestedStackedInline):
    model = TranslatedPageContent
    extra = 2

class PageContentInline(nested_admin.NestedStackedInline):
    model = PageContent
    extra = 1
    inlines = [TranslatedPageContentInline]

class PageAdmin(nested_admin.NestedModelAdmin):
    inlines = [PageContentInline]
    list_display = ('title', 'slug', 'get_page_content')

    def get_page_content(self, obj):
        return obj.pagecontent_set.first().text

    get_page_content.short_description = 'Page Content'


admin.site.register(ContactRequest)
admin.site.register(Page, PageAdmin)
admin.site.register(Image)


