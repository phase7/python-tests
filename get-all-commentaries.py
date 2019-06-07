#!/usr/bin/env python
# coding: utf-8

# ## Create api

# In[26]:


import requests
import json
import os
import io
db_folder_path = '/media/p7/4C1C42351C4219FA/WD/from-github/python-tests/notebook/commentary-project/commentaries1'
match_id = 1144491
innings = [1,2]

os.chdir(db_folder_path)

for innings in innings:
    innings_dir_name = "innings0"+str(innings)
    os.mkdir(innings_dir_name)
    os.chdir(innings_dir_name)
    j=1 #start/restart with a non-zero number
    while(j):
        apistr = 'http://site.web.api.espn.com/apis/site/v2/sports/cricket/5/playbyplay?contentorigin=espn&event='+ str(match_id) +'&page=' + str(j) + '&period='+str(innings)+'&section=cricinfo'
        r = requests.get(apistr)
        data = r.json()
        items = data["commentary"]["items"]
        if  len(items) == 0:
            j = 0
            os.chdir("..")
            continue
        #my work goes here--------------------------
        with io.open("comm_part"+str(j)+".json", "w") as file:
            json.dump(data,file)
            
        j += 1
        

