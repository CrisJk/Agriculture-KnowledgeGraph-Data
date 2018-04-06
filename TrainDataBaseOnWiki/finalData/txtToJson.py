import json
import sys

if(len(sys.argv) != 3):
	print("参数数量错误，请输入两个参数 源文件名 目标文件名")
else:
	
	with open(sys.argv[1],'r') as fr:
		with open(sys.argv[2],'a') as fw:
			for line in fr:
				data = line.split('\t')
				if(len(data) == 4):
					train_data = dict()
					train_data['Entity1'] = data[0].strip()
					train_data['Entity2'] = data[1].strip()
					train_data['Statement'] = data[2].strip()
					train_data['Relation'] = data[3].strip()
					train_data_json = json.dumps(train_data)
					fw.write(train_data_json+"\n")