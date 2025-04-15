import write 

def input_validation(prompt, type_data):
    """
    Function is declared to check the validation
    of the values entered by the user.
    
    If the user enters the wrong value, an appropriate
    error message is displayed.
    """
    while True:
        input_valid = input(prompt)
        
        if not input_valid.strip():
            # If the input field is empty, display an error message and loop back to the prompt.
            print("....................................................................................................................")
            print("")
            print("        ERROR !!!")
            print("        EMPTY FIELD.")
            print("        PLEASE ENTER APPROPRIATE VALUE.")
            print("")
            print("....................................................................................................................")
            continue
        
        if type_data == str and (input_valid.isdigit() or input_valid.replace(".","").isdigit()):
            # If the input field has a wrong value entered by the user, display an error message and loop back to the prompt.
            print("....................................................................................................................")
            print("")
            print("        ERROR !!!")
            print("        INPUT INVALID.")
            print("        PLEASE ENTER A STRING VALUE.")
            print("")
            print("....................................................................................................................")
            continue
        
        if type_data == int:
            # If the entered input is not an integer, display an error message and loop back to the prompt.
            if not input_valid.isdigit():
                print("....................................................................................................................")
                print("")
                print("        ERROR !!!")
                print("        INVALID INPUT.")
                print("        PLEASE ENTER AN INTEGER VALUE.")
                print("")
                print("....................................................................................................................")
                continue
            # Convert the input to an integer before returning
            return int(input_valid)

        if type_data == bool:
            # If the entered input is not boolean, display an error message and loop back to the prompt.
            if input_valid.lower() not in ["yes","no"]:
                print("....................................................................................................................")
                print("")
                print("        ERROR !!!")
                print("        INVALID INPUT.")
                print("        PLEASE ENTER 'YES' OR 'NO'")
                print("")
                print("....................................................................................................................")
                continue
            # Convert the input to a boolean before returning
            return input_valid.lower() == 'yes'
        
        # For any other type (e.g., str), return value as is
        return input_valid

"""
Generation of order invoice by taking all the required details from the 
distributor and generate the invoice by doing required calculations    
"""
def get_order_calculation():

    distributor_order_result = get_distributor_laptop_order_details()

    # Check if the function returned None due to validation error
    if distributor_order_result is not None:
        distributor_name, laptop_list, distributor_laptop_gross_amount, distributor_total_invoice_amount, distributor_phone_no = distributor_order_result
        # Display order invoice on the screen
        write.generate_and_display_order_invoice(distributor_name, laptop_list, distributor_laptop_gross_amount, distributor_total_invoice_amount, distributor_phone_no)

        # Write the invoice to the text file after data is entered
        write.write_order_invoice(distributor_name, laptop_list, distributor_laptop_gross_amount, distributor_total_invoice_amount, distributor_phone_no)

def get_sell_calculation():
    sell_order_result = get_customer_laptop_sell_details()

    # Check if the function returned None due to validation error
    if sell_order_result is not None:
        sell_customer_name, laptop_list, sell_total_invoice_amount, sell_phone_no, sell_shipping_cost = sell_order_result

        # Ask if the user wants shipping
        sell_customer_shipping_choice = input_validation("    DO YOU WANT SHIPPING (YES/NO): ", bool)
        if sell_customer_shipping_choice:
            sell_shipping_cost = 200
            sell_total_invoice_amount += sell_shipping_cost  # Add shipping cost to the total invoice amount
        else:
            sell_shipping_cost = 0

        # Display the invoice
        write.generate_and_display_sell_invoice(sell_customer_name, laptop_list, sell_total_invoice_amount, sell_phone_no, sell_shipping_cost)

        # Generate and write the invoice to a text file
        write.write_sell_invoice(sell_customer_name, laptop_list, sell_total_invoice_amount, sell_phone_no, sell_shipping_cost)
         
def get_distributor_laptop_order_details():
    """
    This function customer takes the input from the distributor
    to fill the details and generate order invoice 
    """
    
    print("")
    print("====================================================================================================================")
    print("        TO GENERATE ORDER INVOICE PLEASE ENTER THE FOLLOWING DETAILS")
    print("====================================================================================================================")
    print("")
    
    distributor_name = input_validation("    ENTER DISTRIBUTOR NAME: ",str)
    distributor_phone_no = input_validation("    ENTER PHONE NUMBER: ",int)
    
    # A list is created to store order details.
    laptop_list = []
    
    while True:
        distributor_laptop_brand_name = input_validation("    ENTER LAPTOP BRAND: ",str)
        distributor_laptop_model_name = input_validation("    ENTER LAPTOP MODEL: ",str)   
        distributor_laptop_quantity = input_validation("    ENTER LAPTOP QUANTITY: ",int)
        distributor_laptop_price = input_validation("    ENTER LAPTOP PRICE: $",int)
        
        # Calculate gross amount of laptop added to the list
        distributor_laptop_gross_amount = distributor_laptop_quantity * distributor_laptop_price
        
        # 13% VAT amount is calculated from the gross amount
        ditributor_VAT_amount = 0.13 * distributor_laptop_gross_amount  
        
        # Calculate total amount
        distributor_total_amount = distributor_laptop_gross_amount + ditributor_VAT_amount
        
        # Add laptop details to the list created.
        laptop_list.append([distributor_laptop_brand_name, 
                            distributor_laptop_model_name, 
                            distributor_laptop_quantity, 
                            distributor_laptop_price, 
                            distributor_laptop_gross_amount, 
                            ditributor_VAT_amount, 
                            distributor_total_amount])   

        """
        If the user want to order more loop the  prompt 
        otherwise display the invoice.
        """
        distributor_order_more_laptop = input_validation("    DO YOU WANT TO ORDER MORE LAPTOPS? (YES/NO): ",bool)

        if distributor_order_more_laptop:
            continue
        else:
            break
        
    # Calculate total amount in invoice
    distributor_total_invoice_amount = sum(laptop[6] for  laptop in laptop_list)
    
    # Calculate total gross amount in invoice
    distributor_laptop_gross_amount = sum(laptop[4] for  laptop in laptop_list)
        
    return distributor_name, laptop_list, distributor_laptop_gross_amount, distributor_total_invoice_amount, distributor_phone_no
    
if __name__ =="__main__":
    get_order_calculation()
    

"""
Generation of purchase invoice by taking all the required details from the 
distributor and generate the invoice by doing required calculations    
"""

def get_customer_laptop_sell_details():
    """
    This function takes the input from the customer
    to fill the details and generate sell invoice 
    """
    print("")
    print("====================================================================================================================")
    print("        TO GENERATE ORDER INVOICE PLEASE ENTER THE FOLLOWING DETAILS")
    print("====================================================================================================================")
    print("")
    
    sell_customer_name = input_validation("    ENTER CUSTOMER NAME: ", str)
    sell_phone_no = input_validation("    ENTER PHONE NUMBER: ", int)
    
    # Store the product sold to the customer.
    laptop_list = []
    
    while True:
        sell_laptop_brand_name = input_validation("    ENTER LAPTOP BRAND: ", str)
        sell_laptop_model_name = input_validation("    ENTER LAPTOP MODEL: ", str)   
        sell_laptop_quantity = input_validation("    ENTER LAPTOP QUANTITY: ", int)
        sell_laptop_price = input_validation("    ENTER LAPTOP PRICE: $", int)  # Use float to handle decimal prices
    
        sell_gross_amount = sell_laptop_quantity * sell_laptop_price
    
        
        laptop_list.append([sell_laptop_brand_name,
                            sell_laptop_model_name,
                            sell_laptop_quantity,
                            sell_laptop_price,
                            sell_gross_amount])
        
        sell_more_laptop = input_validation("    DO YOU WANT TO PURCHASE MORE LAPTOPS? (YES/NO): ", bool)
        """
        If the user wants to order more, loop the prompt 
        otherwise display the invoice.
        """
        
        if sell_more_laptop:
            continue
        else:
            break

    # Calculate the total invoice amount
    sell_total_invoice_amount = sum(product[4] for product in laptop_list)

    # Assume the initial shipping cost is 0
    sell_shipping_cost = 0

    return sell_customer_name, laptop_list, sell_total_invoice_amount, sell_phone_no, sell_shipping_cost

# Call the function to calculate the total amount and generate the invoice
if __name__ == "__main__":
    get_sell_calculation()
    
