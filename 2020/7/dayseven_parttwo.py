bag_specs = dict()

def bagCount(curr_bag):
    if len(bag_specs[curr_bag]) == 0:
        return 0;

    count = 0
    for bag in bag_specs[curr_bag]:
        count += bag[1] + bag[1] * bagCount(bag[0])

    return count

with open("input.txt", "r") as fd:
    possible_bag_count = 0

    lines = fd.readlines()

    for line in lines:
        #split the bag containing other bags from the bags it contains
        bags = line.split("contain")
        #slice up to the word bags to get the type of container bag
        container_bag = bags[0][:bags[0].find(" bags")]

        bag_specs[container_bag] = list()

        if "no other bags" in bags[1]:
            continue

        contained_bags = bags[1].split(',')

        for bag in contained_bags:
            #2 because there's a preceding white space and the number of bags is separated by another space
            bag = bag.split(' ', 2)
            #add bag to the list of contained bags as a tuple with the bag name and bag amount
            bag_specs[container_bag].append( (bag[2][:bag[2].find(" bag")], int(bag[1])) )

    print(bagCount("shiny gold"))



