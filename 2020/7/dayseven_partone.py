bag_specs = dict()

#dict for memoization
known_container = dict()

def canContain(curr_container, search_bag):
    if len(bag_specs[curr_container]) == 0:
        known_container[curr_container] = False
        return False

    #check if search_bag is one of the possible contained bags or already known to contain
    for bag in bag_specs[curr_container]:
        if bag[0] == search_bag:
            return True
        if bag[0] in known_container:
            if known_container[bag[0]]:
                return True

    #recurse on possible contained bags to see if they can contain search_bag
    for bag in bag_specs[curr_container]:
        if canContain(bag[0], search_bag):
            return True
    
    known_container[curr_container] = False
    return False

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
            bag_specs[container_bag].append( (bag[2][:bag[2].find(" bag")], bag[1]) )

    for bag in bag_specs:
        if canContain(bag, "shiny gold"):
            possible_bag_count += 1

    print(possible_bag_count)



