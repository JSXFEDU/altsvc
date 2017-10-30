import os
from flask import Flask, request, abort, Response
app = Flask(__name__)


@app.route('/altsvc')
def altsvc():
	page = '<a href="/altsvc">Refresh</a><br>\n'
	domains = os.environ['DOMAIN_LIST'].split(',')
	index = int(os.environ['DOMAIN_INDEX'])
	page += 'You are accressing {}<br>\n'.format(domains[index])
	rsp = Response()
	if 'code421' in request.args:
		abort(421)
		
	if 'Alt-Used' in request.headers:
		page += 'Using alt svc:{}<br>\n'.format(request.headers['Alt-Used'])
	
	page += '<a href="/altsvc?code421=1">Send Code 421</a><br>\n'
		
	if 'alt' in request.args:
		temp = 'h2="{}"; ma=30'.format(request.args['alt'])
		rsp.headers['Alt-Svc'] = temp
		page += 'Send Head: Alt-Svc: {}<br>\n'.format(temp)
	
	for domain in os.environ['DOMAIN_LIST'].split(','):
		page += '<a href="/altsvc?alt={}">Send Alt {}</a><br>\n'.format(domain, domain)
	
	rsp.set_data(page)
	return rsp
	
	
if __name__ == '__main__':
	app.run('0.0.0.0',8080)