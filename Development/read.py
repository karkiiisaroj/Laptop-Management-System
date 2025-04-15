# Read the text file laptop info.txt
open_textfile_path = "laptop info.txt"

with open(open_textfile_path,'r') as laptop_details_file:
    laptop_list = [line.strip().split(",") for line in laptop_details_file]

def display_laptop_list_table():
    """
    Function display_laptop_list_table()
    is declared to display the products in
    tabular format
    """
    header_laptop_details_table = ["S.N","MODEL","BRAND","PRICE","QUANTITY","PROCESSOR","GRAPHICS"]
    """
    Display the header of the table that includes
    S.N, MODEL, BRAND, PRICE, QUANTITY, PROCESSOR, GRAPHICS
    details of a laptop in organized order.
    """
    print("....................................................................................................................")
    print("")
    
    # Display the header of the table.
    print("+" + "-" * 10 + "+" + "-" * 24 + "+" + "-" * 16 + "+" + "-" * 12 + "+" + "-" * 12 + "+" + "-" * 20 + "+" + "-" * 14 + "+")
    print("|{:^10}|{:^24}|{:^16}|{:^12}|{:^12}|{:^20}|{:^14}|".format(*header_laptop_details_table))
    print("+" + "-" * 10 + "+" + "-" * 24 + "+" + "-" * 16 + "+" + "-" * 12 + "+" + "-" * 12 + "+" + "-" * 20 + "+" + "-" * 14 + "+")
    
    # Display each row of the table in a formatted order with the list of laptops and other details.
    for laptops_table in laptop_list:
        print("|{:^10}|{:^24}|{:^16}|{:^12}|{:^12}|{:^20}|{:^14}|".format(* laptops_table))
    # Display the footer of the table.
    print("+" + "-" * 10 + "+" + "-" * 24 + "+" + "-" * 16 + "+" + "-" * 12 + "+" + "-" * 12 + "+" + "-" * 20 + "+" + "-" * 14 + "+")
    print("")
    print("....................................................................................................................")

def laptop_quantity_update():
    """
    Function laptop_quantity_update()
    is declared to check and update the quantity 
    of the laptops when the laptop is ordered 
    or sold by the store to its customer.
    """
    while True:

        input_index_of_laptop = input("    ENTER THE INDEX OF LAPTOP: ")
        
        
        if not input_index_of_laptop.strip():
            """
            Check if the index of the laptop entered by the user is empty or not. 
            If the field is empty, it displays an error message.
            It loop back to the prompt and ask index of laptop.
            """
            print("....................................................................................................................")
            print("")
            print("        ERROR !!!")
            print("        EMPTY INDEX")
            print("        PLEASE ENTER VALID LAPTOP INDEX.")
            print("")
            print("....................................................................................................................")
            continue
        
        if not input_index_of_laptop.isdigit():
            """
            Check if the index of the laptop entered by the user is a string or not. 
            If the field has a string value, it displays an error message.
            It loop back to the prompt and ask index of laptop.
            """
            print("....................................................................................................................")
            print("")
            print("        ERROR !!!")
            print("        INVALID INDEX")
            print("        PLEASE ENTER A VALID NUMERIC LAPTOP INDEX.")
            print("")
            print("....................................................................................................................")
            continue 
         
        index_of_laptop = int(input_index_of_laptop)
            
        if index_of_laptop < 1 or index_of_laptop > len(laptop_list):
            """
            If the index of the laptop is less than 1 or greater than 
            the number of laptops displayed on the screen, it validates and displays
            an error message as per the input from the user and loop back to the prompt. 
            """
            print("....................................................................................................................")
            print("")
            print("        ERROR !!!")
            print("        INVALID LAPTOP INDEX.")
            print("")
            print("....................................................................................................................")
            continue
            
        break
    
    while True:
        
        quantity_laptop = input("    ENTER QUANTITY:")
       
        
        if not quantity_laptop.strip():
            """
            Check if the index of the laptop entered by the user is empty or not. 
            If the field is empty, it displays an error message.
            It loop back to the prompt and ask index of laptop.
            """
            print("....................................................................................................................")
            print("")
            print("        ERROR !!!")
            print("        EMPTY INPUT.")
            print("        PLEASE ENTER VALID QUANTITY.")
            print("")
            print("....................................................................................................................")
            continue
        
        if not quantity_laptop.isdigit():
            """
            Check if the quantity of the laptop entered by the user is a string or not. 
            If the field has a string value, it displays an error message.
            It loop back to the prompt and ask quantity of laptop.
            """
            print("....................................................................................................................")
            print("")
            print("        ERROR !!!")
            print("        EMPTY INPUT.")
            print("        PLEASE ENTER VALID NUMERIC QUANTITY.")
            print("")
            print("....................................................................................................................")
            continue
        
        reduce_quantity = int(quantity_laptop)
        
        if reduce_quantity < 0 or reduce_quantity == 0:
            
            """
            If the quantity is less than 0 then display
            out of stock message and loop back to prompt again.
            """
            print("....................................................................................................................")
            print("")
            print("        SORRY !!!")
            print("        THE LAPTOP YOU ARE LOOKING FOR IS OUT OF STOCK...")
            print("")
            print("....................................................................................................................")
            continue
        
        break

    # Update the quantity in laptop.txt text file.
    laptop_list[index_of_laptop - 1] [4] = str(int(laptop_list [index_of_laptop - 1] [4] ) - reduce_quantity)
        
    # Writing and updating quantity in laptop.txt file
    with open(open_textfile_path, 'w') as laptop_details_file:
        for information_laptop in laptop_list:
            laptop_details_file.write(",".join(information_laptop) + "\n")
    
    print("....................................................................................................................")
    print("")
    print("        LAPTOP QUNATITY UPDATED IN THE TEXT FILE.")
    print("")
    print("....................................................................................................................")
    
    # Total amount calculation and display
    user_laptop_selected = laptop_list[index_of_laptop - 1]
    user_laptop_price = float(user_laptop_selected[3].replace("$", ""))
    user_total_amount = reduce_quantity * user_laptop_price
    
    print("....................................................................................................................")
    print("        TOTAL AMOUNT : $"+ str(user_total_amount))
    print("....................................................................................................................")
    
    while True:
        user_want_more_laptop = input("    DO YOU WANT TO BUY MORE LAPTOPS? (YES/NO): ") 
        print("....................................................................................................................")
        
        if not user_want_more_laptop.strip():
            """
            Check if the input is empty or not
            If it is empty display error message 
            and loop back to prompt.
            """
            print("....................................................................................................................")
            print("")
            print("        ERROR !!!")
            print("        EMPTY INPUT.")
            print("        PLEASE ENTER 'YES' OR 'NO' ")
            print("")
            print("....................................................................................................................")
            continue
        
        if user_want_more_laptop.isdigit():
            """
            Check if the input is numeric value or not
            If it is numeric value display error message 
            and loop back to prompt.
            """
            print("....................................................................................................................")
            print("")
            print("        ERROR !!!")
            print("        INVALID INPUT.")
            print("        PLEASE ENTER 'YES' OR 'NO' ")
            print("")
            print("....................................................................................................................")
            continue
            
        user_choice = user_want_more_laptop.lower()
        """
        Ask customer if they want to buy more laptop.
        If yes loop the prompt
        If no display thank you message and other details.
        """
        if user_choice == "yes":
            laptop_quantity_update()
            
        elif user_choice == "no":
            print("....................................................................................................................")
            print("")
            print("        THANK YOU FOR SHOPPING WITH US !")
            print("               VISIT AGAIN !!!")
            print("")
            print("....................................................................................................................")
        
        else:
            print("....................................................................................................................")
            print("")
            print("        ERROR !!!")
            print("        INVALID INPUT")
            print("        PLEASE ENTER 'YES' OR 'NO' ")
            print("")
            print("....................................................................................................................")
            continue
        break
    
if __name__ == "__main__":
    laptop_quantity_update()