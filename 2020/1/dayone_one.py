with open("input.txt", "r") as fd:
    nums = list()
    line = fd.readline()
    while line:
        num = int(line)
        diff = 2020 - num
        if diff in nums:
            print(str(diff) + " + " + str(num) + " = 2020")
            print(str(diff) + " * " + str(num) + " = " + str(diff*num))
            break
        else:
            nums.append(num)
        line = fd.readline()
