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
# ## 1. plot

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


# ### (i). Multiple lines

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


# ### (ii). Subplot
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


# ## 2. Scatter plot
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


# 2/1/2026
# ## 3. Bar Chart - bar()

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])
plt.bar(x,y)
plt.show()


# In[2]:


plt.barh(x,y)
plt.show()


# In[4]:


plt.bar(x,y,color='darkblue',width=0.4)
plt.show()


# In[5]:


plt.barh(x,y,color='darkblue',width=0.4)
plt.show()


# In[7]:


plt.barh(x,y,color='darkblue',height=0.4)
plt.show()


# ## 4. Histogram
# - histogram is a graph showing frequency distribution.
# - it shows the number of observations within each given interval.
# 

# In[8]:


import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,1,2,3,3,3,3,4,4,5,7,8,8,9,10,10])
plt.hist(x)
plt.show()


# In[11]:


plt.hist(x,bins=5)
plt.show()


# In[14]:


plt.hist(x,orientation='horizontal')
plt.show()


# In[20]:


x=np.random.randint(1,100,size=(50))
print(x)
plt.hist(x,bins=[0,10,20,30,40,50,60,70,80,90,99])        
# bins only allowed incresing order it does not allow decrese in between increasing numbers or flow
plt.show()


# ## 5. Area plot

# In[23]:


x=range(1,6)
y=[1,4,6,8,4]
plt.fill_between(x,y)
plt.show()


# In[24]:


plt.fill_between(x,y,color='skyblue',alpha=0.5)
plt.show()


# In[26]:


plt.fill_between(x,y,color='skyblue',alpha=0.5)
plt.plot(x,y,color='blue',alpha=0.8)
plt.show()


# ### Area fill between two lines

# In[35]:


time=np.arange(12)
income=np.array([5,9,6,6,10,7,6,4,4,5,6,4])
expense=np.array([6,6,8,3,6,9,7,8,6,6,4,8])
plt.plot(time,income,color='green')
plt.plot(time,expense,color='red')
plt.fill_between(time,income,expense,where=(income>expense),color='green',alpha=0.25,label='positive',interpolate='True')
plt.fill_between(time,income,expense,where=(income<=expense),color='red',alpha=0.25,label='negative',interpolate='True')
plt.legend()
plt.show()


# In[39]:


# stacked area chart
x=range(1,6)
y1=[1,4,6,8,4]
y2=[2,2,7,10,12]
y3=[2,8,5,10,6]
plt.stackplot(x,y1,y2,y3,labels=['A','B','C'],colors=['blue','green','red'])
plt.legend(loc='upper left') #it shows or adjust the position of labels
plt.show()


# In[42]:


x=range(1,6)
y1=[2,2,2,2,2]
y2=[2,2,2,2,2]
y3=[2,2,2,2,2]
plt.stackplot(x,y1,y2,y3,colors=['yellow','red','black'])
plt.title("Germany")
plt.axis('off')
plt.show()


# ## 6. Pie Chart

# In[43]:


y=np.array([35,25,25,15])
plt.pie(y)
plt.show()


# In[45]:


y=np.array([35,25,25,15])
plt.pie(y,startangle=90)
plt.show()


# In[46]:


y=np.array([35,25,25,15])
mylabels=['Apple','Banana','Cherry','Dates']
plt.pie(y,labels=mylabels)
plt.show()


# In[57]:


y=np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
plt.pie(y,colors=['blue','white'])
plt.show()


# In[61]:


y=np.array([25,25,25,25])
mylabels=['Apple','Banana','Cherry','Dates']
myexplode=[0,0,0,0.2]
plt.pie(y,labels=mylabels,explode=myexplode)
plt.show()


# In[63]:


y=np.array([35,25,25,15])
mylabels=['Apple','Banana','Cherry','Dates']
myexplode=[0,0,0,0.2]
mycolors=['black','blue','yellow','brown']
plt.pie(y,labels=mylabels,explode=myexplode,colors=mycolors)
plt.show()


# In[67]:


y=np.array([35,25,25,15])
plt.figure(figsize=(10,10))
mylabels=['Apple','Banana','Cherry','Dates']
myexplode=[0,0,0,0.2]
mycolors=['green','blue','yellow','brown']
plt.pie(y,labels=mylabels,explode=myexplode,colors=mycolors)
plt.legend(title='Four Fruits')
plt.title("Pie chart")
plt.show()


# In[71]:


y=np.array([35,25,25,15])
mylabels=['Apple','Banana','Cherry','Dates']
myexplode=[0,0,0,0.2]
mycolors=['green','blue','yellow','brown']
plt.pie(y,labels=mylabels,explode=myexplode,colors=mycolors,radius=1)
plt.legend(title='Four Fruits')
plt.title("Pie chart")
plt.show()


# In[77]:


y=np.array([35,25,25,15])
plt.figure(figsize=(10,10))
mylabels=['Apple','Banana','Cherry','Dates']
myexplode=[0,0,0,0.2]
mycolors=['green','blue','yellow','brown']
plt.pie(y,labels=mylabels,explode=myexplode,colors=mycolors,radius=1,autopct="%1.1f%%")   
# in autopct 1.1 means after point there is only one digit allowed f means flot
plt.legend(title='Four Fruits',loc='upper right')
plt.title("Pie chart")
plt.show()


# In[125]:


plt.figure(figsize=(8,6))
x=['A']
y1=[2]
y4=np.array([1]*48)
plt.subplot(3,1,1)
plt.barh(x,y1,color='orange',height=10)
plt.axis('off')
plt.title("Indian Flag")
plt.subplot(3,1,2)
plt.pie(y4,colors=['blue','white'],radius=1.8)
plt.subplot(3,1,3)
plt.barh(x,y1,color='green',height=10)
plt.axis('off')

plt.show()


# 6/1/2026
# # Part-1 : UI Creation & Layout Fundamentals
# ### Task 1
# 

# In[10]:


%%writefile 1_hello.py
import streamlit as st
st.set_page_config(page_title='Hello Streamlit',page_icon='⚾',layout='wide')

st.title("Welcome to Streamlit")
st.header("This is header")
st.subheader("This is subheader")
st.text("st.text() is used for simple fixed width text.")
st.write("st.write() is more flexible and can display text,numbers,dataframe,etc.")
st.markdown("**st.markdown()** lets you use markdown for **rich text**")

code_example="""
def add(a,b):
    return a+b
result=add(5,7)
print(result)
"""

st.code(code_example,language='python')

# In[5]:


pwd


#  ### Task 2

# In[9]:


%%writefile 2_layout_basic.py                   
import streamlit as st
st.set_page_config(page_title='Faculty Profile',page_icon='👨‍🏫',layout='wide')

st.title("❄Faculty Profile Demo")
st.markdown("This example shows how to use **sidebar**,**columns** and **expanders**")

st.sidebar.header("Profile Settings")
faculty_name = st.sidebar.text_input("Faculty Name",'Tejas Thakkar')
department = st.sidebar.selectbox('Department',['CE','IT','CSE','ATML'])
experience = st.sidebar.slider('Years experience',0,40,10)
st.sidebar.markdown('---')
st.sidebar.write("You can put filters,toggles,etc in sidebar.")

col1,col2 = st.columns([1,2])

with col1:
    st.subheader("Basic info")
    st.write(f"**Name:** {faculty_name}")
    st.write(f"**Department:** {department}")
    st.write(f"**Experience:** {experience} years")

with col2:
    st.subheader("About")
    st.markdown("""
    User this area to show detailed information about the faculty member,such as research interest,publications and courses handled.""")
    
with st.expander("Show Courses Handled"):
    st.write(" Pyhton-1 ")
    st.write(" Pyhton-2 ")
    st.write(" Digital Electronics ")
    st.write(" PS ")

with st.expander("Show Publications"):
    st.write("1. Research Paper A (2024)")
    st.write("2. Research Paper B (2025)")

# # Part-2 : Input Widgets & Interactivity
# ## Text Inputs

# In[11]:


%%writefile 3_text_inputs.py
import streamlit as st

st.title("Text Input Demo")
name = st.text_input("Enter Your Name:")
comments = st.text_area("Any Comments or Feedback? ")

st.write("**Live Output**")
if name:
    st.write(f"Hello, **{name}** 👋")
if comments:
    st.write("Your Comments:")
    st.write(comments)

# # Number Inputs & Sliders

# In[13]:


%%writefile 4_number_inputs.py
import streamlit as st

st.title("Number Input & Slider Demo")

age = st.number_input("Enter your age:",min_value=0,max_value=100,value=25)
rating = st.slider("Rate this Session(1-10):",min_value=1,max_value=10,value=5)

st.write(f"**Your age is:** {age}")
st.write(f"**You Rated this Session:** {rating}/10")

# # Selection Widgets

# In[18]:


%%writefile 5_selection_widgets.py
import streamlit as st

st.title("Selection Widgets Demo")
course = st.selectbox("Select Course:",['Python-1','FSD-1','PS','DE'])
preferred_days = st.multiselect("Preferred Days for Extra Lectures:",
                               ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])

delivery_mode = st.radio("Preferred Delivery Mode:",
                         ['Offline','Online','Hybrid'])

subscribe = st.checkbox("Subscribe to Course updates?")

st.write("---")
st.write(f"**Course:** {course}")
st.write(f"**Preferred Days:** {','.join(preferred_days) if preferred_days else 'None'}")
st.write(f"**Delivery Mode:** {delivery_mode}")
st.write(f"**Subscribed:** {'Yes' if subscribe else 'No'}")

# In[ ]:




