def outliers(df):
    import numpy as np
    import pandas as pd
    
    for i,ind in zip(range(df.shape[1]),list(df.columns)):
        lwr_bound,upr_bound = detect_outliers_iqr(df[ind])
        df[ind] = np.where(df[ind]>upr_bound, upr_bound, df[ind])
        df[ind] = np.where(df[ind]<lwr_bound, lwr_bound, df[ind])
    
def detect_outliers_iqr(data):
    data = sorted(data)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    # print(q1, q3)
    IQR = q3-q1
    print(q3,q1,IQR)
    lwr_bound = q1-(1.5*IQR)
    upr_bound = q3+(1.5*IQR)
    return lwr_bound, upr_bound
    
   # for i,ind in zip(range(13),list(data.feature_names)):
   # sample_outliers_i = detect_outliers_iqr(df[ind])
   # print(ind," - Outliers from IQR method: ", sample_outliers_i,"\n")
   
  # for ind in list(data.feature_names):
  # globals()["sample_outliers_"+str(ind)] = detect_outliers_iqr(df[ind])
  # print(ind," - Outliers from IQR method: ", globals()["sample_outliers_"+str(ind)],"\n")
  
