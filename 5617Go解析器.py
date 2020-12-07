class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        for i in range(len(command)):
            if command[i] == 'G':
                result += 'G'
            elif command[i] == '(':
                if command[i+1] == ')':
                    result +='o'
                    i+= 1
                elif command[i+3] == ')':
                    result += 'al'
                    i+= 3
        return result