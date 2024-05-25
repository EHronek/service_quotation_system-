#import tkinter as tk

# Function to read counters from the file
def read_counters():
    counters = {}
    try:
        with open("id_counters.txt", "r") as file:
            for line in file:
                table, counter = line.strip().split(":")
                counters[table] = int(counter)
    except FileNotFoundError:
        counters = {"client_counter": 0, "quotation_counter": 0, "organization_counter": 0, 'employee_counter': 0}
    return counters

# Function to write counters to the file
def write_counters(counters):
    with open("id_counters.txt", "w") as file:
        for table, counter in counters.items():
            file.write(f"{table}:{counter}\n")

# Function to generate a new ID
def generate_id(prefix, table_counter):
    counters = read_counters()
    counter = counters[table_counter]
    new_id = f"{prefix}_{counter:03d}"
    counters[table_counter] += 1
    write_counters(counters)
    return new_id

# Example usage
""" def create_ids():
    customer_id = generate_id("CT", "customer_counter")
    quotation_id = generate_id("QT", "quotation_counter")
    organization_id = generate_id("OT", "organization_counter")

    print(f"Customer ID: {customer_id}")
    print(f"Quotation ID: {quotation_id}")
    print(f"Organization ID: {organization_id}") """


def create_client_id():
    customer_id = generate_id("CT", "client_counter")
    return str(customer_id)

def create_quote_id():
    quote_id = generate_id("QT", "quotation_counter")
    return str(quote_id)

def employee_id():
    emp_id = generate_id("EMP", "employee_counter")
    return str(emp_id)





""" # Create the main window
root = tk.Tk()
root.title("ID Generator Example")

# Create a button to generate new IDs
generate_button = tk.Button(root, text="Generate IDs", command=employee_id)
generate_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
 """