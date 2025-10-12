import datetime
#Sams Sandwich
def force_number(message,lower,upper):
    while True: #infinite loop that keeps repeating until a valid number is entered
        try:
            num=int(input(message))
            if num>=lower and num<=upper:
                break
            else:
                print(f"ERROR!, please enter in a number between {lower} - {upper}")
        except: #this will only print if you type in a string
            print("Error, please enter in a number not text")
    return num #returning back a valid number within a range 

def force_name(message, lower, upper):
    while True: #this is an infinite loop that will only break if a valid name is entered
        name = str(input(message)).title()
        if len(name)>=lower and len(name) <=upper and name.isalpha():
            print("The name is valid")
            break #the loop breaks if the above condition is met
        else:
            print(f"This is invalid please enter {lower}-{upper} characters")
    return name #a valid name is returned back to the bariable that called the function

def force_cellphone_number(message,lower,upper):
    while True:
        cell=str(input(message))
        if len(cell)>=lower and len(cell)<=upper and cell.isnumeric():
            break
        else:
            print(f"ERROR!,please enter between a {lower} - {upper}")
    return cell

def print_list(list,item):
    print(f"We have the following {item}")
    count=0
    while count< len(list): #prints out each item on the list
        print(count+1," ",list[count])
        count+=1 
    return 

def bread_selection():
    bread_list = ["White","Brown","Italian","Granary","No Bread"]
    print_list(bread_list,"breads")
    bread_selection=force_number("Which bread do you want? Enter a number",1,len(bread_list))
    print(f"You selected bread is: {bread_selection}")
    return bread_list[bread_selection-1]

def meat_selection():
    meat_list = ["Pork","Chicken","Ham","Tofu","No Meat"] #lists of meat
    print_list(meat_list,"meat")
    meat_selection=force_number("Which type of meat do you want? Enter a number",1,len(meat_list))
    print(f"You selected meat is: {meat_selection}")
    return meat_list[meat_selection-1]

def cheese_selection():
    cheese_list = ["Cheddar","Brie","Feta","Cotija","No Cheese"]
    print_list(cheese_list,"cheese")
    cheese_selection=force_number("Which type of cheese do you want? Enter a number",1,len(cheese_list))
    print(f"You selected Cheese is: {cheese_selection}")
    return cheese_list[cheese_selection-1]

def salads_selection(): 
    salad_list = ["Lettuce", "Tomato","Carrot", "Cucumber","Onion","No Salad"]
    print_list(salad_list,"salads")
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

def dressing_selection():
    dressing_list = ["Tomato","Mayo","BBQ","Hummus","No dressing"] 
    print_list(dressing_list,"Dressing")
    print("Press ENTER when you have finished chosing your salads.")
    dressing_added = "" #Will hold a string for more than one item
    selected_dressing=" "#prompt the user to enter a number in select item from salad

    while selected_dressing != "": #if enters is not pressed it will keep prompted you to select a salad.
        selected_dressing = input(f"What number salad do you want? \n You have selected: {dressing_added}")
        if selected_dressing != "": #If enter pressed this statement won't run.
            selected_dressing= int(selected_dressing)
            #This variable keeps adding on each selected item from salad list. 
            dressing_added = dressing_added + " " + dressing_list[selected_dressing-1]
    return dressing_added.strip()


def output_textfile(sandwhich_order,name,phone_number):
    date_time=datetime.datetime.now()
    outFile=open("sams_sandwhich.txt","a")
    print(f"*******Order for {name} --- {phone_number}*******")
    outFile.write(f"\nDate of booking:{date_time}")
    for booking in sandwhich_order:
        print(booking)
        outFile.write("\n {}".format(booking))
    print(f"*************** End of Order{date_time}***************")
    outFile.close()#Closes off the textfile 
    #Once file print, it goes back to the menu 

#main program
print("Welcome to Sam's Sandwich Shop")
name = force_name("What is your name?",2,25)
print(name)
phone_number = force_cellphone_number("What is your phone number",9,12) 
bread_choice=bread_selection() #Calling the bread selection function 
meat_choice=meat_selection()
cheese_choice=cheese_selection()
salad_choice=salads_selection()
dressing_choice =dressing_selection()
sandwhich_order=[] #creating empty list
sandwhich_order.append(f"Bread: {bread_choice}")
sandwhich_order.append(f"Meat: {meat_choice}")
sandwhich_order.append(f"Cheese: {cheese_choice}")
sandwhich_order.append(f"Salad: {salad_choice}")
sandwhich_order.append(f"Dressing: {dressing_choice}")
output_textfile(sandwhich_order,name,phone_number)
print(output_textfile)


