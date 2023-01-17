import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df=pd.read_csv("dataset.csv")
# print(df)
# print(df.head(10))
# print(df.tail(10))

# # df.info()
# # print(df.shape)

# # print(df.describe())
# # print(df["Opposition"].describe())
# # print(df)
# # print(df["Runs"].value_counts())

# new_df=df[["Runs","4s","6s","Opposition"]]
# # print(new_df)
# # print(new_df.iloc[2:13]["Runs"])

# vs_aussies=df[df["Opposition"]=="v Australia"]
# print(vs_aussies.head(10))

# # print(vs_aussies["Runs"].sum())
# vs_centuries=vs_aussies[vs_aussies["Runs"]>=100]
# print(vs_centuries)

# vs_centuries=df[(df["Opposition"]=="v Australia") & (df["Runs"]>=100)]
# print(vs_centuries)

# def find_centuries(x):
#     if x>=100:
#         return "OG"
#     else:
#         return "NOOB"

# df["Centuries"]=df["Runs"].apply(find_centuries)
# print(df)


# find the total number of runs kohli
total_runs=df["Runs"].sum()
no_of_mathes=len(df["Runs"])

#Average of number of runs he has scored
# Average_runs=int(total_runs/no_of_mathes)
Average_runs=int(df["Runs"].mean())

#Number of mathes he has played at different position
position=df["Pos"]
print(position)
print(position.unique())
df["Pos"]=df["Pos"].map({
    3.0:"Bating at 3",
    4.0:"Bating at 4",
    1.0:"Bating at 1",
    2.0:"Bating at 2",
    5.0:"Bating at 5",
    6.0:"Bating at 6",
    7.0:"Bating at 7",
})
# print(df[["Runs","Pos","Opposition"]].head())

def show_pie_plot(df,key):
    counts=df[key].value_counts()
    counts_values=counts.values 
    count_labels=counts.index

    fig=plt.figure(figsize=(10,7))
    plt.pie(counts_values,labels=count_labels)
    plt.show()

# # Pos pie chart
# show_pie_plot(df,"Pos")

# # Opponent pie chart
# show_pie_plot(df,"Opposition")

# #Ground
# show_pie_plot(df,"Ground")
# #Dismissal
# show_pie_plot(df,"Dismissal")


#Total runs scored in different postions
runs_at_pos=df.groupby("Pos")["Runs"].sum()
runs_at_pos_values=runs_at_pos.values
runs_at_pos_labels=runs_at_pos.index

# fig=plt.figure(figsize=(10,7))
# plt.pie(runs_at_pos_values,labels=runs_at_pos_labels)
# plt.show()


# Total sixes scored with different oppositions
six_with_ops=df.groupby("Opposition")["6s"].sum()
six_with_ops_values=six_with_ops.values
six_with_ops_labels=six_with_ops.index

# fig=plt.figure(figsize=(10,7))
# plt.pie(six_with_ops_values,labels=six_with_ops_labels)
# plt.show()

#Number of centuries scored by kohli in first and second inning
centuries=df.query("Runs>=100")
print(centuries)

innings=centuries["Inns"]
tons=centuries["Runs"]

# fig=plt.figure(figsize=(10,7))
# plt.bar(innings,tons,color="blue",width=0.2)
# plt.show()


#Calculaten the dismissals of kohli
dismissals=df["Dismissal"].value_counts()
print(dismissals)

dismissals_counts=dismissals.values
dismissals_labels=dismissals.index
show_pie_plot(df,"Dismissal")

# fig=plt.figure(figsize=(10,7))
# plt.bar(
#     df["Opposition"],df["Runs"],color="red",width=0.1
# )
# plt.show()

# Against  which  
fig=plt.figure(figsize=(10,7))
plt.bar(
centuries["Opposition"],centuries["Runs"],color="red",width=0.1
)
plt.show()


