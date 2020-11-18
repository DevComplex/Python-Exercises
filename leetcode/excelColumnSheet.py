 def convertToTitle(self, n):
    output = []
        
    while n > 0:
        letterIndex = (n - 1) % 26
        output.append(chr(letterIndex + ord('A')))
        n = (n - 1) // 26
            
    return "".join(output[::-1])