value = input()
data = []
maximum = None

while(value != 'exit'):
    data.append(value)
    temp = value[-1]
    value = float(value[0:-1])
    
    if temp == 'F':
        value = (value - 32)/1.8
        
    if temp == 'K':
        value = value - 273.15

    if maximum == None or value >= maximum:
        maximum = value
        
    value = input()
    
print(f"%.2f" % maximum)
    
    