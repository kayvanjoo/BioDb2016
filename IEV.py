
# coding: utf-8

# In[ ]:

#IEV


p_list = [1, 1, 1, 0.75, 0.5, 0]

EV_list =[]

s= [16004, 17607, 19339, 17359, 19249, 19340]

for index, num_parents in enumerate(s):

    EV_list.append(2*int(num_parents)*p_list[index])


print (sum(EV_list))

