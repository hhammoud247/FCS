# def menU():
#     choice = 0
#     print("1.Sum Tuples")
#     print(" ")
#     print("2.Export JSON")
#     print(" ")
#     print("3.Import JSON")
#     print(" ")
#     print("4. Exit")
#     print(" ")
#     print("- - - - - - - - - - - - - - -")
#     print(" ")
#     n = int(input("Enter a Choice: "))
#     return n
# def selecT():
#     n = menU()
#     if n == 1:
#         choice = 1
#     elif n == 2:
#         choice = 2
#     elif n == 3:
#         choice = 3
#     elif n == 4:
#         choice = 4
#     return choice
# ##############  Choice 1 ##############################
# def addTuples(tup1,tup2):
#     x=0
#     tups1 = list(tup1)
#     tups2 = list(tup2)
#     n = len(tups1)
#     m = len(tups2)
#     sums = []
#     if n == m: 
#         for i in range(n):
#             x = int(tups1[i])+int(tups2[i])
#             sums.append(x)
#         tups = tuple(sums)
#         return tups
#     else:
#         print("can't add tuples of different lengths!")
# # ################# Choice 2 ############################
# def dicttojson(dict1,filename):
#     #open file in read mode
#     file= open(filename,'w') 
#     file.write("{\n")
#     items = [] #include all elements from the dictionary
#     for key,value in dict1.items():
#         keys = f'"{key}"' #we converted key into a json string
#         #now for the value we should convert them according to their type
#         if isinstance(value,str): #learnt from stackoverflow
#             value_s = f'"{value}"'
#         elif isinstance(value,(int,float)):
#             value_s = str(value) #numbers remain the same
#         elif isinstance(value,bool):
#             value_s = str(value).lower() #boolean operators whether it is true or false must be lower case
#         elif value is None:
#             value_s = 'null' # None is translated to null 
#         items.append(f" {keys} : {value_s}")
#     file.write(",\n".join(items)) #join items with commas and write them to file
#     file.write("\n}")
# ######################## choice 3 #########################

# def jsontopython(filename):
#     # Open and read the file content
#     file=open(filename, 'r') 
#     j_s = file.read().strip()

#     # Remove outer brackets and strip excess spaces
#     j_s = j_s[1:-1].strip()

#     # Initialize result list
#     result = []
    
#     # A helper to find individual JSON objects by tracking opening/closing braces
#     obj = ""
#     open_braces = 0

#     for char in j_s:
#         obj += char
        
#         if char == '{':
#             open_braces += 1
#         elif char == '}':
#             open_braces -= 1
        
#         # When the object is fully enclosed in braces
#         if open_braces == 0 and obj:
#             dict1 = {}
#             obj = obj.strip()[1:-1]  # Strip outer braces from the object
#             pairs = obj.split(',')  # Split into key-value pairs
            
#             for p in pairs:
#                 if ':' in p:
#                     keys = p.split(':', 1)
#                     key = keys[0].strip().strip('"')  # Clean the key
                    
#                     # Clean and handle the value
#                     value = keys[1].strip()
#                     if value.startswith('"') and value.endswith('"'):
#                         value = value[1:-1]  # It's a string
#                     elif value == "true":
#                         value = True
#                     elif value == "false":
#                         value = False
#                     elif value == "null":
#                         value = None
#                     else:
#                         # Convert to int or float if possible
#                         try:
#                             value = int(value)
#                         except ValueError:
#                             try:
#                                 value = float(value)
#                             except ValueError:
#                                 pass
                    
#                     # Add the key-value pair to the dictionary
#                     dict1[key] = value
            
#             result.append(dict1)
#             obj = ""  # Reset current object

#     return result

# ############################### choice 4 ###############################
# def exitS():
#     print("The program will stop now!")
#     quit()
# ########################################################################
# #the function that calls functions from the above according to each choice:
# def chooSe():
#     choice = selecT()
#     if choice == 1:
#         input1 = input("Enter elements of the first tuple separated by space or commas: ")
#         tuple1 = tuple(input1.replace(',', ' ').split())
#         input2 = input("Enter elements of the second tuple separated by space or commas: ")
#         tuple2 = tuple(input2.replace(',', ' ').split())
#         print ("the sum of elements of both tuples is: ",addTuples(tuple1,tuple2)) 
#         chooSe()
#     elif choice == 2:
#         newdict = {}
#         print("\n")
#         n=int(input("enter number of students: "))
#         for i in range(n):
#             key = input("enter name of the student: ")
#             value= float(input("enter score: "))
#             newdict.update({key: value})
#         filename=input("input the name of a .json file: ")
#         print(dicttojson(newdict,filename))
#         print("done! check file")
#         print("\n\n")
#         chooSe()
#     elif choice == 3:
#         filename = input("enter the name of the json file: ")
#         print(jsontopython(filename))
#         print("\n\n")
#         chooSe()
#     elif choice == 4:
#         exitS()
# ###########################main function###########################
# def main():
#     chooSe()
# if __name__ == "__main__":
#     main()

###################################################
#                   Exercise 2                    #
###################################################
#a.(1/6)N +8000N^3 + 24
# since 8000N^3 is the dominant term in the expression 
# hence acoording to big O notation it will be O(N^3)
# b.(1/6)N^3 the big O notation of this polynomial is O(N^3)
# c.(1/6)N! + 200N^4:
# here N! is the dominant part since factorial function is faster 
# in growth than polynomials hence the big O notation will be O(N!)
# d.NlogN + 1000:
# in here the dominant term is NlogN the big O notation will be O(NlogN)
# e.logN + N: in here the linear term is the dominant term since it is
#  faster in growing than logarithm hence the big O notation will be O(N)
#f.(1/2)N(N-1): expanding this will give us (1/2)N^2 - N/2 the dominant
#part will be (1/2)N^2 the big O notation O(N^2)
#g. N^2 + 220NlogN^2 +3N + 9000
#in here first NlogN^2 = 2NlogN thus the dominant term will be the polynomial 
#since the polynomial is faster growing than logarithm hence N^2 is the dominant term
#the big O notation O(N^2)
#h.N! + 3^N + 2^N + N^2 + N^3: the dominant term here is the factorial term since 
#factorial is faster growing than exponential functions hence the big O Notation will be O(N!)
















