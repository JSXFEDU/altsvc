import os
from flask import Flask, Response
app = Flask(__name__)


@app.route('/altsvc')
def hello_world():
	r = Response()
#	r.headers['Alt-Svc'] = 'h2="marvin-production-0-1888329800.cn-north-1.elb.amazonaws.com.cn:443"; ma=3600'
#	r.headers['Alt-Svc'] = 'h2="marvin-production-1-1251614655.cn-north-1.elb.amazonaws.com.cn:443"; ma=3600'
	r.headers['Alt-Svc'] = 'h2="{}"; ma=3600'.format(os.environ['OTHERDOMAIN'])

	print(r.headers)
	print(type(r.headers))
	data = 'You accessed {}, <br>Switch to {}'.format(os.environ['THISDOMAIN'], os.environ['OTHERDOMAIN']) + \
	'<br><a href="/altsvc">go back</a>'
	r.set_data(data)
#	return 'Hello World!'
	return r

if __name__ == '__main__':
	app.run('0.0.0.0',8080)