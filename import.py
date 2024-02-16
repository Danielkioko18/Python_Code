import pandas as pd
import  numpy as np
import matplotlib as plt
import math

df=pd.read_excel(r'C:\Users\admin\Desktop\New folder\LITE.xlsx')
#print(df[""])
print("please enter the column you want to read")
read=str(input())
if(read=='1003 '):
    print(df["CRN"])
else:
    print("error")

