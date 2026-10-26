import pandas as pd

studentData = {
    "Student Name": ["Sadat", "Ishraq", "Labib", "Medha", "Safiqa"],
    "ID": ["23-52720-2", "23-55593-2", "23-54732-2", "23-58364-2", "23-55763-2"],
    "Marks": [85, 90, 73, 95, 60],
    "Max_mark": [100, 100, 100, 100, 100],
    "Min_mark": [30, 30, 30, 30, 30]
}

df = pd.DataFrame(studentData)

print("Show the table:")
print(df)

print("\nNumber of rows and column")
print(df.shape)

print("\nShow Datatypes:")
print(df.dtypes)

print("\nShow Dataset Structure:")
print(df.info)

print("\nStatistical Summary: ")
print(df.describe)

print("\nSorted Marks:")
print(df.sort_values("Marks"))
print("\n")
new_rows = pd.DataFrame({
    "Student Name": ["Mahi", "Sadaf"],
    "ID" : ["23-55521-2", "23-57498-2"],
    "Marks": [88,97],
    "Min_mark": [100, 100],
    "Max_mark": [30,30]
})

df = pd.concat([df, new_rows], ignore_index=True)
print(new_rows)


