def prePruning(test_data, attribute_for_split, T):
    num_total=test_data.shape[0]
    (p_good, p_not_good)=calculateAccuracy(test_data)
    p_before_split=max(p_good, p_not_good)
    p_after_split=0
    if(T==None):
        for attr_value in test_data[attribute_for_split].unique():
            sub_test_data=test_data[test_data[attribute_for_split]==attr_value]
            p_attr_value=sub_test_data.shape[0]/num_total
            accuracy_attr_value=max(calculateAccuracy(sub_test_data))
            p_after_split+=p_attr_value*accuracy_attr_value
    else:
        smaller_test_data=test_data[test_data[attribute_for_split]<=T]
        p_smaller=smaller_test_data.shape[0]/num_total
        accuracy_smaller=max(calculateAccuracy(smaller_test_data))
        larger_test_data=test_data[test_data[attribute_for_split]>T]
        p_larger=larger_test_data.shape[0]/num_total
        accuracy_larger=max(calculateAccuracy(larger_test_data))
        p_after_split=p_smaller*accuracy_smaller+p_larger*accuracy_larger
    return (p_after_split>p_before_split, '否' if p_good<p_not_good else'是')