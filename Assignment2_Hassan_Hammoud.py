####################Q1#############################
#def myFactorials(m):
#    fact = 1
#    if m == 0:
#        fact=1
#    if m== 1:
#        fact=1
#    else:
#        for i in range(1,n+1):
#            fact = fact*i
#    return fact

#n = int(input("enter your number to get the factorial: "))
#if n < 0:
#    print("Invalid number enter another!")
#else:
#    print(n,"!= ",myFactorials(n))
#####################################################

########################Q2###############################
#def numDiv(m):
#    nums = []
#    if m == 0:
#       return 0
#    if m == 1:
#        return 1
#    else:
#        for i in range (1,m+1):
#            if m%i ==0:
#                nums.append(i)
#    return nums
#n= int(input("enter your number to get its divisors: "))
#print(numDiv(n))
##########################################################
################Q3###########################################
#def revString(mys):
#    n = len(mys)
#    sym=""
#   for i in mys:
#        sym = i + sym
#    return sym
#mnr = input("enter your string: ")
#print(revString(mnr))
#############################################################
######################Q4#########################################
# evenNums(nms):
 #   evens = []  
 #   for num in nms:
 #       if num % 2 == 0:  
 #           evens.append(num) 
 #   return evens

#test = input("Enter a list of integers separated by commas: ")
#tst = [int(num.strip()) for num in test.split(',')]
#result = evenNums(tst)
#print("Output:", result)
#################################################################
#######################Q5###############################


#def checkPassword(pswrd):
#    specialchar = '#!&*$%@^*?'
#    capitals ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#    lows = 'abcdefghijklmnopqrstuvwxyz'
#    nums = '0123456789'
#   upcase = False
#    lowcase= False
#   digcase= False
#    speccase = False

#    if len(pswrd) < 8:
#        return ("weak password")
#    for char in pswrd:
#        if char in capitals:
#           upcase = True
#        elif char in lows:
#            lowcase= True
#        elif char in nums:
#            digcase = True
#        elif char in specialchar:
#            speccase = True
     #   print(char, upcase,lowcase,digcase,speccase)
#    if upcase and lowcase and digcase and speccase:
#        return "strong password"
#   else:
#        return "weak password"

#password = input("enter your password to check: ")
#print(checkPassword(password))
########################################################################
#######################################Q6#################################
#def ipV4(ip):
#    octets = []
#    oct = 0
#    coct = ''
#    count = 0 
#    for char in ip:
#        if char == '.':
#            if coct == '' or count >=3:
#                return False
#            octets.append(coct)
#            coct = ""
#            count += 1
#        else:
#            if '0'<= char <= '9':
#                coct+=char
#            else:
#                return False
#    if coct == "" or count != 3:
#        return False
#    octets.append(coct)
#    for oct in octets:
#        if len(oct)>1 and oct[0] == 0:
#            return False
#        num = 0
#        for digit in oct:
#            num = num * 10 + (ord(digit) - ord('0'))
#        if num < 0 or num > 255:
#            return False
#
#    return True
#
#ips = input("enter your ip: ")
#if ipV4(ips):
#    print("valid")
#else:
#    print("invalid")
#####################################################################



