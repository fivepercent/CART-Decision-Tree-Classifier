class DecisionTree:
    def __init__(self, data):
        self.root=buildTree(data)
            
    def predict(self, test_sample):
        cur=self.root
        while len(cur.children)!=0:
            attr=test_sample[cur.attribute_for_split]
            if(type(attr)==str):
                cur=cur.children[attr]
            else:
                if(attr<=cur.partitionValue):
                    cur=cur.children['不大于']
                else:
                    cur=cur.children['大于']
        return cur.attribute_for_split