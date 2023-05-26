from django import template

register = template.Library()

@register.simple_tag
def get_translation(translations, language_code):
    try:
        return translations.get(language=language_code).translated_text
    except translations.model.DoesNotExist:
        try:
            return translations.get(language='tr').translated_text  # return Turkish text if no translation
        except translations.model.DoesNotExist:
            return ''  # return an empty string if no translation in any language
