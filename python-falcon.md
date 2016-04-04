# Python Falcon

### Installation

    pip install --upgrade cython falcon
    pip install --upgrade gevent gunicorn

### Receive POST data as JSON

Shows transforming within resource method, it would be better to use a JSON translation middleware. See second section for example.

    ...
    def on_post(self, req, resp):
        body = req.stream.read()
        data = json.load(body.decode('utf-8'))
        ...
        resp.status = falcon.HTTP_201
        resp.location = '/items/{item_id}'.format(item_id=item_id)

Middleware example:

    class JSONTranslator(object):
        def process_request(self, req, resp):
            if req.content_length in (None, 0):
                return
            body = req.stream.read()
            if not body:
                raise falcon.HTTPBadRequest('Empty request body. A valid JSON document is required.')
            try:
                req.context['doc'] = json.loads(body.decode('utf-8'))
            except (ValueError, UnicodeDecodeError):
                raise falcon.HTTPError(falcon.HTTP_753, 'Malformed JSON')
                        
