#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np

class mapping:
    def __init__(self):
        ## read key
        self.dir = './mapping_ans_to_speech/mapping_folder/'
        file_r1 = open(self.dir+'key_room.txt','r')
        self.key_room = file_r1.read().split("\n")
        
        ## read ans with key        
        self.ans_room={}
        file_r2 = pd.read_csv(self.dir+'ans_room.csv').to_numpy()
        for w in file_r2:
            self.ans_room[w[0]]=w[1]
        
        
        ## read name other when call room                
        file_r3 = open(self.dir+'name_other.txt','r')
        self.name_other = file_r3.read().split("\n")

        
        ## read name other with key    
        file_r4 = pd.read_csv(self.dir+'key_name_other.csv').to_numpy()
        self.key_name_other={}
        for w in file_r4:
            self.key_name_other[w[0]]=w[1]
    
    
        ## read intent        
        file_r5 = pd.read_csv(self.dir+'target.csv').to_numpy()
        self.target = {}
        for w in file_r5:
            self.target[w[0]]=w[1]
            

        ## read key to room(for target)    
        
        file_r6 = pd.read_csv(self.dir+'key_to_room.csv').to_numpy()
        self.key_to_room={}
        for w in file_r6:
            self.key_to_room[w[0]]=w[1]
            
        file_r1.close()
#         file_r2.close()
        file_r3.close()
#         file_r4.close()
#         file_r5.close()
        
            
    def adding_name_room(self,key_, ans_):
        self.name_other.append(key_)
        self.key_name_other[key_]=ans
        file_a1 = open(self.dir+'name_other.txt','a+')
        file_a2 = open(self.dir+'key_name_other.csv','a+')
        file_h1 = open(self.dir+'history.txt','a+')
        file_h1.write(key_+","+ans+'\n')
        file_a1.write(key_+'\n')
        file_a2.write(key_+","+ans+'\n')
        file_a1.close()
        file_a2.close()
        file_h1.close()
        
        
    def adding_target_room(self, key_, ans_):
        self.target[key_]=ans
        file_a1 = open(self.dir+'target.csv','a+')
        file_a1.write(key_+","+ans)
        file_a1.close()
        
        
    def is_room(self, key_):
        for sub_room in self.name_other:
            if(key_== sub_room):
                return sub_room
        if (key_[0]=='A' or key_[0]=='B' or key_[0]=='a' or key_[0]=='b'):
            if(key_[1]>'0' and key_[1]<='9'):
                return '*####*'
        return '0'
    
    def target_room(self, key_): 
        max_pro = -1
        tar_name = ""
        key_list = list(self.target.keys()) 
        sub_word_key = key_.split(' ')
        for sub_tag in key_list:
            pro=-1
            for word in sub_word_key:
                if word in sub_tag:
                    pro+=1
            if pro==-1:
                continue
            if (pro/len(sub_tag)>max_pro):
                tar_name = sub_tag
                max_pro = pro/len(sub_tag)
        if(max_pro==-1):
            return "+=+","###"
        return tar_name,self.target[tar_name]
        
    ### return ans
        
    def return_key(self,key_):
        
        ans_final = []
        for sub_key in key_:
            if (sub_key==""):
                ans_final.append([""])
                continue
            check_room = self.is_room(sub_key) ### kiểm tra xem liệu key có phải là phòng hay tìm đến mục đích không?
            if (not check_room =='0'):
                if check_room =='*####*': ### kiểm tra xem liệu key có phải phòng học hay không? ví dụ: b105,a205
                    ans_final.append(["phòng" ,sub_key ,"nằm tại tầng" , sub_key[1] , "dãy nhà" , sub_key[0] , "tòa nhà học" ])
                    continue
                
                if self.key_name_other[check_room]== "PH02": ### kiểm tra xem liệu key có phải phòng học ở dãy nhà giảng đường hay không?
                    ans_final.append(["phòng" , check_room , "nằm tại tầng 1 dãy nhà giảng đường và hội trường"])
                    
                ans_final.append(["phòng" , check_room ,  self.ans_room[self.key_name_other[check_room]]]) ### trường hợp còn lại chỉ ra các bộ môn hoặc phòng ban
                continue
                
            target,key_tar = self.target_room(sub_key) ### trả về mục đích và key phòng của mục đích đó
            if(key_tar=="###"): ### trong trường hợp mục đích không có trong tập dữ liệu
                ans_final.append([""])
                continue
            ans_final.append(["bạn có thể  đến" , self.key_to_room[key_tar] , self.ans_room[key_tar]]) ### trả về  câu trả lời về phòng học chứa mục đích đó
        return ans_final
    # def print_(self):
    #     print(self.ans_room)