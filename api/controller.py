import json
from tornado.web import RequestHandler


class Controller(RequestHandler):
    def set_default_headers(self, *args, **kwargs):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Content-Type', 'application/json')
        self.set_header('Cache-Control', 'public, max-age=3600')

    def write_error(self, status_code, message=None):
        self.set_status(status_code)
        if message:
            self.finish(json.dumps({
                'message': message
            }))
        elif status_code:
            self.set_status(status_code)
            self.finish()

    def write_response(self, status_code, result=None):
        self.set_status(status_code)
        if result:
            self.finish(result)
        elif status_code:
            self.set_status(status_code)
            self.finish()
