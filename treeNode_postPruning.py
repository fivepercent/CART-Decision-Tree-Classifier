class treeNode_postPruning(treeNode_prePruning):
    def __init__(self, father, isDiscrete, attribute_for_split, attribute_value, partitionValue, data, test_data, accuracy):
        treeNode_prePruning.__init__(self, father, isDiscrete, attribute_for_split, attribute_value, partitionValue, data, test_data)
        self.setAccuracy(accuracy)
    
    def setAccuracy(self, accuracy):
        self.accuracy=accuracy
    
    def removeChildren(self):
        self.children.clear()