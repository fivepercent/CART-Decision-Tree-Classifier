def calculateGini(data):
    num_total=data.shape[0]
    p_good=(data[data['好瓜']=='是'].shape[0])/num_total
    p_not_good=1-p_good
    return 1-np.square(p_good)-np.square(p_not_good)

def calculateGiniIndex_discrete(data, attribute):
    gini_index=0
    num_total=data.shape[0]
    for attr_value in data[attribute].unique():
        p_attr=data[data[attribute]==attr_value].shape[0]/num_total
        gini_attr=calculateGini(data[data[attribute]==attr_value])
        gini_index+=p_attr*gini_attr
    return gini_index

def calculateGiniIndex_continuous(data, attribute):
    attriList = np.array(data[attribute]).tolist()
    attriList.sort()
    TList=[]
    for i in range(len(attriList)-1):
        TList.append((attriList[i]+attriList[i+1])/2)
    giniIndex_min=1
    
    for Tn in TList:
        p_smaller=data[data[attribute]<=Tn].shape[0]/num_total
        p_larger=1-p_smaller
        gini_smaller=calculateGini(data[data[attribute]<=Tn])
        gini_larger=calculateGini(data[data[attribute]>Tn])
        cur_gini_index=p_smaller*gini_smaller+p_larger*gini_larger
        if(cur_gini_index<giniIndex_min):
            giniIndex_min=cur_gini_index
            T=Tn
    return (giniIndex_min, T)

def chooseAttributeForSplit(data):
    min_gini_index=1
    res=(None, None)
    for attribute in data.columns:
        if(attribute=='好瓜'):
            continue
        T=None
        if(type(data[attribute].iloc[0])==str):
            cur_gini_index=calculateGiniIndex_discrete(data, attribute)
        else:
            (cur_gini_index, T)=calculateGiniIndex_continuous(data, attribute)
        if(cur_gini_index<min_gini_index):
            res=(attribute, T)
            min_gini_index=cur_gini_index
    return res
def generate_Training_Test_Set(data, frac):
    data_test=data.sample(frac=frac)
    data_training=data[~data.index.isin(data_test.index)]
    return (data_training, data_test)

def calculateAccuracy(data):
    num_total=data.shape[0]
    if(num_total==0):
        return 0
    p_good=(data[data['好瓜']=='是'].shape[0])/num_total
    p_not_good=1-p_good
    return (p_good, p_not_good)



