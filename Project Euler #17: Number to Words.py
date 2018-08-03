t = int(raw_input().strip())

words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

def inWords(n):
    output = ""
    if n == 0:
        return(words[0])
    
    while(n > 0):
        if n <= 15:
            output += words[n]
            n -= n
        elif n < 20:    
            if n!=18: output += words[(n%10)] + "teen";
            else: output += words[(n%10)] + "een";
            n -= n
        elif n < 100:
            a = n//10
            output += words[a+14]
            n = n % 10
        elif n < 1000:
            a = n//100
            output += words[a] + " Hundred"
            n = n % 100
        elif n < 1000000:
            a = n//1000
            output += inWords(a) + " Thousand"
            n = n % 1000
        elif n < 1000000000:
            a = n//1000000
            output += inWords(a) + " Million"
            n = n % 1000000  
        elif n < 1000000000000:
            a = n//1000000000
            output += inWords(a) + " Billion"
            n = n % 1000000000
            
        else:
            a = n//1000000000000
            output += inWords(a) + " Trillion"
            n = n % 1000000000000
        if n > 0:
            output += " "
    return(output)            
        
for a0 in range(t):
    n = int(raw_input().strip())
    print(inWords(n))
