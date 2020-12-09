with open("input.txt", "r") as fd:
    acc = 0
    eip = 0
    run_count = dict()
    lines = fd.readlines()
    instructions = list()

    #parse instructions
    for line in lines:
        parsed_line = line.split(' ')
        instructions.append( (parsed_line[0], int(parsed_line[1])) )

    while eip < len(instructions):
        if eip in run_count:
            #stop before running an instruction a second time
            print(acc)
            break
        else:
            run_count[eip] = 1
        
        if instructions[eip][0] == "acc":
            acc += instructions[eip][1]
            eip += 1
        elif instructions[eip][0] == "nop":
            eip += 1
        elif instructions[eip][0] == "jmp":
            eip += instructions[eip][1]
        else:
            print("Unrecognized instruction " + instructions[eip][0])
            break
