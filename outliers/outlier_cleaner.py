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
    error=np.ndarray
    error=abs(predictions-net_worths)


    Data=np.ndarray
    Data=np.zeros((len(error),3))
    Data[:,0] = error.transpose()
    Data[:,1] = ages.transpose()
    Data[:,2] = net_worths.transpose()

    Data = Data[Data[:, 0].argsort()]

    cleaned_data=np.zeros((len(error)-10,3))
    cleaned_data[:,0]=Data[0:len(error)-10,1]
    cleaned_data[:,1]=Data[0:len(error)-10,2]
    cleaned_data[:,2]=Data[0:len(error)-10,0]
    #cleaned_data = []

    ### your code goes here

    
    return cleaned_data

