#https://geek-docs.com/pandas/pandas-read-write/pandas-to-read-and-write-excel.html
#读取某一列
import xlrd,pandas,re,numpy,os
#wb = xlrd.open_workbook("./输入的excel/1.xls")
excel_name=os.listdir("./输入的excel/")[0]
dada_needed=[]
data=pandas.read_excel("./输入的excel/"+excel_name,engine="openpyxl",keep_default_na=False)
data=data.iloc[:,2]
patt="139SPO1"
for i in data:
    if i!="":
        if re.match(patt,i)!=None:
            dada_needed.append(i)
            
#print(dada_needed)
df=pandas.DataFrame(dada_needed)
df.to_excel('./保存的excel/'+excel_name)  
        
   

