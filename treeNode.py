class treeNode:
    def __init__(self, father, isDiscrete, attribute_for_split, attribute_value, partitionValue, data):
        self.father=father
        self.isDiscrete=isDiscrete
        self.setAttributeForSplit(attribute_for_split)
        self.setAttributeValue(attribute_value)
        self.setPartitionValue(partitionValue)
        self.data=data
        self.children={}
        
    def setAttributeForSplit(self,attribute_for_split):
        self.attribute_for_split=attribute_for_split
        
    def setAttributeValue(self,attribute_value):
        self.attribute_value=attribute_value
        
    def setPartitionValue(self, partitionValue):
        self.partitionValue=partitionValue
    
    def addChild(self, attribute, child):
        self.children[attribute]=child