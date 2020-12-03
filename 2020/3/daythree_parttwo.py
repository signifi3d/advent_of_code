def treeCount(slopes, right, down):
    curr_pos = 0
    tree_count = 0
    modulus = len(slopes[0])-1

    for i in range(0, len(slopes), down):
        if slopes[i][curr_pos] == '#':
            tree_count += 1
        curr_pos = (curr_pos + right) % modulus

    return tree_count

with open("input.txt", "r") as fd:
    slopes = fd.readlines()

    one = treeCount(slopes,1,1)
    two = treeCount(slopes,3,1)
    three = treeCount(slopes,5,1)
    four = treeCount(slopes,7,1)
    five = treeCount(slopes,1,2)

    print(str(one*two*three*four*five))


