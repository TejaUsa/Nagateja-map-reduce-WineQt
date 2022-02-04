import sys

#iterate through the input lines
for line in sys.stdin:
    dataList = line.strip().split(",")
    if(len(dataList)==17):
       InvoiceID,Branch,City,Customertype,Gender,Productline,Unitprice,Quantity,Tax,Total,Date,Time,Payment,cogs,grossmarginpercentage,grossincome,Rating = dataList
      
        #print alcohol and time spent on study daily
print(City,"\t",1)


