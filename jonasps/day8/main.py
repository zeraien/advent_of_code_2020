
#part 1 and 2
class Interpreter:
    def __init__(self, code):
        self.line_numbers_visited = []
        self.accumulator = 0
        self.line_number = 0
        self.done = False
        self.code = code
        self.code_lines = len(code) -1

    def acc(self, operator, value):
        if operator == '-':
            self.accumulator = self.accumulator - value
        else:
            self.accumulator = self.accumulator + value

    def jmp(self, operator, value):
        if operator == '-':
            self.line_number = self.line_number - value -1
        else:
            self.line_number = self.line_number + value -1
        


    def execute(self, part):
        if self.line_number > self.code_lines:
            print('Part 2 ->', self.accumulator)
            self.done = True
        
        instruction, values = self.code[self.line_number].strip().split(' ')
        operator = values[0]
        value = int(values[1:])

        if self.line_number in self.line_numbers_visited:
            if part == 'part1':
                print("Part 1 -> ", self.accumulator)
            self.done = True 
        else:
           self.line_numbers_visited.append(self.line_number)
        
        if instruction == 'acc':
            self.acc(operator, int(value))
        elif instruction == 'jmp':
            self.jmp(operator, int(value))
        self.line_number += 1


    def run(self, part):
        while not self.done:
            self.execute(part)

if __name__ == "__main__":
    with open('day8.txt') as file:
        code = file.readlines()
        engine = Interpreter(code)
        engine.run('part1')

    for i in range(0, len(code)):
        try:
            with open('day8.txt') as file:
                code = file.readlines()
                if 'jmp' in code[i]:
                    code[i] = code[i].replace('jmp', 'nop')
                    engine = Interpreter(code)
                    engine.run('part2')
                elif 'nop' in code[i]:
                    code[i] = code[i].replace('nop', 'jmp')
                    engine = Interpreter(code)
                    engine.run('part2')
        except IndexError:
            print('Program finished')
    
