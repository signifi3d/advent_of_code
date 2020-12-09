def findFirstInvalid(stream):
    for index in range(25, len(stream)):
        for i in range(index-25, index):
            if (stream[index]-stream[i]) in stream[i+1:index]:
                break
        else:
            return stream[index]

def findWeakness(stream, invalid):
    for i in range(len(stream)):
        for j in range(i+2, len(stream)+1):
            slice_sum = sum(stream[i:j])
            if slice_sum == invalid:
                return min(stream[i:j]) + max(stream[i:j])
            elif slice_sum > invalid:
                break
    return 0
            

with open("input.txt", "r") as fd:
    stream = [int(x) for x in fd.readlines() if x != '\n']
    invalid = findFirstInvalid(stream)
    weakness = findWeakness(stream, invalid)

    print(invalid)
    print(weakness)

    
