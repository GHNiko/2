while True:
    enter = int(input("Enter the number of elements you want to add to your list: "))
    our_list = []

    for i in range(enter):
        num=int(input("Enter a number: "))
        our_list.append(num)

    even,odd=([i for i in our_list if i%2==0],[i for i in our_list if i%2!=0])    

    if (len(odd)!=0):
        avg = sum(odd)/len(odd)
        print("The average of odd numbers in the list is: ",round(avg,2))
        break
    else:
        print('You did not enter any odd numbers.')
        print('Please add at least one odd number!')
        continue
