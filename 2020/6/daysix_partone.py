with open("input.txt", "r") as fd:
    lines = fd.readlines()

    total_count = 0
    answered = set()

    for line in lines:

        if line == '\n':
            if len(answered) > 0:
                total_count += len(answered)
                answered = set()
            continue

        for c in line.strip():
            answered.add(c)

    print(total_count)

