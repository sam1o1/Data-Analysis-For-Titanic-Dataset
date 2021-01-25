#Importing libs
#####################################
import pandas as pd
import matplotlib.pyplot as plt
#####################################
df=pd.read_excel('titanic.xls')        # Reading dataset

print(df.head())                       # Printing the first 5 rows
print(df.shape)                        #printing the shape of the data how many colms and rows
print(df.columns)
print(df.info())                       #printing data info like nan values and so on
print(df.describe())                   #describing the data in terms of statistical features such as mean, max, std
df.drop(['fare','home.dest','name'],axis=1,inplace=True) #droping colms that are not effective
df['age']=df['age'].fillna(0)                            #filling in the nan values in Age colm with 0
df.hist(figsize=(20,15))                                 #printing descriptive figures of the data
plt.show()
#########################################################################################################
# Dealing with outliers
# the data we are dealing with does not have outliers so we will create some in order to understand with them in future
df_copy=df.copy()
df_copy['age'].iloc[0:10]=500
df_copy['age']=df_copy['age'].fillna(0)                            #filling in the nan values in Age colm with 0
df_copy.hist(figsize=(20,15))                                 #printing descriptive figures of the data
plt.show()
############################################################################################################
df_copy.drop(df_copy[df_copy['age']>100]['age'].index,inplace=True)
df_copy.hist(figsize=(20,15))                                 #printing descriptive figures of the data
plt.show()
############################################################################################################
print(df['sex'].value_counts())
print(df['sex'].unique())
male=df[df['sex']=='male']
male_survived=male[male['survived']==1]
print(df['sex'].value_counts())
print(df['sex'].unique())
female=df[df['sex']=='female']
female_survived=female[female['survived']==1]
print('the persentage of male survived is',(male_survived.shape[0]/male.shape[0])*100,'%')
print('the persentage of female survived is',(female_survived.shape[0]/female.shape[0])*100,'%')
##############################################################################################################
##############################_____Doing the same thing using for loop_____###################################
for gen in df['sex'].unique():
    df_gender=df[df['sex']==gen]
    survived=df_gender[df_gender['survived']==1]
    per_of_survived=(survived.shape[0]/df_gender.shape[0])*100
    print("___________")
    print('For',gen)
    print("The persentage of survived is ","%.2f"%per_of_survived,"%")
##############################################################################################################
##############################_____Doing the same thing for the class_____###################################
print(df['pclass'].unique())
for x in df['pclass'].unique():
    ppl_in_each_class=df[df['pclass']==x]
    survived_in_each_class=ppl_in_each_class[ppl_in_each_class['survived']==1]
    percentage=(survived_in_each_class.shape[0]/ppl_in_each_class.shape[0])*100
    print("___________")
    print('For class',x)
    print("The total number of people in this class is",ppl_in_each_class.shape[0])
    print("The total number of survived people in this class is", survived_in_each_class.shape[0])
    print("The persentage of survived is ","%.2f"%percentage,"%")
###################################################################################################################
df.to_csv('new.csv')
