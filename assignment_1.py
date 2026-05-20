"""college = input("Enter College Name: ")
course = input("Enter Course: ")
year = input("Enter Year: ")

print("\n--- College Information ---")
print(f"College: {college}")
print(f" Course: {course}")
print(f" Year: {year}")"""

"""t_name = input("Enter Teacher Name: ")
subject = input("Enter Subject: ")
exp = input("Enter Experience (years): ")

print("\n--- Teacher Profile ---")
print(f"Name: {t_name}\nSubject: {subject}\nExperience: {exp} years")"""

"""cust_name = input("Enter Customer Name: ")
acc_num = input("Enter Account Number: ")
branch = input("Enter Branch Name: ")

print("\n--- Bank Account Details ---")
print(f"Customer: {cust_name} | A/C: {acc_num} | Branch: {branch}")"""


"""p_name = input("Enter Patient Name: ")
p_id = input("Enter Patient ID: ")
disease = input("Enter Disease: ")

print("\n--- Medical Record ---")
print(f"Patient: {p_name}\nID: {p_id}\nDiagnosis: {disease}")"""

"""prod_name = input("Enter Product Name: ")
prod_id = input("Enter Product ID: ")
company = input("Enter Company Name: ")

print("\n--- Product Information ---")
print(f"Product: {prod_name} (ID: {prod_id}) - {company}")"""


"""brand = input("Enter Car Brand: ")
model = input("Enter Model Name: ")
color = input("Enter Color: ")

print(f"\nCar Info: {color} {brand} {model}")"""

"""brand = input("Enter Phone Brand: ")
model = input("Enter Model: ")
price = input("Enter Price: ")

print("\n--- Mobile Specifications ---")
print(f"Brand: {brand}\nModel: {model}\nPrice: {price}")"""

"""book = input("Enter Book Name: ")
author = input("Enter Author Name: ")
publisher = input("Enter Publisher: ")

print(f"\nBook: '{book}' by {author}. Published by {publisher}.")"""

"""s_name = input("Enter Student Name: ")
domain = input("Enter Internship Domain: ")
company = input("Enter Company Name: ")

print(f"\n{s_name} is interning in {domain} at {company}.")"""

"""movie = input("Enter Movie Name: ")
hero = input("Enter Hero Name: ")
director = input("Enter Director Name: ")

print(f"\nMovie: {movie} | Lead: {hero} | Directed by: {director}")"""

"""brand = input("Enter Laptop Brand: ")
processor = input("Enter Processor: ")
ram = input("Enter RAM (GB): ")

print("\n--- Laptop Specs ---")
print(f"Brand: {brand}, CPU: {processor}, RAM: {ram}GB")"""

"""pass_name = input("Enter Passenger Name: ")
source = input("Enter Source City: ")
dest = input("Enter Destination City: ")

print(f"\nTicket for {pass_name}: From {source} to {dest}.")"""

"""customer = input("Enter Customer Name: ")
food = input("Enter Food Item: ")
table = input("Enter Table Number: ")

print("\n--- Order Summary ---")
print(f"Table {table}: {food} for {customer}")"""

"""comp_name = input("Enter Company Name: ")
loc = input("Enter Location: ")
ceo = input("Enter CEO Name: ")

print(f"\nCompany: {comp_name}\nHeadquarters: {loc}\nCEO: {ceo}")"""

"""s_name = input("Enter Student Name: ")
course = input("Enter Course Name: ")
trainer = input("Enter Trainer Name: ")

print(f"\nRegistration Successful: {s_name} enrolled in {course} under {trainer}.")"""

"""p_name = input("Enter Participant Name: ")
event = input("Enter Event Name: ")
college = input("Enter College Name: ")

print(f"\n{p_name} from {college} has registered for {event}.")"""

"""user = input("Enter Username: ")
email = input("Enter Email: ")
password = input("Enter Password: ")

print("\n--- Account Info Collected ---")
print(f"Username: {user}\nEmail: {email}\nPassword: {'*' * len(password)} (Hidden for safety)")"""

# 1. Create and print a list
"""my_list = [10, 20, 30, 40, 50]
print("List:", my_list)

# 2. Access first and last
print(f"First: {my_list[0]}, Last: {my_list[-1]}")

# 3. Update first element
my_list[0] = 100
print("Updated List:", my_list)

# 4. Create and print a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# 5. First and last of tuple
print(f"First: {my_tuple[0]}, Last: {my_tuple[-1]}")

# 6. Try updating tuple (This will raise a TypeError)
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error observed: {e}")

# 7. Set with duplicates (Duplicates will be removed automatically)
my_set = {1, 2, 2, 3, 4, 4, 5}
print("Set (duplicates removed):", my_set)

# 8. Dictionary
my_dict = {"Name": "Bilal", "Age": 21, "RegNo": "ISL001"}
print("Dictionary:", my_dict)

# 9. Access Age
print("Age only:", my_dict["Age"])

# 10. Modify dictionary
my_dict["Age"] = 22
print("Updated Dictionary:", my_dict)"""

# 1. Integer to others
'''val = 10
print(f"Int to Float: {float(val)}, {type(float(val))}")
print(f"Int to Complex: {complex(val)}, {type(complex(val))}")
print(f"Int to Bool: {bool(val)}, {type(bool(val))}")
print(f"Int to String: {str(val)}, {type(str(val))}")

# 2. Float to others
val = 10.5
print(f"Float to Int: {int(val)}, {type(int(val))}")
print(f"Float to Complex: {complex(val)}, {type(complex(val))}")
print(f"Float to Bool: {bool(val)}, {type(bool(val))}")
print(f"Float to String: {str(val)}, {type(str(val))}")

# 3. Complex to others (Cannot convert complex to int or float)
val = 5+2j
print(f"Complex to Bool: {bool(val)}, {type(bool(val))}")
print(f"Complex to String: {str(val)}, {type(str(val))}")

# 4. Boolean to others
val = True
print(f"Bool to Int: {int(val)}, {type(int(val))}") # True = 1, False = 0
print(f"Bool to Float: {float(val)}, {type(float(val))}")
print(f"Bool to String: {str(val)}, {type(str(val))}")

# 5. String to others
val = "100"
print(f"Str to Int: {int(val)}, {type(int(val))}")
print(f"Str to List: {list(val)}, {type(list(val))}") # Breaks string into characters

# 6, 7, 8. Collections (List, Tuple, Set)
my_collection = [1, 2, 3]
print(f"List to Tuple: {tuple(my_collection)}")
print(f"List to Set: {set(my_collection)}")

# 9. Dictionary to others
my_map = {"a": 1, "b": 2}
print(f"Dict to List: {list(my_map)}") '''# Only converts keys


my_tuple = (1, 2, 3, 4, 5)

print("Simple Iteration:")
for item in my_tuple:
    print(item)  

print("\nIteration with Index:")
for index, item in enumerate(my_tuple): 
    print(f"Index: {index}, Value: {item}") 

print("\nIteration using range:") 
for i in range(len(my_tuple)):
    print(my_tuple[i])

my_tuple_new = (10, 20, 30, 40, 50)

print("\nPrinting constant for each element:")
for _ in my_tuple_new:  
    print("PK")


name_tuple = tuple("PK FROM UK")

print("\nTuple from String:")
for x in name_tuple:
    print(x) 


my_dict = {'a': 1, 'b': 2, 'c': 3}

print("\nDictionary Keys:")
for key in my_dict:
    print(key)

print("\nDictionary Items:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

print("\nDictionary Values:")
for value in my_dict.values(): 
    print(value)

my_set = {1, 2, 3, 4, 5}

print("\nSet Iteration:")
for element in my_set: 
    print(element)