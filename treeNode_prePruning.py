class treeNode_prePruning(treeNode):
    def __init__(self, father, isDiscrete, attribute_for_split, attribute_value, partitionValue, data, test_data):
        treeNode.__init__(self, father, isDiscrete, attribute_for_split, attribute_value, partitionValue, data)
        self.test_data=test_data