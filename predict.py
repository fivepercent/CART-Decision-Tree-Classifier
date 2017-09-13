dt=DecisionTree(data)
test_sample_1={'色泽':'青绿','根蒂':'蜷缩','敲声':'浊响','纹理':'清晰','脐部':'凹陷','触感':'硬滑','密度':0.697,'含糖率':0.460}
print('是否为好瓜: '+ dt.predict(test_sample_1))