import datetime

"""
    Date and time for invoice 
    which is displayed at the time 
    while ordering or selling laptop
    
    Displayed in dd/mm/yy and hh:mm:ss
    format.
"""
now = datetime.datetime.now()
string_day = str(now.day) 
string_month = str(now.month) 
string_year = str(now.year) 
string_hour = str(now.hour)
string_minute = str(now.minute)
string_second = str(now.second)

string_date_time = string_day +"/"+ string_month +"/"+ string_year +"  "+ string_hour +":"+ string_minute+":"+string_second

# Function to display order invoice
def generate_and_display_order_invoice(distributor_name, laptop_list, distributor_laptop_gross_amount, distributor_total_invoice_amount, distributor_phone_no):
    print("====================================================================================================================")
    print("")
    print("                             KARKI ELECTRONICS AND LAPTOP SUPPLIERS                                              ")
    print("                             KAPAN, KATHMANDU | CONTACT: 01-4270603                                              ")
    print("")
    print("====================================================================================================================")
    print("                                         ORDER INVOICE")
    print("====================================================================================================================")
    print("Name of customer: " + str(distributor_name) + "\n")
    print("Phone no: " + str(distributor_phone_no) + "\n")
    print("Date: " + str(string_date_time + "\n"))
    print("====================================================================================================================")

    if laptop_list:
        print("------------------------------------------------------------------------------------------------------------")
        print("f{:<15}{:<15}{:<15}{:<15}{:<15}".format("LAPTOP BRAND", "LAPTOP MODEL", "QUANTITY", "UNIT PRICE", "AMOUNT"))
        print("------------------------------------------------------------------------------------------------------------")
        for laptop in laptop_list:
            print("f{:<15}{:<15}{:<15}{:<15}{:<15}".format(laptop[0], laptop[1], laptop[2], "$" + str(laptop[3]), "$" + str(laptop[4])))

    print("------------------------------------------------------------------------------------------------------------")
    print("{:<30}Gross Amount: ${}\n".format("", distributor_laptop_gross_amount ))
    print("{:<30}13% VAT: ${}\n".format("", sum(product[5] for product in laptop_list)))
    print("{:<30}Total Amount: ${}\n".format("", distributor_total_invoice_amount))
    print("====================================================================================================================")
    print("")
    print("                                 THANK YOU FOR SHOPPING WITH US !!!")
    print("                                            VISIT AGAIN !!!")
    print("")
    print("====================================================================================================================")
   
# Function to write order invoice to .txt file
def write_order_invoice(distributor_name, laptop_list, distributor_laptop_gross_amount, distributor_total_invoice_amount, distributor_phone_no):
    filename = f"{distributor_name}_order_invoice.txt"
    with open(filename, "w") as file:
        file.write("====================================================================================================================\n")
        file.write("\n")
        file.write("                             KARKI ELECTRONICS AND LAPTOP SUPPLIERS                                              \n")
        file.write("                             KAPAN, KATHMANDU | CONTACT: 01-4270603                                              \n")
        file.write("\n")
        file.write("====================================================================================================================\n")
        file.write("                                         ORDER INVOICE\n")
        file.write("====================================================================================================================\n")
        file.write("Name of customer: " + str(distributor_name) + "\n")
        file.write("Phone no: " + str(distributor_phone_no) + "\n")
        file.write("Date: " + str(string_date_time) + "\n")
        file.write("====================================================================================================================\n")

        if laptop_list:
            file.write("------------------------------------------------------------------------------------------------------------\n")
            file.write("{:<15}{:<15}{:<15}{:<15}{:<15}\n".format("LAPTOP BRAND", "LAPTOP MODEL", "QUANTITY", "UNIT PRICE", "AMOUNT"))
            file.write("------------------------------------------------------------------------------------------------------------\n")
            for laptop in laptop_list:
                file.write("{:<15}{:<15}{:<15}{:<15}{:<15}\n".format(laptop[0], laptop[1], laptop[2], "$" + str(laptop[3]), "$" + str(laptop[4])))

        file.write("------------------------------------------------------------------------------------------------------------\n")
        file.write("{:<30}           Gross Amount:      ${}\n".format("", distributor_laptop_gross_amount))
        file.write("{:<30}           13% VAT:           ${}\n".format("", sum(product[5] for product in laptop_list)))
        file.write("{:<30}           Total Amount:      ${}\n".format("", distributor_total_invoice_amount))
        file.write("====================================================================================================================\n")
        file.write("\n")
        file.write("                                 THANK YOU FOR SHOPPING WITH US !!!\n")
        file.write("                                            VISIT AGAIN !!!\n")
        file.write("\n")
        file.write("====================================================================================================================\n")

       

# Function to display sell invoice
def generate_and_display_sell_invoice(sell_customer_name, laptop_list, sell_total_invoice_amount, sell_phone_no, sell_shipping_cost):
    """
    Function to generate and display the sell invoice
    """
    print("====================================================================================================================")
    print("")
    print("                             KARKI ELECTRONICS AND LAPTOP SUPPLIERS                                              ")
    print("                             KAPAN, KATHMANDU | CONTACT: 01-4270603                                              ")
    print("")
    print("====================================================================================================================")
    print("                                         SELL INVOICE")
    print("====================================================================================================================")
    print("CUSTOMER NAME:", sell_customer_name)
    print("PHONE NUMBER:", sell_phone_no)
    print("Date: " + str(string_date_time) + "\n")
    print("")
    print("====================================================================================================================")

    if laptop_list:
        print("------------------------------------------------------------------------------------------------------------")
        print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("LAPTOP BRAND", "LAPTOP MODEL", "QUANTITY", "UNIT PRICE", "AMOUNT"))
        print("------------------------------------------------------------------------------------------------------------")
        for laptop in laptop_list:
            print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(laptop[0], laptop[1], laptop[2], "$" + str(laptop[3]), "$" + str(laptop[4])))

    print("------------------------------------------------------------------------------------------------------------")
    print("                                             GROSS AMOUNT:", " $" + str(sell_total_invoice_amount))
    print("                                             SHIPPING COST:", "$" + str(sell_shipping_cost))
    print("------------------------------------------------------------------------------------------------------------")
    print("                                             TOTAL:","$" + str(sell_total_invoice_amount + sell_shipping_cost))
    print("====================================================================================================================")
    print("")
    print("                                 THANK YOU FOR SHOPPING WITH US !!!")
    print("                                            VISIT AGAIN !!!")
    print("")
    print("====================================================================================================================")

# Function to write sell invoice to .txt file
def write_sell_invoice(sell_customer_name, laptop_list, sell_total_invoice_amount, sell_phone_no, sell_shipping_cost):
    filename = f"{sell_customer_name}_sell_invoice.txt"
    with open(filename, "w") as file:
        file.write("====================================================================================================================\n")
        file.write("\n")
        file.write("                             KARKI ELECTRONICS AND LAPTOP SUPPLIERS                                              \n")
        file.write("                             KAPAN, KATHMANDU | CONTACT: 01-4270603                                              \n")
        file.write("\n")
        file.write("====================================================================================================================\n")
        file.write("                                         SELL INVOICE\n")
        file.write("====================================================================================================================\n")
        file.write("CUSTOMER NAME: " + sell_customer_name + "\n")
        file.write("PHONE NUMBER: " + sell_phone_no + "\n")
        file.write("Date: " + str(string_date_time) + "\n")
        file.write("\n")
        file.write("====================================================================================================================\n")

        if laptop_list:
            file.write("------------------------------------------------------------------------------------------------------------\n")
            file.write("{:<15}{:<15}{:<15}{:<15}{:<15}\n".format("LAPTOP BRAND", "LAPTOP MODEL", "QUANTITY", "UNIT PRICE", "AMOUNT"))
            file.write("------------------------------------------------------------------------------------------------------------\n")
            for laptop in laptop_list:
                file.write("{:<15}{:<15}{:<15}{:<15}{:<15}\n".format(laptop[0], laptop[1], laptop[2], "$" + str(laptop[3]), "$" + str(laptop[4])))

        file.write("------------------------------------------------------------------------------------------------------------\n")
        file.write("                                             GROSS AMOUNT: $" + str(sell_total_invoice_amount) + "\n")
        file.write("                                             SHIPPING COST: $" + str(sell_shipping_cost) + "\n")
        file.write("------------------------------------------------------------------------------------------------------------\n")
        file.write("                                             TOTAL:        $" + str(sell_total_invoice_amount + sell_shipping_cost) + "\n")
        file.write("====================================================================================================================\n")
        file.write("\n")
        file.write("                                 THANK YOU FOR SHOPPING WITH US !!!\n")
        file.write("                                            VISIT AGAIN !!!\n")
        file.write("\n")
        file.write("====================================================================================================================\n")
