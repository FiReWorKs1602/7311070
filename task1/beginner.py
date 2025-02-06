'''
step1
read context in txt file
extract and store countries in a list 
    - use a condition to ensure only unique countries are added to the list
    - e.g. if country not in list:
                list.append(country)

step 2
count players of each countries
- using loop and count (built in function) to find out the number of player

step 3
finding the largest number:
putting all number in a list 
then use max (built in function) to find the largest number

step 4
using loop and the largest number to find winner
(warn: you can't you index as it only returns teh position of first winner and there might be 2 winners)
'''


file = open("./task1/jump_to_distance.txt", "r")
data = file.read()
file.close()

# create list of countries
countries = []
for line in data.split("\n"):
    country = line.split()[1] # extract data
    if  country not in countries: # check wether the country is already in the list or not
        countries.append(country) # add country to the list
print(countries)

# count players of each country 
for country in countries: # looping the countries 
    player = data.count(country) # count the country name in the txt file context
    print(f"V {country} je {player} hracou!") 

# find the highest point within the players
numbers = []
for word in data.split(): # looping every word in txt file
    if word.isdigit(): # if word is number
        numbers.append(word) # then add to the list
largest_num = max(numbers) # using max to find the largest number

# print winner
for player in data.split("\n"): # looping each line of txt file
    if largest_num in player: # if current line contain the largest number 
        print(player.split()[0]) # print winner

