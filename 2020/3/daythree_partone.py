with open("input.txt", "r") as fd:
    line = fd.readline().strip()
    modulus = len(line)
    tree_count = 0
    curr_pos = 3

    line = fd.readline().strip()
    while line:
        if line[curr_pos] == '#':
            tree_count += 1
        curr_pos = (curr_pos + 3) % modulus
        line = fd.readline().strip()

    print(tree_count)

