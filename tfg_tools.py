import pandas as pd
import numpy as np

def data_nan_review_analysis(X,without_homa_vit_d = False,show_info_nan = False):
    """
    Function that takes as input a matrix with pats and features for one review, and gets back
    X_train_rev_imputed,pats_to_drop,feature_to_drop,imputation_data
    """
    
    feature_names = ['Age','Weight','Size','IMC','Creatinine','Cystatin','HDL','LDL','Triglyciredes','GOT','GPT','GGT','Albuminuria','Ferritin','HOMA','Insulin','Blood_Glucose','Glycated-HB','PCR','Vitamin-D','TAS','TAD','Date']
    
    df = pd.DataFrame(X,columns = feature_names[:-1]) #convert it to df #delete date [:-1]
    
    
    df = df.drop('Blood_Glucose',axis = 1)
    df = df.drop('Glycated-HB',axis = 1)
 
    
    if without_homa_vit_d:
        df = df.drop('HOMA',axis = 1)
        df = df.drop('Insulin',axis = 1) 
        df = df.drop('Vitamin-D',axis = 1)
    
    #print(df.columns)
    
    #initialize vars to return
    X_train_rev_imputed = []
    pats_to_drop = []
    feature_to_drop = []
    imputation_data = []
    #check number of NaNs per feature
    
    #use a boolean to allow to show
    if show_info_nan:
        
        for index,value in enumerate (df.isnull().sum()):
            if value !=0:
                print(df.columns[index],value)
            
    #Drop features: Blood_Glucose and Glycated_HB
    

    ##reemplazar cada valor por la mediana 
    
    X_train_rev_imputed = df.fillna(df.median()) 
    
    imputation_data = df.median()
    
    return X_train_rev_imputed,pats_to_drop,feature_to_drop,imputation_data

def imputing_data(X,num_reviews = 3,without_homa_vit_d = False):
    """ 
    Function that check data with nans and replace them with appropriate imputation
    """
    #X_train_aux = X_train.copy() #this is bad. 
    X_train_aux = X.copy()
    num_review = X_train_aux.shape[1]
    
    X_train_imp = []
    imput_data = []
    
    #run over the reviews and get the X_train_imputed, pats_to_drop, feature_to_drop, and imputation values
    for i in range(num_reviews):
        print("review",i)
        X_train_rev_imputed,pats_to_drop,feature_to_drop,imputation_data = data_nan_review_analysis(X_train_aux[:,i,:],without_homa_vit_d)

        
        X_train_imp.append(X_train_rev_imputed)
        imput_data.append(imputation_data)
        
    return X_train_imp,imput_data