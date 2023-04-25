#!/usr/bin/env python
# coding: utf-8

# In[1]:


# User inputs their name
name = input("Enter your name: ")

# User input their weight 
weight = int(input("Enter your weight in kilograms: "))

# User input their height
height = int(input("Enter your height in inches: "))

# Calculate user BMI
BMI = (weight * 703) / (height * height)
print("Your BMI is:", round(BMI,2))

if BMI>0:
    if(BMI) < 16:
        print(name + ",you are severely thin.")
    elif(BMI) <= 17:
        print("You are moderately thin.")
    elif(BMI) <= 18.5:
        print(name +", you are mildly thin.")
    elif(BMI) <= 25:
        print(name +", you are normal weight.")
    elif(BMI) <= 30:
        print(name +", you are overweight.")
    elif(BMI) <= 35:
        print(name +", you are obese class 1.")
    elif(BMI) <= 40:
        print(name +", you are obese class 2.")
    elif(BMI) > 40:
        print(name + ", you are obese class 3.")
    else:
        print("Enter valid inputs")


# In[ ]:




