class DecisionTree_prePruning(DecisionTree):
    def __init__(self, data):
        self.root=buildTree_prePruning(data)