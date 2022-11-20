from altai_web.models import FailureMode
import csv, os
import pandas as pd

def run():
    path=os.path.join(os.getcwd(),"static/mine","failuremode.csv")
    info=pd.read_csv(path,sep=",")
    for i in range(len(info)):
        failuremode,check= FailureMode.objects.get_or_create(name=info.iloc[i]['name'],explanation=info.iloc[i]['explanation'],driver=info.iloc[i]['driver'],driver2=info.iloc[i]['driver2'],failuremodefamily=info.iloc[i]['failuremodefamily'])
        if not check:
            print(info.iloc[i]['name'] + ' already exist' )
        failuremode.save()

