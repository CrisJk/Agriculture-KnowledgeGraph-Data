from py2neo import Graph,Node,Relationship

class Neo4j():
	graph = None
	def __init__(self):
		print("create neo4j class ...")
		
	def connectDB(self):
		self.graph = Graph("http://localhost:7474", username="neo4j", password="123456")
		
	def matchItembyTitle(self,value):
		answer = self.graph.find_one(label="Item",property_key="title",property_value=value)
		return answer

	# 根据title值返回互动百科item
	def matchHudongItembyTitle(self,value):
		answer = self.graph.find_one(label="HudongItem",property_key="title",property_value=value)
		return answer

	# 根据entity的名称返回关系
	def getEntityRelationbyEntity(self,value):
		answer = self.graph.data("MATCH (entity1) - [rel] -> (entity2)  WHERE entity1.title = \"" +value +"\" RETURN rel,entity2")
		return answer

	#查询两个实体间存在的关系
	def findRelationBetweenEntities(self,entity1):
		answer = self.graph.data("MATCH (n1:HudongItem {title:\""+entity1+"\"})- [rel] -> (n2) RETURN rel,n2" )
		if(len(answer) == 0):
			answer = self.graph.data("MATCH (n1:NewNode {title:\""+entity1+"\"})- [rel] -> (n2) RETURN rel,n2" )
		return answer

	#查找一个实体及其对应的关系（与findRelationBetweentEntities的差别就是返回值不一样
	def findRelationByEntity(self,entity1):
		answer = self.graph.data("MATCH (n1:HudongItem {title:\""+entity1+"\"})- [rel] -> (n2) RETURN n1,rel,n2" )
		if(len(answer) == 0):
			answer = self.graph.data("MATCH (n1:NewNode {title:\""+entity1+"\"})- [rel] -> (n2) RETURN n1,rel,n2" )
		return answer
	#根据一个实体和指定的关系查找另一实体
	def findOtherEntities(self,entity,relation):
		answer = self.graph.data("MATCH (n1:HudongItem {title:\"" + entity + "\"})- ["+relation+"] -> (n2) RETURN n2" )
		if(len(answer == 0)):
			answer = self.graph.data("MATCH (n1:NewNode {title:\"" + entity + "\"})- ["+relation+"] -> (n2) RETURN n2" )

		return answer

	#根据两个实体查询它们之间的关系
	def findRelationByEntities(self,entity1,entity2):
		answer = self.graph.data("MATCH (n1:HudongItem {title:\"" + entity1 + "\"})- [rel] -> (n2:HudongItem{title:\""+entity2+"}) RETURN rel" )
		if(len(answer) == 0):
			answer = self.graph.data("MATCH (n1:HudongItem {title:\"" + entity1 + "\"})- [rel] -> (n2:NewNode{title:\""+entity2+"}) RETURN rel" )
		if(len(answer) == 0):
			answer = self.graph.data("MATCH (n1:NewNode {title:\"" + entity1 + "\"})- [rel] -> (n2:HudongItem{title:\""+entity2+"}) RETURN rel" )
		if(len(answer) == 0):
			answer = self.graph.data("MATCH (n1:NewNode {title:\"" + entity1 + "\"})- [rel] -> (n2:NewNode{title:\""+entity2+"}) RETURN rel" )

		return answer

	def findEntityRelation(self,entity1,entity2,relation):
		answer = self.graph.data("MATCH (n1:HudongItem {title:\"" + entity1 + "\"})- ["+relation+"] -> (n2:HudongItem{title:\""+entity2+"}) RETURN rel" )
		if(len(answer) == 0):
			answer = self.graph.data("MATCH (n1:HudongItem {title:\"" + entity1 + "\"})- ["+relation+"] -> (n2:NewNode{title:\""+entity2+"}) RETURN rel" )
		if(len(answer) == 0):
			answer = self.graph.data("MATCH (n1:NewNode {title:\"" + entity1 + "\"})- ["+relation+"] -> (n2:HudongItem{title:\""+entity2+"}) RETURN rel" )
		if(len(answer) == 0):
			answer = self.graph.data("MATCH (n1:NewNode {title:\"" + entity1 + "\"})- ["+relation+"] -> (n2:NewNode{title:\""+entity2+"}) RETURN rel" )

		return answer
