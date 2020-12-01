with open("input.txt", "r") as fd:
    sums = dict()
    nums = list()
    line = fd.readline()
    while line:
        num = int(line)
        diff = 2020 - num
        if diff in sums:
            print(str(num) + " + " + str(sums[diff][0]) + " + " + str(sums[diff][1]) + " = 2020")
            print(str(num) + " * " + str(sums[diff][0]) + " * " + str(sums[diff][1]) + " = " + str(num*sums[diff][0]*sums[diff][1]))
        else:
            for i in nums:
                sums[num+i] = (num, i)
            nums.append(num)
        line = fd.readline()
