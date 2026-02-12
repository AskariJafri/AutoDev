from flask import request

class RequestMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Log basic request info
        print(f"Request from {environ['REMOTE_ADDR']} - {environ['HTTP_HOST']}")
        
        # Continue processing
        return self.app(environ, start_response)

def setup_middleware(app):
    middleware = RequestMiddleware(app)
    app.wsgi_app = middleware