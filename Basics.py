#!/usr/bin/env python
# coding: utf-8

# Predicting The Chance Of Winning a Lottery

# The proeject is about developing a mobile app that can predict the possibility of winning the big prize of lottery. The purpose of this is to help prevent gambing addiction
# The app idea comes from a medical institute which is specialized in treating gambling addictions. The institute already has a team of engineers that will build the app, but they need us to create the logical core of the app and calculate probabilities. For the first version of the app, they want us to focus on the 6/49 lottery and build functions that can answer users the following questions:
# 
# What is the probability of winning the big prize with a single ticket?
# What is the probability of winning the big prize if we play 40 different tickets (or any other number)?
# What is the probability of having at least five (or four, or three) winning numbers on a single ticket?
# The scenario we're following throughout this project is fictional — the main purpose is to practice applying probability and combinatorics (permutations and combinations) concepts in a setting that simulates a real-world scenario.

# In[1]:


import pandas as pd
import numpy as np


# In[8]:


def factorial(n):
    fac = 1
    for i in range(n,0,-1):
        fac *= i
    return fac

def combinations(n,k):
    com = factorial(n) / factorial(k) / factorial(n-k)
    return com    


# In[9]:


def one_ticket_probability(number):
    total = combinations(49, 6)
    success = 1
    possibility = success / total
    perc = possibility * 100
    print('''your chance to win a big prize with number {} is {:.7f}%. which means you have 1 IN {:,} to win'''.format(number, perc, int(total)))
          


# In[10]:


input1 = [13,10,8,11,7,2]
one_ticket_probability(input1)


# In[11]:


print(combinations(49, 6))


# Historical Data About Canada Lottery
# 
# The institute also wants us to consider the data coming from the national 6/49 lottery game in Canada. The data set contains historical data for 3,665 drawings, dating from 1982 to 2018 (the data set can be downloaded from here).

# In[12]:


historical = pd.read_csv("649.csv")


# In[14]:


historical.shape


# We're going to begin by extracting all the winning numbers from the lottery data set. The extract_numbers() function will go over each row of the dataframe and extract the six winning numbers as a Python set.

# In[15]:


print(historical.head(3))


# In[16]:


print(historical.tail(3))


# In[18]:


def extract_numbers(data):
    data = data[4:10]
    data_set = set(data.values)
    return data_set

winning_numbers = historical.apply(extract_numbers, axis=1)
winning_numbers.head()
    
    


# Here I am writing a funtion named check_historical_occurence() that takes in two inputs: a Python list containing the user numbers and a pandas Series containing sets with the winning numbers (this is the Series you'll extract using the extract_numbers() function).

# In[26]:


def check_historical_occurrence(user_number, historical_number):
    user_number = set(user_number)
    check = (user_number == historical_number)
    n_occurence = check.sum()
    
    #need to print put a easy way for understanding
    
    if n_occurence == 0:
        print('''this combination {} has never occured, but this does not mean this won't happen, the possibility of this number drawn is 0.0000072%'''.format(user_number))
    
    else:
        print('''this combination {} has occured {} times in the past, the possibility of this number drawn in the future is 0.0000072%'''.format(user_number, n_occurence))


# In[27]:


test_input = [1, 8, 10, 25, 17, 32]

check_historical_occurrence(test_input, winning_numbers)


# In[29]:


test_input_2 = [34, 5, 14, 47, 21, 31]
check_historical_occurrence(test_input_2, winning_numbers)


# Multi-ticket Probability
# For the first version of the app, users should also be able to find the probability of winning if they play multiple different tickets. For instance, someone might intend to play 15 different tickets and they want to know the probability of winning the big prize.
# 
# The engineering team wants us to be aware of the following details when we're writing the function:
# 
# The user will input the number of different tickets they want to play (without inputting the specific combinations they intend to play).
# Our function will see an integer between 1 and 13,983,816 (the maximum number of different tickets).
# The function should print information about the probability of winning the big prize depending on the number of different tickets played

# In[30]:


def multi_ticket_probability(n):
    total = combinations(49, 6)
    success = n
    possibility = success / total
    perc = possibility * 100
    print('''if you decided to buy {} tickets, your chance to win a big prize will increase to {:.6f}%'''.format(n, perc))
          


# In[31]:


input = [1, 10, 100, 10000, 1000000, 6991908, 13983816]

for i in input:
    multi_ticket_probability(i)
    print('---------------------')


# These are the details we need to be aware of when we write a function to make the calculations of those probabilities possible:
# 
# Inside the app, the user inputs:
# six different numbers from 1 to 49; and
# an integer between 2 and 5 that represents the number of winning numbers expected
# Our function prints information about the probability of having a certain number of winning numbers
# To calculate the probabilities, we tell the engineering team that the specific combination on the ticket is irrelevant and we only need the integer between 2 and 5 representing the number of winning numbers expected. Consequently, we will write a function named probability_less_6() which takes in an integer and prints information about the chances of winning depending on the value of that integer.
# 
# The function below calculates the probability that a player's ticket matches exactly the given number of winning numbers. If the player wants to find out the probability of having five winning numbers, the function will return the probability of having five winning numbers exactly (no more and no less). The function will not return the probability of having at least five winning numbers.

# In[ ]:


def probability_less_6(n):
    total = combinations(49,6)
    success = combinations(6,n) * combinations((49-n),(6-n))
    possibility = success / total
    perc = possibility * 100
    print("if you want to win smaller prize by matching only {} of 6 numbers, your chance will rise to {:.6f}".format(n, ))

