from django.contrib import admin
from .models import ContactRequest, Page, PageContent, Image, TranslatedPageContent

class TranslatedPageContentInline(admin.StackedInline):
    model = TranslatedPageContent
    extra = 2

class PageContentInline(admin.StackedInline):
    model = PageContent
    extra = 1
    inlines = [TranslatedPageContentInline]

class PageAdmin(admin.ModelAdmin):
    inlines = [PageContentInline]
    list_display = ('title', 'slug', 'get_page_content')

    def get_page_content(self, obj):
        return obj.pagecontent_set.first().text

    get_page_content.short_description = 'Page Content'

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    inlines = [TranslatedPageContentInline]
    list_display = ('get_page_title', 'id')

    def get_page_title(self, obj):
        return obj.page.title

admin.site.register(ContactRequest)
admin.site.register(Page, PageAdmin)
admin.site.register(Image)


