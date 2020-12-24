
#part 1

class Interpreter:
    def __init__(self, file_name):
        self.line_numbers_visited = []
        self.accumulator = 0
        self.line_number = 1
        self.file_name = file_name
        self.done = False
        self.file = []
        self.file_length = 0

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
        


    def execute(self):
        # if self.line_number > self.file_length:
        #     print("Part 2 -> ", self.accumulator)
        #     self.done = True

        instruction, operator, value = self.file[self.line_number -1].strip().split(' ')
        if self.line_number in self.line_numbers_visited:
            print("Part 1 -> ", self.accumulator)
            self.done = True 
        else:
           self.line_numbers_visited.append(self.line_number)
        
        if instruction == 'acc':
            self.acc(operator, int(value))
        elif instruction == 'jmp':
            self.jmp(operator, int(value))
        # elif instruction == 'noop':
        self.line_number += 1


    def run(self):
        with open(self.file_name) as file:
            self.file = file.readlines()
            self.file_length = len(self.file)
            while not self.done:
                self.execute()

if __name__ == "__main__":
    engine = Interpreter('day8.txt')
    engine.run()
    
