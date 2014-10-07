# import the file
# open the file
# read the file
# for loop to read each line
# create dictionary w/ restaurnt as key and rating as value
# use sorted method

from sys import argv

script, filename = argv

opened_file = open(filename)

# dictionary = {}

for line in opened_file:
    words = line.split(":")
    restaurant_name = words[0]
    restaurant_score = words[1]
    print restaurant_name restaurant_score
    
    # for name, score in zip(restaurant_name, restaurant_score):
        # print "Restaurant {0} is rated at {1}.".format(name, score)


# print dictionary




