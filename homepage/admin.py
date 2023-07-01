from django.contrib import admin
import nested_admin
from .models import ContactRequest, Page, PageContent, Image, TranslatedPageContent

class TranslatedPageContentInline(nested_admin.NestedStackedInline):
    model = TranslatedPageContent
    extra = 0

class PageContentInline(nested_admin.NestedStackedInline):
    model = PageContent
    extra = 0
    inlines = [TranslatedPageContentInline]

class PageAdmin(nested_admin.NestedModelAdmin):
    inlines = [PageContentInline]
    # list_display = ('title', 'slug', 'get_page_content')
    list_display = ('title', 'slug', 'get_page_content_count')

    # def get_page_content(self, obj):
    #     return obj.pagecontent_set.first().text
    #
    # get_page_content.short_description = 'Page Content'
    def get_page_content_count(self, obj):
        return obj.pagecontent_set.count()

    get_page_content_count.short_description = 'Page Content Count'


admin.site.register(ContactRequest)
admin.site.register(Page, PageAdmin)
admin.site.register(Image)


