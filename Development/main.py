#Import all the required libraries to this main module 
import read
import write
import operation

def main_screen_display():

    # Display the title, address and contact details of the shop and greet the user.
    print("....................................................................................................................")
    print("")
    print("                             KARKI ELECTRONICS AND LAPTOP SUPPLIERS                                              ")
    print("                             KAPAN, KATHMANDU | CONTACT: 01-4270603                                              ")
    print("")
    print("....................................................................................................................")
    print("")
    print("                        WELCOME TO KARKI ELECTRONICS AND LAPTOP SUPPLIERS...                                     ")
    print("")
    print("....................................................................................................................")

def validate_input_from_user():
    while True:
        """
        To conduct order and selling process a 
        screen with options are displayed for 
        selecting the operation the user want to
        continue and the user have to enter the value.
        
        If the user enter the value apart from the displayed screen, 
        an error message is displayed.
        """
        print("....................................................................................................................")
        input_from_user = input("    ENTER YOUR SELECTION TO CONTINUE OPERATION: ")
        print("....................................................................................................................")

        """
        Check whether the field is empty or not
        otherwise display suitable message and ask
        the user to input the value again. 
        """
        if not input_from_user.strip():
            print("....................................................................................................................")
            print("")
            print("        ERROR !!!")
            print("        INVALID INPUT.")
            print("        PLEASE ENTER VALUE FROM 1 TO 4.")
            print("")
            print("....................................................................................................................")
            continue

        """
        Using try except block to check if the entered value is integer or not.
        If the value is not integer an error message is displayed.
        """
        try:
            return int(input_from_user)

        except ValueError:
            print("....................................................................................................................")
            print("")
            print("        ERROR !!!")
            print("        ENTERED VALUE IS NOT NUMERIC.")
            print("        PLEASE ENTER A NUMRIC VALUE.")
            print("")
            print("....................................................................................................................")


if __name__ == "__main__":
    while True:
        main_screen_display()

        loop_selection_user = True

        while loop_selection_user:
            print("....................................................................................................................")
            print("")
            print("    PLEASE ENTER THE OPTIONS TO CONTINUE...")
            print("")
            print("    PRESS 1 : TO ORDER LAPTOP")
            print("    PRESS 2 : TO SELL LAPTOP")
            print("    PRESS 3 : TO CHECK LAPTOP STOCK")
            print("    PRESS 4 : TO CLOSE THE PROGRAM AND EXIT FROM THE SYSTEM")
            print("")
            print("....................................................................................................................")

            option_selection = validate_input_from_user()

            if option_selection > 4 or option_selection < 1:
                print("....................................................................................................................")
                print("")
                print("        ERROR !!! ")
                print("        INVALID SELECTION.")
                print("        PLEASE SELECT FROM 1 TO 4.")
                print("")
                print("....................................................................................................................")

            elif option_selection == 1:
                """ 
                When the user enters 1 as the input a question is displayed
                asking which laptop the user want to order.
                Along with the question the list of laptop is displayed in 
                tabular format.

                Functions from other modules are called to this file to
                display the list of laptops, take input from the user and
                display the output in the form of invoice after ordering the laptop.
                """
                print("....................................................................................................................")
                print("")
                print("    WHICH LAPTOP DO YOU WANT TO ORDER ?")
                print("")
                print("....................................................................................................................")
                
                read.display_laptop_list_table()
                read.laptop_quantity_update()
                
                try:
                    # Attempt to get order calculation details
                    distributor_name, laptop_list, distributor_laptop_gross_amount, distributor_total_invoice_amount, distributor_phone_no = operation.get_order_calculation()

                    # Check if the operation was successful (no validation errors)
                    if distributor_name is not None and laptop_list is not None:
                        # Display the order invoice and write it to a file
                        write.generate_and_display_order_invoice(distributor_name, laptop_list, distributor_laptop_gross_amount, distributor_total_invoice_amount, distributor_phone_no)
                        write.write_order_invoice(distributor_name, laptop_list, distributor_laptop_gross_amount, distributor_total_invoice_amount, distributor_phone_no)

                except TypeError:
                    # Handle the case where operation.get_order_calculation() returned None (validation error)
                    print("")
                    
            elif option_selection == 2:
                """ 
                When the user enters 2 as the input a question is displayed
                asking which laptop the user want to sell.
                Along with the question the list of laptop is displayed in 
                tabular format.

                Functions from other modules are called to this file to
                display the list of laptops, take input from the user and
                display the output in the form of invoice after selling the laptop.
                """
                print("....................................................................................................................")
                print("")
                print("    WHICH LAPTOP DO YOU WANT TO SELL?")
                print("")
                print("....................................................................................................................")
                read.display_laptop_list_table()
                read.laptop_quantity_update()
                
                try:
                    sell_customer_name, laptop_list, sell_total_invoice_amount, sell_phone_no, sell_shipping_cost = operation.get_sell_calculation()
                # Check if the operation was successful (no validation errors)
                
                    if sell_customer_name is not None and laptop_list is not None:
                         # Display the order invoice and write it to a file
                        write.generate_and_display_sell_invoice(sell_customer_name, laptop_list, sell_total_invoice_amount, sell_phone_no, sell_shipping_cost)
                        write.write_sell_invoice(sell_customer_name, laptop_list, sell_total_invoice_amount, sell_phone_no, sell_shipping_cost)

                except TypeError:
                    # Handle the case where operation.get_order_calculation() returned None (validation error)
                    print("")
                    
            elif option_selection == 3:
                """
                When the user enters 3 as the input a messae is displayed
                showing the avialble laptops and its stock available in a
                tabular format along with other laptop details.
                """
                print("....................................................................................................................")
                print("")
                print("    THESE ARE THE LAPTOPS AVAILABLE AT OUR STORE CURRENTLY...")
                print("")
                print("....................................................................................................................")
                
                read.display_laptop_list_table()
                
                loop_selection_user = False  # Exit the inner loop and go back to the main menu

            elif option_selection == 4:
                """
                When the user enters 4 as the input a message is displayed
                saying system have been terminated and stops the operation 
                """
                print("....................................................................................................................")
                print("")
                print("    THE SYSTEM HAS BEEN TERMINATED.")
                print("")
                print("....................................................................................................................")
                exit()