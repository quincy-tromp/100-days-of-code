import csv
import pandas

# file manipulation
with open("weather_data.csv") as f:
    raw_data = f.read()
data = raw_data.split("\n")
print(data)

# csv module
with open("weather_data.csv") as f:
    data = csv.reader(f)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# pandas module
data = pandas.read_csv("weather_data.csv")
# pandas DataFrame
print(data)
# Pandas Series (column)
print(data["temp"])
# Convert DataFrame to dictionary
print(data.to_dict())
# Convert Series to list 
print(data["temp"].to_list())
# Get the average temperature
print(data["temp"].mean())
# Get the maximum temperature
print(data["temp"].max())
# Get data in column using attribute
print(data.condition)
# Get data in row
print(data[data.day == "Monday"])
# Get data in row where temperature is at maximum
print(data[data.temp == data.temp.max()])
# Convert monday's temp from celsius to fahrenheit
monday_data = data[data.day == "Monday"]
new_temp = (monday_data.temp * (9/5)) + 32
print(new_temp)
# Create a DataFrame from scratch
data_dict = {
    "Students": ["Amy", "James", "Angela"],
    "Scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
# Convert DataFrame to CSV 
new_data.to_csv("notes.csv")

# Squirrel Count
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

my_table = data.groupby("Primary Fur Color").size()
gray_squirrel_count = int(my_table["Gray"])
cinnamon_squirrel_count = int(my_table["Cinnamon"])
black_squirrel_count = int(my_table["Black"])
# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")