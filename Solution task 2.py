data = {}

x = int(input("Enter the number of entries you want: "))


for y in range(x):
    key = input("Title: ")
    value = int(input("Days it was rented: "))
    data[key] = value

titles = list(data.keys())   
days = list(data.values())  
most_rented = max(data, key=data.get)
most_days = data[most_rented]
min_rented = min(data, key=data.get)
min_days = data[min_rented]
num_days = len(days)
sum_days = sum(days)
average = sum_days/num_days
unique = set(titles)
desc = sorted(titles, reverse=True)
print("Most borrowed book was: "+most_rented+" it was rented for:",most_days,"days")
print("Least borrowed book was: "+min_rented+" it was rented for:",min_days,"days")
print("The average days the books were rented:",average)
print("All of the unique titles: ",unique)
print("The list in descending order based on days rented: ",desc)
#Explantion video is in the readme file the first link!