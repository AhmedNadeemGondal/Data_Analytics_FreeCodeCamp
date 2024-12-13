import numpy as np

def calculate(list1):
    if len(list1)<9:
        raise ValueError("List must contain nine numbers.")
    data =np.array(list1)
    data = data.reshape((3,3))

    col_mean, row_mean, flat_mean = data.mean(axis=0),data.mean(axis=1),data.mean()
    mean_outp = {'mean': [list(col_mean),list(row_mean),float(flat_mean)]}

    col_var, row_var, flat_var = data.var(axis=0),data.var(axis=1),data.var()
    var_outp = {'variance': [list(col_var),list(row_var),float(flat_var)]}

    col_std, row_std, flat_std = data.std(axis=0),data.std(axis=1),data.std()
    std_outp = {'standard deviation': [list(col_std),list(row_std),float(flat_std)]}

    col_max, row_max, flat_max = data.max(axis=0),data.max(axis=1),data.max()
    max_outp = {'max': [list(col_max),list(row_max),int(flat_max)]}

    col_min, row_min, flat_min = data.min(axis=0),data.min(axis=1),data.min()
    min_outp = {'min': [list(col_min),list(row_min),float(flat_min)]}

    col_sum, row_sum, flat_sum = data.sum(axis=0),data.sum(axis=1),data.sum()
    sum_outp = {'sum': [list(col_sum),list(row_sum),float(flat_sum)]}

    output_dict = {**mean_outp,**var_outp,**std_outp,**max_outp,**min_outp,**sum_outp}

    return output_dict