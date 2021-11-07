import pandas

df1 = pandas.DataFrame([[2,4,6],[3,4,5]],columns=["age","money","value"],index=["first","second"])
df2 = pandas.DataFrame([{"Name":"Nimritee","LastName":"Sirsalewala"},{"Name":"Divya"}])
df3 = pandas.DataFrame([[2,3,4],[4,5,6]],columns=["name","age","value"])
df3.mean()
print(df3.age)
print(df3.value.max())
print(df1)