import scrapy
import re
import requests
from CN_DBpediaCrawler.items import CnDbpediacrawlerItem
from requests.adapters import HTTPAdapter
import time
class CNDBpediaEntityRelationSpider(scrapy.spiders.Spider):
	name = "getEntityRelation"
	allowed_domains = ["http://shuyantech.com"]
	#allowed_domains = ["http://www.ip181.com"]
	start_urls = [
		"http://www.baidu.com"
	]
	# start_urls = [
	# 	"http://www.ip181.com"
	# ]
	# def parse(self,response):
	# 	headers = {
	# 		"user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
	# 		"accept-language" : "zh-CN,zh;q=0.9,en;q=0.8",
	# 		"keep_alive" : "False"
	# 	}
	# 	httpRequest = requests.session()
	# 	httpRequest.mount('https://',HTTPAdapter(max_retries = 30))
	# 	httpRequest.mount('http://',HTTPAdapter(max_retries = 30))
	# 	sss = httpRequest.get("http://www.ip181.com",headers=headers)
	# 	print(sss.text.encode('gbk').decode('utf-8'))
	# 	httpRequest.close()
	def parse(self,response):
		entityList = list()
		entityNumberList = list()
		entityCount = 0 
		with open('/home/kuangjun/WikidataSpider/CN_DBpediaCrawler/predict_labels3.txt','r') as fr:
			for line in fr:
				entity = line.split(" ")[0]
				if(len(line.split(" ")) >= 2):
					entityNumber = line.split(" ")[1][0:-1]
				else:
					entityNumber = "999"
				entityList.append(entity)
				entityNumberList.append(entityNumber)
				entityCount += 1

		count = 0

		url_list = list()
		for entity in entityList:
			url = "http://shuyantech.com/api/cndbpedia/avpair?q="+entity
			url_list.append(url)

		headers = {
			"user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
			"accept-language" : "zh-CN,zh;q=0.9,en;q=0.8",
			"keep_alive" : "False"
		}
		proxy_list = list()
		proxy_list.append({"http":"http://120.77.201.46:8080","https":"http://120.77.201.46:8080"})
		proxy_list.append({"http":"http://47.92.73.2:8088","https":"http://47.92.73.2:8088"})
		proxy_list.append({"http":"http://47.95.36.86:8081","https":"http://47.95.36.86:8081"})
		proxy_list.append({"http":"http://218.202.219.82:81","https":"http://218.202.219.82:81"})
		proxy_list.append({"http":"http://61.160.190.146:8090","https":"http://61.160.190.146:8090"})		
		proxy_list.append({"http":"http://116.199.2.210:80","https":"http://116.199.2.210:80"})	
		proxy_list.append({"http":"http://116.199.115.78:82","https":"http://116.199.115.78:82"})
		proxy_list.append({"http":"http://116.199.2.209:80","https":"http://116.199.2.209:80"})
		proxy_list.append({"http":"http://47.94.230.42:9999","https":"http://47.94.230.42:9999"})
		proxy_list.append({"http":"http://139.199.38.32:3128","https":"http://139.199.38.32:3128"})
		proxy_list.append({"http":"http://140.205.222.3:80","https":"http://140.205.222.3:80"})
		proxy_list.append({"http":"http://119.23.252.11:8080","https":"http://119.23.252.11:8080"})
		proxy_list.append({"http":"http://139.199.49.13:80","https":"http://139.199.49.13:80"})
		proxy_list.append({"http":"http://222.186.10.29:3128","https":"http://222.186.10.29:3128"})
		proxy_list.append({"http":"http://211.159.219.158:80","https":"http://211.159.219.158:80"})
		proxy_list.append({"http":"http://47.95.36.86:8081","https":"http://47.95.36.86:8081"})
		proxy_list.append({"http":"http://120.77.201.46:8080","https":"http://120.77.201.46:8080"})
		proxy_list.append({"http":"http://47.92.73.2:8088","https":"http://47.92.73.2:8088"})
		proxy_list.append({"http":"http://47.95.36.86:8081","https":"http://47.95.36.86:8081"})
		proxy_list.append({"http":"http://218.202.219.82:81","https":"http://218.202.219.82:81"})
		proxy_list.append({"http":"http://61.160.190.146:8090","https":"http://61.160.190.146:8090"})		
		proxy_list.append({"http":"http://116.199.2.210:80","https":"http://116.199.2.210:80"})	
		proxy_list.append({"http":"http://116.199.115.78:82","https":"http://116.199.115.78:82"})
		proxy_list.append({"http":"http://116.199.2.209:80","https":"http://116.199.2.209:80"})
		proxy_list.append({"http":"http://47.94.230.42:9999","https":"http://47.94.230.42:9999"})
		proxy_list.append({"http":"http://139.199.38.32:3128","https":"http://139.199.38.32:3128"})
		proxy_list.append({"http":"http://140.205.222.3:80","https":"http://140.205.222.3:80"})



		pcount = 0 
		for url in url_list:
			time.sleep(5)	
			print(1.0*count/entityCount)
			proxy_count = (pcount%27) 
			proxies = proxy_list[proxy_count]  
			print("***************proxy_ip is "+str(proxy_list[proxy_count])+'\n')
			try:
				flag = 1
				while(flag == 1):
					print("start....")
					httpRequest = requests.session()
					httpRequest.mount('https://',HTTPAdapter(max_retries = 30))
					httpRequest.mount('http://',HTTPAdapter(max_retries = 30))
					entityjson = httpRequest.get(url,headers=headers,proxies = proxies,timeout = 5).json()
					if(entityjson['status'] != "ok"):
						print("fail")
						proxy_count =(proxy_count+1)%27 
						proxies = proxy_list[proxy_count]
					else:
						flag = 0
					httpRequest.close()
			except:
				print("httpRequest Error!")
				httpRequest.close() 
				pcount += 1
			else:
				entity1 = entityList[count]
				print(entityjson)
				if 'ret' in entityjson  :
					for entityAndRelation in entityjson['ret']:
						relation  = entityAndRelation[0]
						entity2 = entityAndRelation[1]
						tmp = CnDbpediacrawlerItem()
						tmp['entity1'] = entity1
						tmp['entity2'] = entity2
						tmp['relation'] = relation

						yield tmp

				count += 1
				pcount += 1
