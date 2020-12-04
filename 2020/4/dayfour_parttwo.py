def validPassport(passport_data):
    valid_fields = ['byr', 'eyr', 'iyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in valid_fields:
        if field not in passport_data:
            return False
        elif not validField(field, passport_data[field]):
            return False
    return True

def validField(field_type, field_data):
    fieldValidators = { 'byr': lambda x : validYear(1920, 2002, x),
                        'iyr': lambda x : validYear(2010, 2020, x),
                        'eyr': lambda x : validYear(2020, 2030, x),
                        'hgt': lambda x : validHeight(x),
                        'hcl': lambda x : validHair(x),
                        'ecl': lambda x : validEye(x),
                        'pid': lambda x : validPid(x) }
    
    return fieldValidators[field_type](field_data)

def validYear(lower_bound, upper_bound, year):
    if len(year) != 4 or not year.isdigit():
        return False
    if int(year) < lower_bound or int(year) > upper_bound:
        return False
    return True

def validHeight(height):
    if height.endswith('cm'):
        if int(height[:-2]) >= 150 and int(height[:-2]) <= 193:
            return True
    elif height.endswith('in'):
        if int(height[:-2]) >= 59 and int(height[:-2]) <= 76:
            return True
    else:
        return False

def validHair(hair_color):
    return len(hair_color) == 7 and hair_color[0] == '#' and all(c in 'abcdef0123456789' for c in hair_color[1:])

def validEye(eye_color):
    return eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validPid(pid):
    return len(pid) == 9 and pid.isdigit()

with open("input.txt", "r") as fd:
    lines = fd.readlines()
    curr_passport = dict()
    valid_count = 0

    for line in lines:
        if line == '\n':
            if validPassport(curr_passport):
                valid_count += 1
            curr_passport = dict()
            continue
        else:
            line = line.strip().split(' ')
            for field in line:
                field = field.split(':')
                curr_passport[field[0]] = field[1]

    print(valid_count)
