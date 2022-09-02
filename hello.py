
def app(env, start_response):
    resp = [bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return  resp

