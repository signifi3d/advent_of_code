def fulfillsPasswordPolicy(lower_bound, upper_bound, constraint, password):
    
    constraint_count = 0
    
    for char in password:
        if char == constraint:
            constraint_count += 1
    
    return constraint_count >= lower_bound and constraint_count <= upper_bound

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

