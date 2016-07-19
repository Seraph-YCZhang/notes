import re
import requests
import urllib
import time

fp=open('T.txt','r')
line=fp.readline()
while line:
	retryTimes=5
	line=line.strip('\n')
	num=line
	url='http://www.kegg.jp/kegg-bin/show_organism'
	value={
		'org':num
	}
	data=urllib.urlencode(value)
	url=url+'?'+data
	while retryTimes>0:
		try:
			r=requests.get(url,timeout=20)
			break
		except :
			print 'error'
			retryTimes-=1
	content=r.text
	m=re.search(r'a href="http://www\.ncbi\.nlm\.nih\.gov/Taxonomy/Browser/wwwtax\.cgi\?mode=Info&id=[0-9]+"',content)
	s=m.group(0)
	x=re.search(r"[0-9]+",s)
	print x.group(0)
	k=x.group(0)
	fileHandle=open('No3.txt','a')
	fileHandle.write(k+'\n')
	fileHandle.close()
	line=fp.readline()
	time.sleep(0.5)


fp.close()

