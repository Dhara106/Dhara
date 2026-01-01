#!/usr/bin/env python
# coding: utf-8

# 23/12/2025
# # Chapter-10
# ## Visualization & Streamlit UI
# ### Matplotlib Library
# - plot, scatterplot, Bar chart, Area plot, Histogram, Pie chart with different parameters. (These are subplots which we have to make)
# - import matplotlib.pyplot as plt
# ### Basics of streamlit UI
# - creating a UI
# - I/P widgets
# - display O/Ps
# - streamlit with charts.

# 31/12/2025
# 1. plot

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,6])
y=np.array([0,250])
plt.plot(x,y)
plt.show()


# In[7]:


x=np.array([1,8])
y=np.array([3,10])
plt.plot(x,y,'o')      # it is called marker
plt.show()


# In[8]:


x=np.array([1,8])
y=np.array([3,10])
plt.plot(x,y,'*')      # it is called marker
plt.show()


# In[9]:


x=np.array([1,8])
y=np.array([3,10])
plt.plot(x,y,'v')      # it is called marker
plt.show()


# **Markers**
# 
# =============    ===============================
# 
# character        description
# 
# =============    ===============================
# 
# ``'.'``          point marker  
# 
# ``','``          pixel marker
# 
# ``'o'``          circle marker
# 
# ``'v'``          triangle_down marker
# 
# ``'^'``          triangle_up marker
# 
# ``'<'``          triangle_left marker
# 
# ``'>'``          triangle_right marker
# 
# ``'1'``          tri_down marker
# 
# ``'2'``          tri_up marker
# 
# ``'3'``          tri_left marker
# 
# ``'4'``          tri_right marker
# 
# ``'s'``          square marker
# 
# ``'p'``          pentagon marker
# 
# ``'*'``          star marker
# 
# ``'h'``          hexagon1 marker
# 
# ``'H'``          hexagon2 marker
# 
# ``'+'``          plus marker
# 
# ``'x'``          x marker
# 
# ``'D'``          diamond marker
# 
# ``'d'``          thin_diamond marker
# 
# ``'|'``          vline marker
# 
# ``'_'``          hline marker
# 
# =============    ===============================
# 
# 
# put cursor on plot and then click shift+tab and then clickon + sign and go down words you see these table and more.

# In[14]:


x=np.array([1,2,6,8])
y=np.array([3,8,1,10])
plt.plot(x,y,marker='h') 
plt.show()


# In[16]:


y=np.array([3,8,1,10])
plt.plot(y,marker='d')
plt.show()


# In[17]:


y=np.array([3,8,1,10])
plt.plot(y,'o:r')     # o --> marker ; : --> linestyle ; r --> color
plt.show()


# In[22]:


y=np.array([3,8,1,10])
plt.plot(y,'o-g')     
plt.show()


# In[23]:


y=np.array([3,8,1,10])
plt.plot(y,'o--b')     
plt.show()


# In[24]:


y=np.array([3,8,1,10])
plt.plot(y,'o-.y')     
plt.show()


# In[25]:


y=np.array([3,8,1,10])
plt.plot(y,marker='o',ms=50)         # ms = marker size     
plt.show()


# In[26]:


y=np.array([3,8,1,10])
plt.plot(y,marker='o',ms=29,mec='r')     # marker edge color = mec
plt.show()


# In[27]:


y=np.array([3,8,1,10])
plt.plot(y,marker='o',ms=10,mfc='y')     # marker face color = mfc
plt.show()


# In[28]:


y=np.array([3,8,1,10])
plt.plot(y,linestyle='dotted')   # ls is also allowed in place of linestyle & ':' this is also allowed in place of dotted  
plt.show()


# In[29]:


y=np.array([3,8,1,10])
plt.plot(y,ls=":",color='g')
plt.show()


# In[33]:


y=np.array([3,8,1,10])
plt.plot(y,ls="-",color='#4CAF50')
plt.show()


# In[32]:


y=np.array([3,8,1,10])
plt.plot(y,ls="--",color='darkblue')
plt.show()


# In[37]:


y=np.array([3,8,1,10])
plt.plot(y,ls=":",linewidth=20,color='purple')
plt.show()


# In[39]:


y=np.array([3,8,1,10])
plt.plot(y,ls="-.",linewidth=10,color='pink')
plt.show()


# (i). Multiple lines

# In[43]:


y1=np.array([3,8,1,10])
y2=np.array([6,2,7,11])
plt.plot(y1,marker='d',c='r',ls='-.')
plt.plot(y2,marker='h',c='b',ls='-.')
plt.show()


# In[53]:


x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])
plt.plot(x,y)
plt.title("Sports Watch Data",loc='left')
plt.xlabel("Average Pulse",loc='center')
plt.ylabel("Calorie Burnage",loc='bottom')
plt.show()


# In[60]:


x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])
font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':10}
plt.plot(x,y)

plt.title("Sports Watch Data",fontdict=font1)
plt.xlabel("Average Pulse",fontdict=font2)
plt.ylabel("Calorie Burnage",fontdict=font2)
plt.grid(c='g',ls='-')            # you can also write grid(axis='x') & grid(axis='y')
plt.show()


# ## Subplot
# - format(row,col,number)

# In[62]:


x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x1,y1)
plt.show()
x2=np.array([0,1,2,3])
y2=np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x2,y2)
plt.show()      # if we write show in every place then it does not go as per our need, as you see in these example


# In[63]:


x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x1,y1)
x2=np.array([0,1,2,3])
y2=np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x2,y2)
plt.show()


# In[72]:


x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])
plt.subplot(2,1,1)
plt.plot(x1,y1)
plt.title("Workout")
plt.xlabel("Days")
plt.ylabel("Number of exercise")
x2=np.array([0,1,2,3])
y2=np.array([10,20,30,40])
plt.subplot(2,1,2)
plt.plot(x2,y2)
plt.title("Marks")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.suptitle("Student info")
plt.tight_layout()    # it gives space between then texts so it does not overlap
plt.show()


# In[80]:


plt.figure(figsize=(10,8))
x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])
plt.subplot(2,3,1)
plt.plot(x1,y1,marker='o',ls=':',c='r')
plt.title("AB")
plt.xlabel("A")
plt.ylabel("B")
x2=np.array([3,8,1,10])
y2=np.array([0,1,2,3])
plt.subplot(2,3,2)
plt.plot(x2,y2,marker='*',ls='-',c='b')
plt.title("CD")
plt.xlabel("C")
plt.ylabel("D")
x3=np.array([2,4,6,8])
y3=np.array([1,3,5,7])
plt.subplot(2,3,3)
plt.plot(x3,y3,marker='H',ls='--',c='y')
plt.title("EF")
plt.xlabel("E")
plt.ylabel("F")
x4=np.array([6,10,29,10])
y4=np.array([5,10,15,20])
plt.subplot(2,3,4)
plt.plot(x4,y4,marker='D',ls='-.',c='g')
plt.title("GH")
plt.xlabel("G")
plt.ylabel("H")
x5=np.array([3,5,8,2])
y5=np.array([5,8,2,9])
plt.subplot(2,3,5)
plt.plot(x5,y5,marker='1',ls=':',c='orange')
plt.title("IJ")
plt.xlabel("I")
plt.ylabel("J")
x6=np.array([34,6,23,35])
y6=np.array([2,23,8,3])
plt.subplot(2,3,6)
plt.plot(x6,y6,marker='>',ls='-',c='pink')
plt.title("KL")
plt.xlabel("K")
plt.ylabel("L")
plt.suptitle('Alphabets')
plt.tight_layout()
plt.show()


# 2. Scatter plot
# 

# In[84]:


x=np.array([5,7,8,7,2,17,2,9,4,11])
y=np.array([99,86,87,88,111,86,103,87,94,78])
plt.scatter(x,y)
plt.show()


# In[100]:


x1=np.array([5,7,8,7,2,17,2,9,4,11])
y1=np.array([99,86,87,88,111,86,103,87,94,78])
plt.scatter(x1,y1,marker='*')
x2=np.array([5,1,2,3,2,5,3,2,8,4])
y2=np.array([99,100,150,110,80,130,140,90,125,115])
plt.scatter(x2,y2,marker='>')
plt.show()


# In[115]:


x=np.array([5,7,8,7,2,17,2,9,4,11])
y=np.array([99,86,87,88,111,86,103,87,94,78])
colors=np.array(['red','green','blue','yellow','pink','black','orange','purple','beige','brown'])
sizes=np.array([110,120,130,140,150,160,170,180,190,200])
plt.scatter(x,y,color=colors,s=sizes)
plt.show()


# In[108]:


x=np.array([5,7,8,7,2,17,2,9,4,11])
y=np.array([99,86,87,88,111,86,103,87,94,78])
colors=np.array([0,10,20,30,40,50,60,70,80,90])
plt.scatter(x,y,c=colors,cmap='dhurvi')
plt.colorbar()
plt.show()
# to see the color you have to get error first and in down side there is every color name was shown.


# In[116]:


x=np.array([5,7,8,7,2,17,2,9,4,11])
y=np.array([99,86,87,88,111,86,103,87,94,78])
colors=np.array([0,10,20,30,40,50,60,70,80,90])
size=np.array([45,20,15,25,5,30,35,40,29,10])
plt.scatter(x,y,c=colors,cmap='hot',s=size,alpha=0.5)
plt.colorbar()
plt.show()


# In[122]:


import matplotlib.pyplot as plt
import numpy as np
from numpy import random
x=10*np.array([random.randint(0,100,size=(50))])
# or x=10*np.randint(0,100,size=(50))
y=10*np.array([random.randint(0,100,size=(50))])
sizes2=10*np.array([random.randint(0,100,size=(50))])
colors=10*np.array([random.randint(0,100,size=(50))])
plt.scatter(x,y,c=colors,s=sizes2)
plt.show()


# In[ ]:




