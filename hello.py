def app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    
    body = (
        environ['QUERY_STRING']     #
        .split('?')[-1]             # от последнего '?'
        .split('#')[0]              # до первого #
        .replace('&', '\n')         #
        .encode('utf-8')
    )
    
    start_response(status, headers)
    return [body]
