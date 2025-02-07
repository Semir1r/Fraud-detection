from sklearn.preprocessing import LabelEncoder

def encodingCategoricalVariables(dataframe):
    categorical_columns = ['device_id','source','browser','country']
    encoder = LabelEncoder()
    for col in categorical_columns:
        dataframe[col + '_encoded'] = encoder.fit_transform(dataframe[col])
    dataframe.drop(columns=categorical_columns, inplace=True)
    
    return dataframe