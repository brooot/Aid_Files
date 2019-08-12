import urllib.request

# urlopen:得到的结果为响应对象
response=urllib.request.urlopen('http://httpbin.org/get')
# 获取响应对象内容
html = response.read().decode('utf-8')
# 获取HTTP响应码
code = response.getcode()
# 获取返回实际数据的URL地址
url = response.geturl()

print(html)















