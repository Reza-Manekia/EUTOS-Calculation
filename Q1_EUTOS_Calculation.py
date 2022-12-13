#!/usr/bin/env python
# coding: utf-8

# In[1]:


def EUTOS(a, b):
    while True:
        if a <= 25 and b <= 40:
            patient_score = 7*a + 4*b
            return patient_score
            break
        elif a > 25:
            print("Basophil percentage out of range")
            basophil = int(input("Enter basophil percentage(Range: 0-25): "))
        
        elif b > 40:
            print("spleen size out of range")
            spleen_size = int(input("Enter spleen size(Range: 0-40): "))


basophil = int(input("Enter basophil percentage(Range: 0-25): "))
spleen_size = int(input("Enter spleen size(Range: 0-40): "))

result = EUTOS(basophil, spleen_size)
if result > 87:
    print("High Risk")
    print("Patient score is ", str(result))
    
else:
    print("Low Risk")
    print("Patient score is ", str(result))


# In[ ]:




