#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Libraries
import os
import csv


# In[3]:


# Input and Output files
input_file = 'election_data.csv'
output_file = 'election_data_summary.txt'


# In[4]:


# Input and Output paths
csvfile = os.path.join('Resources', 'election_data.csv')
txtfile = os.path.join('election_data_summary.txt')


# In[5]:


total_votes = 0
names = []
candidates = {}
percent_votes = 0
most_votes = 0
most_voted = ""


# In[6]:


file = open(csvfile)

csvreader = csv.reader(file)

header = next(csvreader)
print(header)


# In[7]:


for row in csvreader:
    #print(row)
    total_votes = total_votes + 1
    if row[2] not in names:
        names.append(row[2])
        candidates[row[2]] = 0
    candidates[row[2]] = candidates[row[2]] + 1
    
    percent_votes = candidates[row[2]]/ total_votes
    
    if candidates[row[2]] > most_votes:
        most_votes = candidates[row[2]]
        most_voted = row[2]


# In[8]:


print(f'Total Number Votes Cast: {total_votes}')


# In[9]:


print(f'Total Number Votes per Candidate: {names}')


# In[10]:


print(f'Candidate Who Receive Votes: {candidates}')


# In[11]:


khan_percentage = round(candidates ["Khan"] / total_votes *100,2)


# In[12]:


correy_percentage = round(candidates ["Correy"] / total_votes *100,2)


# In[13]:


li_percentage = round(candidates ["Li"] / total_votes *100,2)


# In[14]:


otooley_percentage = round(candidates ["O'Tooley"] / total_votes *100,2)


# In[15]:


print(f'Winner of Election: {most_voted}')


# In[16]:


with open(txtfile,'w', newline='') as summary_txt:
    writer = csv.writer(summary_txt)
    
    writer.writerows([["Election Results for:" + input_file],
        ["-" *50],
        ["Total Votes:" + str(total_votes)],
        ["-" *50],             
        ["Khan:" + str(khan_percentage), + (candidates["Khan"])],
        ["Correy:" + str(correy_percentage), + (candidates["Correy"])],
        ["Li:" + str(li_percentage), + (candidates["Li"])],
        ["O'Tooley:" + str(otooley_percentage), + (candidates["O'Tooley"])],
        ["-" *50],
        ["Winner:" + str(most_voted)]])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




