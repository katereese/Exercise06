# import the file
# open the file
# read the file
# for loop to read each line
# create dictionary w/ restaurnt as key and rating as value
# use sorted method

from sys import argv

script, filename = argv

def read_file(filename):
	opened_file = open(filename)
	rest_dict = {}

	for line in opened_file:
		line = line.rstrip()
		words = line.split(":")
		restaurant_name = words[0]
		restaurant_score = words[1]

		rest_dict[restaurant_name] = restaurant_score

	for restaurant_name in sorted (rest_dict):
		print "Restaurant %s is rated at %s." % (restaurant_name, rest_dict[restaurant_name])
		
# print str(sorted(rest_list))
# print "Restaurant {0} is rated at {1}.".format(name, score)

def print_ratings(rest_dict):

	for i in sorted(rest_dict.keys()):
	   print 'Restaurant %s is rated %s.' % (i, rest_dict[i])

def main():

	rest_dict = read_file(filename)
	print_ratings(rest_dict)

if __name__ == '__main__':
	main()
