def validPassport(passport_data):
    valid_fields = ['byr', 'eyr', 'iyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in valid_fields:
        if field not in passport_data:
            return False
    return True

with open("input.txt", "r") as fd:
    lines = fd.readlines()
    curr_passport = ''
    valid_count = 0

    for line in lines:
        if line == '\n':
            if validPassport(curr_passport):
                valid_count += 1
            curr_passport = ''
            continue
        else:
            curr_passport += line.strip()

    print(valid_count)
