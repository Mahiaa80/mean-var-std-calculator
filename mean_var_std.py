import numpy as np
def calculate(t):
  if len(t) != 9:
    raise ValueError("list must contain nine numbers")
  matrix = np.array(t).reshape((3,3))
  mean = [np.mean(matrix, axis=0), np.mean(matrix,axis=1), np.mean(matrix)]
  variance = [np.var(matrix, axis=0), np.var(matrix, axis=1), np.var(matrix)]
  std_dev = [np.std(matrix, axis=0), np.std(matrix,axis=1), np.std(matrix)]
  max_val = [np.max(matrix, axis=0), np.max(matrix, axis=1), np.max(matrix)]
  min_val = [np.min(matrix, axis=0), np.min(matrix, axis=1), np.min(matrix)]
  sum_val = [np.sum(matrix, axis=0), np.sum(matrix, axis=1), np.sum(matrix)]
  result = {
    'mean':mean,
    'variance':variance,
    'standard deviation': std_dev,
    'max':max_val,
    'min':min_val,
    'sum':sum_val
  }
  return result
  
