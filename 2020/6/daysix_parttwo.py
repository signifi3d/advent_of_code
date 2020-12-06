with open("input.txt", "r") as fd:
    lines = fd.readlines()

    total_count = 0
    answered = dict()
    group_size = 0

    for line in lines:

        if line == '\n':
            if len(answered) > 0:
                for key in answered:
                    if answered[key] == group_size:
                        total_count += 1
                answered = dict()
                group_size = 0
            continue

        group_size += 1

        for c in line.strip():
            if c in answered:
                answered[c] += 1
            else:
                answered[c] = 1

    print(total_count)

