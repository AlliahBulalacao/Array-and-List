# Bulalacao, Alliah Mae B.

list1 = [2, 18, 19, 97, 14, 20, 16, 5, 27, 15]
print(list1)
print("Menu: \n"
      "1 -> Add an element \n"
      "2 -> Insert an element \n"
      "3 -> Modify an element \n"
      "4-> Delete an element \n"
      "5-> Arrange in ascending order \n"
      "6 -> Arrange in descending order")

while True:
    option = input("Your choice: ")

    if option == '1':
        list1.append(input("Enter the number you want to add: "))
        print("This is the updated list:", list1)

    elif option == '2':
        index = int(input("Where do you want it to insert? [0-9]: "))
        num = int(input("Enter the number you want to insert: "))
        list1.insert(index, num)
        print("This is the updated list:", list1)

    elif option == '3':
        modify = int(input("What index you want to modify? [0-9]: "))
        item = int(input("Enter the element you want to modify: "))
        list1[modify] = item
        print("The element has been modified.")
        print("This is the updated list:", list1)

    elif option == '4':
        list1.pop(int(input("Enter the index you want to delete [0-9]: ")))
        print("The element has been deleted.")
        print("This is the updated list:",list1)

    elif option == '5':
        list1.sort()
        print("This is the updated list:", list1)

    elif option == '6':
        list1.sort()
        list1.reverse()
        print("This is the updated list:", list1)


    else:
        print("Please insert a valid option. Try again.")
        continue

    break

