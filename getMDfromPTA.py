import requests
from datetime import datetime
with open('url_cookie.txt', 'rt') as f:
	data = f.read().split('\n')
data = [item for item in data if item != '']
url = data[1]
headers = {
	'Accept': 'application/json;charset=UTF-8',
	'cookie': data[0]
}
r = requests.get(url,headers=headers).json()
problem = r['problemSetProblem']
idx = problem['label']
title = problem['title']
score = problem['score']
content = problem['content'].replace('$$','$')
content = content.replace('### Input Specification:', '<!--more-->\n\n## Input Specification')
content = content.replace('### Output Specification:', '## Output Specification')
content = content.replace('### Sample Input:', '## Sample Input\n')
content = content.replace('### Sample Output:', '## Sample Output\n')
code = problem['lastSubmissionDetail']['programmingSubmissionDetail']['program'].replace('<','&lt;').replace('>','&gt;')

file_name = './source/_posts/' + idx + '-' + title.replace(' ','-') + '-' + str(score) + '分.md'
article_title = idx + ' ' + title + ' (' + str(score) + '分)'


time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

res = [
	'---',
	'title: %s'%article_title,
	'date: %s'%time,
	'updated: %s'%time,
	'mathjax: true',
	'tags:',
	'- CPP',
	'- 算法',
	'categories:',
	'- PAT甲级真题',
	'---',
	'',
	content,
	'',
	'## 分析',
	'',
	'分析',
	'',
	'## AC代码',
	'',
	'```cpp',
	code,
	'```',
	'',
	'## 原题地址',
	'',
	'[%s](%s)'%(article_title,url.replace('/api', '')),
	''
]
with open(file_name,'wt',encoding='utf-8') as f:
	f.write('\n'.join(res))