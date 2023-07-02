# default_language_middleware.py

from django.shortcuts import redirect

class DefaultLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # check if it's the root path and there is no language prefix
        if request.path == '/' and '/tr' not in request.path:
            return redirect('/tr')
        
        # otherwise, just continue as normal
        response = self.get_response(request)
        return response
