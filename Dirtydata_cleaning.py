import pandas as pd
data = pd.read_csv("dirty.csv")

#standardizing column names
data.columns = data.columns.str.strip().str.lower() 
 # Remove leading/trailing spaces from column names.
print(data.head())
data.info()
  #cleaning spaces and converting to correct data types  
data["name"] = data["name"].astype(str).str.strip().str.upper()
data["marks"]=data["marks"].astype(str).str.strip()
data["marks"]=pd.to_numeric(data["marks"],errors="coerce")
data["city"]= data["city"].astype(str).str.strip().str.title()

#filling missing values with mean
data["marks"]=data["marks"].fillna(data["marks"].mean())

#creating a new column "Result" based on marks
data["result"]= data["marks"].apply(lambda x: "Pass" if x>=50 else "Fail")

#removing duplicates
data.drop_duplicates(inplace=True)
print("Data after cleaning:\n",data)

#Average marks
print("Average marks:", data["marks"].mean())

#Top scorer details
top_scorer = data.loc[data["marks"].idxmax()]
print("Top_scorer_name:",top_scorer["name"])
print("Top_scorer_marks:",top_scorer["marks"])
print("Top_scorer_city:",top_scorer["city"])

#Sorting data by marks in descending order
data = data.sort_values(by="marks", ascending=False)

print("Final cleaned data:\n",data)

#visualization
data.groupby("city")["marks"].mean().plot(kind="bar")
plt.title("Average marks by city")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.show()

#missing values count
print("\nMissing values:\n", data.isnull().sum())

# Group analysis
print("\nAverage marks by city:\n", data.groupby("city")["marks"].mean())
