#Created by Pradyumna P Rao
#04-April-2021
#Dayananda Sagar College Of Engineering
#All conversions in between number systems like Binary,Decimal,Octal and Hexadecimal

#Binary To Decimal Conversion

def bintodeci(number):
    number=str(number)
    leng = len(number)
    b= 0
    for i in number:
        c = int(i) * pow(2,leng - 1)
        b = b + c
        leng = leng  -1
    return b


#Decimal to Binary Conversion

def decitobin(number):
    number = int(number)
    s=''
    while(number>0.1):
        a=number%2
        number = number/2
        s=s+str(int(a))
    return int(s[::-1])



#Binary To Octal Conversion

def bintooctal(number):
    b = bintodeci(number)
    s=''
    while(b>0.1):
        a=b%8
        b = b/8
        s=s+str(int(a))
    return int(s[::-1])



#Octal to Binary Conversion

def octaltobin(number):
    number=str(number)
    number = octaltodeci(number)
    h=decitobin(number)
    return h



#Binary To Hexa-Decimal Conversion

def bintohexa(number):
    number=str(number)
    if not len(number)%4 ==0:
        number =  ('0'*(4-len(number)%4)) + number
    diction={'0000':0,'0001':1,'0010':2,'0011':3,'0100':4,'0101':5,'0110':6,'0111':7,'1000':8,'1001':9,'1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
    h,g='',''
    y,z=0,4
    while(y<len(number)):
        g = number[y:z]
        h = h + str(diction[g])
        y+=4
        z+=4
    return h



#Hexa-Decimal to binary Conversion

def hexatobin(number):
    number=str(number)
    diction={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}
    h,g='',''
    y,z=0,4
    for i in number:
        h = h + str(diction[i])
    return int(h)



#Decimal to Octal Conversion

def decitooctal(number):
    number=int(number)
    s=''
    while(number>0.1):
        a=number%8
        number=number/8
        s=s+str(int(a))
    return int(s[::-1])



#Octal to Decimal Conversion

def octaltodeci(number):
    leng = len(number)
    b= 0
    for i in number:
        c = int(i) * pow(8,leng - 1)
        b = b + c
        leng = leng  -1
    return b



#Decimal To Hexa-Decimal Conversion

def decitohexa(number):
    number=int(number)
    s=''
    while(number>0.1):
        a=number%16
        number=number/16
        s=s+str(int(a))
    return int(s[::-1])


#Hexa-Decimal to Decimal Conversion

def hexatodeci(number):
    leng = len(number)
    b= 0
    diction = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    for i in number:
        if i.isdigit():
            c = int(i) * pow(16,leng - 1)
            b = b + c
        else:
            c =diction[i] * pow(16,leng - 1)
            b = b + c
        leng = leng  -1
    return int(b)



#Octal to Hexa-Decimal Conversion

def octaltohexa(number):
    number =octaltobin(number)
    h = bintohexa(number)
    return h




#Hexa-Decimal to Octal Conversion

def hexatooctal(number):
    number=str(number)
    diction={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}
    diction2={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
    g,f,j,h='','','',''
    y,z=0,3
    for i in number:
        h = h + str(diction[i])
    if not len(h)%3 ==0:
        h =  ('0'*(3-len(h)%3)) + h
    while(y<len(h)):
        f = h[y:z]
        j = j + str(diction2[f])
        y+=3
        z+=3
    if int(j[0]) == 0:
        j = j[1:]
    return int(j)


# In[ ]:




