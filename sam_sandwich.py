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

def salads_selection(): 
    salad_list = ["Lettuce", "Tomato","Carrot", "Cucumber","Onion"]
    count = 0
    print("We have the following salad options, you can have as many as you want.")
    while count <len(salad_list):
        print(count," ",salad_list[count])
        count+=1 
    print("Press ENTER when you have finished chosing your salads.")
    salads_added = "" #Will hold a string for more than one item
    selected_salad=" "#prompt the user to enter a number in select item from salad

    while selected_salad != "": #if enters is not pressed it will keep prompted you to select a salad.
        selected_salad = input(f"What number salad do you want? \n You have selected: {salads_added}")
        if selected_salad != "": #If enter pressed this statement won't run.
            selected_salad= int(selected_salad)
            #This variable keeps adding on each selected item from salad list. 
            salads_added = salads_added + " " + salad_list[selected_salad-1]
    return salads_added.strip()


#main program
print("Welcome to Sam's Sandwich Shop")
name = str(input("What is your name?"))
print(name)
phone_number = str(input("What is your phone number")) 
bread_choice=bread_selection()
meat_choice=meat_selection()
cheese_choice=cheese_selection()
salad_choice=salads_selection()
print(f"Your selected bread: {bread_choice}") 
print(f"Your selected meat: {meat_choice}") 
print(f"Your selected cheese: {cheese_choice}") 
print(f"Your selected salads: {salad_choice}")
sandwhich_order=[] 
