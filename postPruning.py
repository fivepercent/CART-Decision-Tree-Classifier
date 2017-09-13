def postPruning(node):
    num_total=node.test_data.shape[0]
    (p_good, p_not_good)=calculateAccuracy(node.test_data)
    p_before_split=max(p_good, p_not_good)
    p_after_split=0
    for key in node.children.keys():
        child=node.children[key]
        if(child.accuracy!=None):
            accuracy_child=child.accuracy
        else:
            accuracy_child=max(calculateAccuracy(child.test_data))
            child.setAccuracy(accuracy_child)
        p_child=child.test_data.shape[0]/num_total
        p_after_split+=p_child*accuracy_child
    if(p_after_split>p_before_split):
        node.setAccuracy(p_after_split)
    else:
        node.setAccuracy(p_before_split)
        node.setAttributeForSplit('是' if p_good>p_not_good else '否')
        node.removeChildren()
        