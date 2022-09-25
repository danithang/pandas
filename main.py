# getting data from the weather_data file and placing it in a list
with open("weather_data.csv") as weather_file:
    data = weather_file.readlines()
    print(data)

# getting data from weather_data file with importing csv and using for loop to put each row in a list
import csv

with open("weather_data.csv") as weather_file:
    data = csv.reader(weather_file)
    # just getting the temp column of the data and excluding the word "temp" from printing
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# even easier way to get data from csv documents and get a single column
import pandas

data = pandas.read_csv("weather_data.csv")
# printing one column from the data table
print(data["temp"])

# another way to get temp column
print(data.temp)

# converting data into a dictionary
data_dict = data.to_dict()
print(data_dict)

# making temp column print as a list
temp_list = data["temp"].to_list()

# regular way to get average
average_regular = sum(temp_list) / len(temp_list)
print(average_regular)

# getting average of data with pandas
average = data["temp"].mean()
print(average)

max_value = data["temp"].max()
print(max_value)

# get data in rows
print(data[data.day == "Monday"])

# getting row that has max temp
print(data[data.temp == data.temp.max()])

# getting the condition of the row Monday
monday = data[data.day == "Monday"]
print(monday.condition)

# converting monday's temp from Celsius to fahrenheit...google the calculation
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_dictionary = pandas.DataFrame(data_dict)
# creating new csv file
data.to_csv("new_data.csv")

