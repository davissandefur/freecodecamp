import numpy as np

def calculate(x):
    if len(x) < 9:
        raise ValueError('List must contain nine numbers')
    arr = np.array(x)
    arr= arr.reshape(3,3)
    mean = [np.mean(arr,axis=0).tolist(),np.mean(arr,axis=1).tolist(),np.mean(arr)]
    var=[np.var(arr,axis=0).tolist(),np.var(arr,axis=1).tolist(),np.var(arr)]
    sd=[np.std(arr,axis=0).tolist(),np.std(arr,axis=1).tolist(),np.std(arr)]
    maxi=[np.max(arr,axis=0).tolist(),np.max(arr,axis=1).tolist(),np.max(arr)]
    mini=[np.min(arr,axis=0).tolist(),np.min(arr,axis=1).tolist(),np.min(arr)]
    summ=[np.sum(arr,axis=0).tolist(),np.sum(arr,axis=1).tolist(),np.sum(arr)]
    calculations = {
        'mean':mean,
        'variance':var,
        'standard deviation':sd,
        'max':maxi,
        'min':mini,
        'sum':summ
    }
    return  calculations