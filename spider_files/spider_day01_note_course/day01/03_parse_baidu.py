from urllib import request
from urllib import parse

# 拼接URL地址
def get_url(word):
  url = 'http://www.baidu.com/s?{}'
  # params: wd=%E7XXXXX
  params = parse.urlencode({'wd':word})
  url = url.format(params)

  return url


# 发请求,保存本地文件
def request_url(url,filename):
  headers = {'User-Agent':'Mozilla/5.0'}
  # 1.创建请求对象
  req = request.Request(url=url,headers=headers)
  # 2.获取响应对象
  res = request.urlopen(req)
  # 3.提取响应内容
  html = res.read().decode('utf-8')
  # 4.保存到本地文件
  with open(filename,'w',encoding='utf-8') as f:
    f.write(html)

if __name__ == '__main__':
  word = input('请输入搜索内容:')
  url = get_url(word)
  filename = word + '.html'
  request_url(url,filename)

















