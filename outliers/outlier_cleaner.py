#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import numpy as np
    cleaned_data = []
    N=10/100
    ### my code goes here
    #(Y-truth-prediction)^2
    R2_Error=(predictions-net_worths)**2
    # sort on descending score
    sort_index = np.argsort(R2_Error, axis=0)
    #np.sort(R2_Error, axis=0)
    #combine data
    dataArray=np.concatenate((ages, net_worths,R2_Error), axis=1)
    data=list(map(tuple, dataArray))
# throw away the Nth percent from dada based on last Nth index
    d=round(N*len(R2_Error)) #elements need to be deleted
    l=len(R2_Error)
    IndexTo_remove=sort_index[l-d:].tolist()
    cleaned_data=np.delete(data,IndexTo_remove, axis=0)


    return cleaned_data


## loop to find N largest 
def Nmaxelements(list1, N): 
    final_list = [] 
  
    for i in range(0, N):  
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]; 
                  
        list1.remove(max1); 
        final_list.append(max1) 
          
    print(final_list) 