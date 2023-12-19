import pandas as pd


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
    
    
    
    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["mean","median","mode","Q1:25th","Q2:50th",
                                    "Q3:75th","99th","Q4:100th","IQR","min","max",
                                    "lower whister","upper whister","skewness","kurtosis"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["mean"]=dataset[columnName].mean()
            descriptive[columnName]["median"]=dataset[columnName].median()
            descriptive[columnName]["mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25th"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50th"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75th"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99th"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100th"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75th"]-descriptive[columnName]["Q1:25th"]
            descriptive[columnName]["min"]=dataset.describe()[columnName]["min"]
            descriptive[columnName]["max"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["lower whister"]=descriptive[columnName]["Q1:25th"]-(1.5*descriptive[columnName]["IQR"])
            descriptive[columnName]["upper whister"]=descriptive[columnName]["Q3:75th"]+(1.5*descriptive[columnName]["IQR"])
            descriptive[columnName]["skewness"]=dataset[columnName].skew()
            descriptive[columnName]["kurtosis"]=dataset[columnName].kurtosis()
            descriptive[columnName]["var"]=dataset[columnName].var()
            descriptive[columnName]["std"]=dataset[columnName].std()
        return descriptive



    def Outliers():
        L_outliers=[]
        G_outliers=[]
        for columnName in quan:
            if(descriptive[columnName]["min"]<descriptive[columnName]["lower whister"]):
                L_outliers.append(columnName)
            if(descriptive[columnName]["max"]>descriptive[columnName]["upper whister"]):
                G_outliers.append(columnName)
        return L_outliers,G_outliers

    
    
    def replace():
        for columnName in L_outliers:
            dataset[columnName][dataset[columnName]<descriptive[columnName]["lower whister"]]=descriptive[columnName]["lower whister"]
        for columnName in G_outliers:
            dataset[columnName][dataset[columnName]>descriptive[columnName]["upper whister"]]=descriptive[columnName]["upper whister"]

            
    def freqtable(columnName,dataset):
        freqtable=pd.DataFrame(columns=["Marks","Frequency","Relative_Frequency","Cumsum"])
        freqtable["Marks"]=dataset[columnName].value_counts().index
        freqtable["Frequency"]=dataset[columnName].value_counts().values
        freqtable["Relative_Frequency"]=freqtable["Frequency"]/103
        freqtable["Cumsum"]=dataset[columnName].cumsum()
        return freqtable
