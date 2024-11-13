#LAB 1## 

def lab1 (): 

    num=int(input("Enter the number of scores: "))#Gets the number of scores from the user 

    scores_list=[] #Sets up an empty list get keep the scores

    for i in range (num):#The for loop to get the scores into the list using num or the users input as the range 

        score=float(input("Enter your score: ")) 

        scores_list.append(score) 

        avrage=sum(scores_list)/len(scores_list) #Calculates the avrage and stores it into variable avrage 

    if avrage>=90: #Compares the avrage to a number. TO get the letter grade 

        print("A") 

    elif avrage>=80 and avrage<90: 

        print("B") 

    elif avrage>=70 and avrage<80:  

        print("C") 

    elif avrage>=60 and avrage<70:  

        print("D") 

    else: 

        print("F") 

    print("Your avrage is:",avrage) #Prints the avrage with in a sentince 

#lab1 () #Envokes the lab1 function

 

#LAB 2 ## 

def lab2 (): 

    nums=input("Enter numbers: ")#Gets the users numbers for the list 

    nums_list=nums.split(' ')#Splits the string up into numbers and stores it into a list with a space in the middle 

    even=0 #Sets the variable even to 0

    odd=0 #Sets the variable odd to 0 

    print(nums_list)#Prints the list 

    for num in nums_list: #Compares each number %2 to the output of 0. If the answer is 0 than it increases even else it increase odd 

        if int(num)%2==0: 

            even+=1 

        else: 

            odd+=1 

    print("You have", even, "even numbers")#Prints even in a sentence 

    print("You have", odd, "odd numbers")#Prints odd in a sentence

#lab2() #Envokes the lab2 function

 

#LAB 3 ###  

def lab3(): 

    nums1=input("Enter numbers: ")#Gets the numbers for list 1

    nums_list1=nums1.split(' ') #Splits the string into characters 

    nums2=input("Enter numbers: ") #Gets the numbers for list 2

    nums_list2=nums2.split(' ') #Splits the string into characters 

    for num in nums_list1: #Iterates over each value in list 1 
        if num in nums_list2: #If they find num in list 2 remove it 
            nums_list2.remove(num)
    return nums_list1 + nums_list2  # Combindes both lists into a single list 
   
print(lab3()) 