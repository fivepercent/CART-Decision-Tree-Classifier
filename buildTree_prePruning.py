def buildTree_prePruning(data):
    splitData=generate_Training_Test_Set(data, 0.4)
    root=treeNode_prePruning(None, True, None, None, None, splitData[0], splitData[1])
    q=Queue()
    q.put(root)
    while not q.empty():
        cur = q.get()
        if(calculateGini(cur.data)==0):
            cur.setAttributeForSplit(cur.data['好瓜'].iloc[0])
            continue
        (attribute_for_split, T)=chooseAttributeForSplit(cur.data)
        pruning=prePruning(cur.test_data, attribute_for_split, T)
        if(pruning[0]):
            cur.setAttributeForSplit(attribute_for_split)
        else:
            cur.setAttributeForSplit(pruning[1])
            continue
        if(T==None):
            for attr_value in cur.data[attribute_for_split].unique():
                child_data=cur.data[cur.data[attribute_for_split]==attr_value]
                child_test_data=cur.test_data[cur.test_data[attribute_for_split]==attr_value]
                if(child_data.shape[0]>0):
                    child = treeNode_prePruning(cur, True, None, attr_value, None, child_data, child_test_data)
                    cur.addChild(attr_value,child)
                    q.put(child)
        else:
            smaller_data=cur.data[cur.data[attribute_for_split]<=T]
            smaller_test_data=cur.test_data[cur.test_data[attribute_for_split]<=T]
            if(smaller_data.shape[0]>0):
                smaller_child=treeNode_prePruning(cur, False, None, '不大于', None, smaller_data, smaller_test_data)
                cur.setPartitionValue(T)
                cur.addChild('不大于', smaller_child)
                q.put(smaller_child)
            larger_data=cur.data[cur.data[attribute_for_split]>T]
            larger_test_data=cur.test_data[cur.test_data[attribute_for_split]>T]
            if(larger_data.shape[0]>0):
                larger_child=treeNode_prePruning(cur, False, None, '大于', None, larger_data, larger_test_data)
                cur.setPartitionValue(T)
                cur.addChild('大于', larger_child)
                q.put(larger_child)
    return root