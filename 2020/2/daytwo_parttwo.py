def fulfillsPasswordPolicy(first_pos, second_pos, constraint, password):
    return (password[first_pos-1] == constraint) ^ (password[second_pos-1] == constraint)

with open("input.txt", "r") as fd:
    valid_pw_count = 0

    for line in fd.readlines():
        line = line.split(':')
        password = line[1].strip()
        policy = line[0].split(' ')
        constraint = policy[1].strip()
        bounds = policy[0].split('-')
        valid_pw_count += fulfillsPasswordPolicy(int(bounds[0]), int(bounds[1]), constraint, password)

    print(str(valid_pw_count) + " valid passwords are present.")

