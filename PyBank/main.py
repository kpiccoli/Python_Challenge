#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
import os
import csv


# In[2]:


# input and output files
input_file = 'budget_data.csv'
output_file = 'budget_data_summary.txt'


# In[3]:


# input and output paths
csvfile = os.path.join('Resources','budget_data.csv')
txtfile = os.path.join('budget_data_summary.txt')


# In[4]:


total_months = 0
profit_losses = 0
change_list = []
month_of_change = []
greatest_increase = ["",0]
greatest_decrease = ["",0]


# In[5]:


# Open file to read
with open (csvfile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csvheader=next(csvreader)
    
    print(f"Header: {csvheader}")
    
    # Jan-2010 , 864000
    first_row = next(csvreader)
    print(f'First Row: {first_row}')
    total_months = total_months + 1
    profit_losses = profit_losses + int(first_row[1])
    first_value = int(first_row[1])
    
    for row in csvreader:
        print(row)
        total_months = total_months + 1 
        profit_losses = profit_losses + int(row[1])
        
        net_change = int(row[1]) - first_value
        change_list = change_list + [net_change]
        #change_list.append(net_change)
        
        if net_change > greatest_increase[1]:
            greatest_increase[1] = net_change
            greatest_increase[0] = row[0]   
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[1] = net_change
            greatest_decrease[0] = row[0]
      


# In[6]:


print(f'Total Months: {total_months}')
print(f'Profit/Losses: ${profit_losses}')


# In[7]:


average_change = round(profit_losses / total_months, 2)
print(f'Average Change: {average_change}')


# In[8]:


print(f'Greatest Increase: {greatest_increase} ')
print(f'Greatest Decrease: {greatest_decrease} ')


# In[9]:


with open(txtfile,'w', newline='') as summary_txt:
    writer = csv.writer(summary_txt)
       
    writer.writerows([["Financial Analysis for:" + input_file],
        ["-" *50],
        ["Total Months:" + str(total_months)],
        ["Total Profit/Losses:"  + str(profit_losses)],
        ["Average Change in Profit/Losses:" + str(average_change)],
        ["Greatest Increase in Profits:" + str(greatest_increase)],
        ["Greatest Decrease in Profits:" + str(greatest_decrease)]])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




