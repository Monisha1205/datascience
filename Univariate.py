class Univariate():
    
    
    def Quanqual(dataset):
        qual=[]
        quan=[]
        for columnName in dataset.columns:
            if (dataset[columnName].dtypes=="O"):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return qual,quan
    
    
    