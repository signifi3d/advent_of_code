def execute(instructions):
    acc = 0
    eip = 0
    run_count = dict()

    while eip < len(instructions):
        if eip in run_count:
            #stop before running an instruction a second time
            return False
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
            return False

    return acc

with open("input.txt", "r") as fd:
    lines = fd.readlines()
    instructions = list()

    #parse instructions
    for line in lines:
        parsed_line = line.split(' ')
        instructions.append( [parsed_line[0], int(parsed_line[1])] )

    for addr in range(len(instructions)):
        if instructions[addr][0] == 'jmp':
            instructions[addr][0] = 'nop'
            res = execute(instructions)
            if res:
                print(res)
                break
            else:
                instructions[addr][0] = 'jmp'
        elif instructions[addr][0] == 'nop':
            instructions[addr][0] = 'jmp'
            res = execute(instructions)
            if res:
                print(res)
                break
            else:
                instructions[addr][0] = 'nop'

