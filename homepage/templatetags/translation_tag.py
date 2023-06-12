from django import template

register = template.Library()

# @register.simple_tag
# def get_translation(page_content, translations, language_code):
#     print(f'Page content: {page_content}')
#     print(f'Translations: {translations}')
#     print(f'Language code: {language_code}')
#     if language_code == 'tr':
#         return page_content.text  # return original Turkish text
#     try:
#         return translations.get(language=language_code).translated_text
#     except translations.model.DoesNotExist:
#         return page_content.text  # return original Turkish text if no translation


@register.simple_tag
def get_translation(page_content, translations, language_code):
    # Return original text if language_code is 'tr'
    if language_code == 'tr':
        return page_content.text
    # Try to return the translated text for the given language
    try:
        return translations.get(language=language_code).translated_text
    except translations.model.DoesNotExist:
        # If a translation doesn't exist, return the text in a default language
        try:
            return translations.get(language='tr').translated_text
        except translations.model.DoesNotExist:
            return page_content.text