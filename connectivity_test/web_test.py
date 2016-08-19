
# coding: utf-8

# ## This is a notebook designed test outbound connectivity from a Sight Machine Sentinel

# In[ ]:

import urllib2
import os


# In[ ]:

def check_proxy():
    http_status = False
    https_status = False
    try:
        print os.environ['http_proxy']
        http_status = True
    except KeyError:
        print 'http_proxy is not set or accessable by python'
    try:
        print os.environ['https_proxy']
        https_status = True
    except KeyError:
        print 'https_proxy is not set or accessable by python'
    return {'http': http_status, 'https': https_status}


# In[ ]:

def web_test(url, proxy = False):
    
    # http://stackoverflow.com/questions/1450132/proxy-with-urllib2
    if proxy:
        proxy = urllib2.ProxyHandler({
        'http': proxy,
        'https': proxy
        })
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        print 'proxy set to {}'.format(proxy)
        
    resp = urllib2.urlopen(url)
    page = resp.read()
    code = resp.code
    return {'code': code, 'page': page}


# In[ ]:

check_proxy()


# In[ ]:

print 'https test', web_test('https://demo.sightmachine.com/')['code']
print 'http test', web_test('https://demo.sightmachine.com/')['code']
print 'git hub test', web_test('https://github.com/sightmachine/SimpleCV.git')['code']
print 'pypi test', web_test('http://pypi.python.org')['code']


# In[ ]:
