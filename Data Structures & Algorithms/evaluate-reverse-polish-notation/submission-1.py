class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operands = ["-", "+", "*", "/"]
        
        for n in tokens:
            if n in operands:
                op1 = numbers.pop()
                op2 = numbers.pop()
                if n == "-":
                    numbers.append(op2 - op1)
                elif n == "+":
                    numbers.append(op1 + op2)
                elif n == "*":
                    numbers.append(op1 * op2)
                elif n == "/":
                    
                    numbers.append(int(float(op2) / op1))
            else:
                numbers.append(int(n))
        return numbers[0]