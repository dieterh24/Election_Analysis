counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else: 
    print("El Paso is not in the list of counties")
for county in counties:
    print(county)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
counties_dict
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


         