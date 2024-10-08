
# from pathlib import Path


# def menU():
#     choice = 0
#     print("1. Count Digits")
#     print(" ")
#     print("2. Find Max")
#     print(" ")
#     print("3. Count Tags")
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
# def countDigits(n):
#     n = abs(n)
#     if n == 0:
#         return 1
#     if n < 10 :
#         return 1
#     else:
#         return 1 + countDigits(n//10)
# ############################# Choice 2 #####################
# def findMax(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         maxx = findMax(lst[1:])
#         if lst[0] > maxx:
#             return lst[0]
#         else:
#             return maxx

# def prompt_User_list():
#     user_input = input("enter a list of numbers seperated by a space: ")
#     int_list = list(map(int, user_input.split()))
#     return int_list
# ##################### Choice 3 ###########################
# def readHtml(directory_path, file_name):
#      directory = Path(directory_path)
#      file_path = directory / file_name
#      if not file_path.is_file():
#         print(f"The file '{file_name}' does not exist in the directory '{directory_path}'.")
#         return None
#      if file_path.suffix != ".html":
#         print(f"The file '{file_name}' is not an HTML file.")
#         return None
#      with file_path.open('r', encoding='utf-8') as file:
#         html_content = file.read()

#      return html_content 

# def countTaghtml(html,tag,start=0):
    
#     openingtag = f"<{tag}"
#     closingtag = f"</{tag}>"

#     opentagpos = html.find(openingtag,start)
#     if opentagpos == -1:
#         return 0
#     else:
#         return 1 + countTaghtml(html, tag, opentagpos + len(openingtag))

# def htmlActions():
#     directory=input("enter the directory of your html file: ")
#     fil = input("enter the name of yor file: ")
#     tag = input("Enter the tag you wish to count: ")

#     html = readHtml(directory, fil)

#     return countTaghtml(html,tag)
# ########################choice 4########################
# def exitS():
#     print("The program will stop now!")
#     quit()
# ############################################################
# #the function that calls functions from the above according to each choice:
# def chooSe():
#     choice = selecT()
#     if choice == 1:
#         n = int(input("Enter your number: "))
#         print("the number of digits in ",n," is ",countDigits(n))
#         chooSe()
#     elif choice == 2:
#         lst = prompt_User_list()
#         print("The Maximum number in your list is ", findMax(lst))
#         chooSe()
#     elif choice == 3:
#         counter = htmlActions()
#         print("The number of times the tag is ",counter)
#         chooSe()
#     elif choice == 4:
#         exitS()
# ###########################main function###########################
# def main():
#     chooSe()
# if __name__ == "__main__":
#     main()


