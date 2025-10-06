#Sams Sandwich
def bread_selection():
    bread_list = ["White","Brown","Italian","Granary","No Bread"]
    print("We have the following breads")
    count=0
    while count< len(bread_list): #prints out each item on the list
        print(count+1," ",bread_list[count])
        count+=1 
    bread_selection=int(input("Which bread do you want? Enter a number"))
    print(f"You selected bread is: {bread_selection}")
    return bread_list[bread_selection-1]

def meat_selection():
    meat_list = ["Pork","Chicken","Ham","Tofu","No Meat"] #lists of meat
    print("We have the following meats")
    count=0
    while count< len(meat_list): #prints out each item on the list
        print(count+1," ",meat_list[count])
        count+=1 
    meat_selection=int(input("Which type of meat do you want? Enter a number"))
    print(f"You selected bread is: {meat_selection}")
    return meat_list[meat_selection-1]

def cheese_selection():
    cheese_list = ["Cheddar","Brie","Feta","Cotija","No Cheese"]
    count=0
    while count< len(cheese_list): #prints out each item on the list
        print(count+1," ",cheese_list[count])
        count+=1 
    cheese_selection=int(input("Which type of cheese do you want? Enter a number"))
    print(f"You selected bread is: {cheese_selection}")
    return cheese_list[cheese_selection-1]

#main program
print("Welcome to Sam's Sandwich Shop")
bread_choice=bread_selection()
meat_choice=meat_selection()
cheese_choice=cheese_selection()
