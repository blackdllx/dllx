PHONENUM = " "
try: 
    num = str(input('ваш номер телефону:'))
    num = num.replace(' ', '')
    PHONENUM = [int(num)]
except ValueError:
    print(PHONENUM)
    
    
    print("помилка") 
print(PHONENUM)

def lisage():
    global PHONENUM
    phonenum = []
    
    for i in str(PHONENUM):
        phonenum = phonenum + [i]
    PHONENUM = phonenum

def tren():
    global PHONENUM
    lisage()
    perebor = PHONENUM
    
    print(perebor[1])
    pb = perebor[1] + perebor[2] + perebor[3]
    print(pb)
    if pb == '+380':
        
        for i in range(0, 4):
            perebor[i] = ''
    elif perebor[1] == '0':
        perebor[1] = ''
    elif pb == '380':
        
        for i in range(0, 4):
            perebor[i] = ''
    else:
        pass
    finisd = ['+38(0'] + [perebor[4]] + [perebor[5]] + [')'] + [perebor[6]] + [perebor[7]] + [perebor[8]] + ['-'] + [perebor[9]] + [perebor[10]] + ['-'] + [perebor[11]] + [perebor[12]]
    perebor = listToString(finisd)
    perebor = perebor.replace(']', '')
    
    PHONENUM = str(perebor)
    

def listToString(s): 
    
    str1 = "" 
    
   
    for ele in s: 
        str1 += ele  
      
    return str1 

tren()

print(PHONENUM)




