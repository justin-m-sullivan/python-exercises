
# In[1]:


import json


# In[2]:


f = open('profiles.json')


# In[3]:


data = json.load(f)
# it seems I may need to set a variable = to the json file to access its elements using python...?


# In[4]:


# testing accessing list of dict elements in profiles.json as data
for i in data[0]['eyeColor']:
    print(i)


# In[5]:


#Checking type for key of "balance" in profiles.json as data
data[0]
type(data[0]['balance'])


# In[6]:


# open json file fully
json.load(open('profiles.json'))


# In[7]:


#1. Find the number of users:

def find_the_users(data):
    num_of_users = 0
    for dict in data:
        num_of_users += 1
    return num_of_users
find_the_users(data)    


# In[8]:


#2 Find the number of active users

def find_all_active_users(data):
    active_num_of_users = 0
    for user in data:
        if user['isActive'] == True:
            active_num_of_users += 1
    return active_num_of_users

find_all_active_users(data)
        


# In[9]:


#3 Find the number of inactive users:

def find_all_inactive_users(data):
    num_of_inactive_users = 0
    for user in data:
        if user['isActive'] == False:
            num_of_inactive_users += 1
    return num_of_inactive_users

find_all_inactive_users(data)


# In[10]:


#4 Find the sum for all users' balances
def list_of_balances(data):
    list_of_balances = []
    
    for user in data:
        list_of_balances.append(user['balance'])
    return list_of_balances


    


# In[11]:


#Convert the list of balances as strings to a list of balances as floats
def list_of_balances_converted(data):
    balances_list = list_of_balances(data)
    list_of_balances_converted = []
    
    for balance in balances_list:
        balance = balance.replace('$','')
        balance = balance.replace(',','')
        balance = (float(balance))
        list_of_balances_converted.append(balance)
     
   
    return list_of_balances_converted

list_of_balances_converted(data)


# In[12]:


#4 Find the sum for all users' balances
sum(list_of_balances_converted(data))


# In[13]:


#5. Find the average balance for all users: 
def avg_balance_for_all_users():
    avg_balance = round(sum(list_of_balances_converted(data)) / find_the_users(data), 2)
    return avg_balance

avg_balance_for_all_users()


# In[14]:


#6 - #7 Find the user with the highest balance
# First I return a list of all the balances:
def list_all_users_balances(data):
    list_of_balances = list_of_balances_converted(data)
    list_of_users = []
    for user in data:
        list_of_balances.append(user['balance'])
        list_of_users.append(user['name'])
        
    zipbObj = zip(list_of_balances, list_of_users)  
    dict_of_users_balances = dict(zipbObj)
    
    return dict_of_users_balances
            

list_all_users_balances(data)
       


# In[15]:


#6 Find the user with the lowest balance

def user_with_lowest_balance():
    return sorted(list_all_users_balances(data).items())[0]
        
user_with_lowest_balance()        


# In[16]:


#7 Find the user with highest balance
def user_with_highest_balance():
    
    return sorted(list_all_users_balances(data).items())[-1]

user_with_highest_balance()


# In[17]:


#8 thru # 9
# For finding the most common and least common favorite fruits 
def list_of_favorite_fruit(data):
    fruit_list = []
    
    for user in data:
        fruit_list.append(user['favoriteFruit'])
        
    return fruit_list

list_of_favorite_fruit(data)


# In[18]:


# 8. Find the most common favorite fruit
def favorite_fruit():
    fruit_list = list_of_favorite_fruit(data)
    return max(set(fruit_list), key=fruit_list.count)

favorite_fruit()
        


# In[19]:


# 9. Find the least most common favorite fruit
def not_favorite_fruit():
    fruit_list = list_of_favorite_fruit(data)
    return min(set(fruit_list), key=fruit_list.count)

not_favorite_fruit()


# In[20]:


# 10. Find the total number of unread messages for all users

def unread_messages_in_greeting(data):
    list_of_unread_messages = []
    
    for user in data:
        list_of_unread_messages.append(user['greeting'])
        
     
        
    return list_of_unread_messages
unread_messages_in_greeting(data)

def num_of_mess(messages):
    messages_count = []
    for n in range(len(messages)):
        for n in messages[n].split():
            if n.isdigit():
                messages_count.append(n)
    return messages_count
    
    
sum([int(i) for i in num_of_mess(unread_messages_in_greeting(data))])

