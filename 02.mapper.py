import sys

#iterate through the input lines
for line in sys.stdin:
    dataList = line.strip().split(",")
    if(len(dataList)==6):
        id,company,Product,Size,Currency,prices = dataList
      
        #print alcohol and time spent on study dail
        print(company,"\t",prices)


