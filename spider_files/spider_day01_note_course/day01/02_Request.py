from urllib import request

# 先定义常用变量
url = 'http://www.baidu.com/'
headers = {
  'User-Agent':'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'
}
# 1. 创建请求对象 - 包装,并没有真正发请求
req = request.Request(url=url,headers=headers)
# 2. 获取响应对象
res = request.urlopen(req)
# 3. 提取响应内容
html = res.read().decode('utf-8')

print(html)








