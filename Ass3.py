



#Plotting Bar Chart

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("C:\\Users\\omini jadhav\\Desktop\\States.csv")
print(df)

#Plotting a bar chart
plt.bar(x=df['States'],height=df['Population( in Lakhs)'],color=['red','green'])
plt.xticks(rotation=45)

#naming x-axis , y-axis and title
plt.xlabel('States')
plt.ylabel('Population in lakhs')
plt.title("Population of Districts in maharshtra")






#Plotting Pie Chart

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("C:\\Users\\omini jadhav\\Desktop\\States.csv")
print(df)
state_data=df["States"]
population=df["Population( in Lakhs)"]
colors=['red','blue','#8c564b','white','yellow','pink','violet','gray','#ff7f0e','orange','pink']
explode=(0,0,0.1,0,0.1,0,0.1,0,0,0,0)

#plotting Pie Chart
plt.pie(population,labels=state_data,colors=colors,startangle=140,shadow=True,explode=explode,radius=2.4,autopct='%1.1f%%')

plt.legend()

#Showing a pie chart
plt.show()




#Plotting with Seaborn

import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:\\Users\\omini jadhav\\Desktop\\States.csv")
print(df)
x=df["States"]
y=df["Population( in Lakhs)"]

#Plotting strip plot with seaborn
ax=sns.stripplot(x,y);

#giving label to x-axis and y=axis and title
ax.set(xlabel='States',ylabel='Population in lakhs')
plt.title("Population of Districts in maharshtra")
plt.xticks(rotation=45)
#Show plot
plt.show()

   
