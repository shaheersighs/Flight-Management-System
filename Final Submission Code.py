"""


Final Project - Data Structures & Algorithms
Topic - Flight Management Systems

Muhammad Shaheer Khan

Content Table
Part 1 - Object Oriented Programming (Creating classes)
Part 2 - Data structure with objects (Binary Tree)
Part 3 - Searching and Sorting algorithms
Part 4 - File Processing Fucntions (Handling)
Part 5 - User interface (Main and submenus)
Part 6 - Helping Functions (Additional Part)
Part 7 - Execution

Execution - Scroll all the way down to the last block (Part 7 - Execution), & execute the program using the PYTHON DEBUGGER IN VS CODE.



"""


#-----------------------------------------------------------------------------------------------------------------------------


"""
------------------------------------------------------------------------------------------------------------------------------
Part 1 - Object Oriented Programming (Creating classes)
------------------------------------------------------------------------------------------------------------------------------
"""

class Person:
    """
    This is the parent class called 'Person', containing a constructor function for initialization, 
    getter functions and setter functions for setting and fetching attributes, and a string function 
    for displaying basic information and a user defined function for determining the age group of a person.
    """
    def __init__(self, name, age, ID):
        self.set_name(name)  # Set name attribute using setter function
        self.set_age(age)    # Set age attribute using setter function
        self.set_ID(ID)      # Set ID attribute using setter function

    def get_name(self):
        return self.__name  # Return the name attribute
    def get_age(self):
        return self.__age   # Return the age attribute
    def get_ID(self):
        return self.__ID    # Return the ID attribute

    def set_name(self, name):
        new_name = name.replace(" ", "-")  # Replace spaces in the name with dashes
        self.__name = new_name             # Set the modified name as the name attribute
    def set_age(self, age):
        if age <= 10:
            self.__age = 20   # Set default age as 20 if age is less than or equal to 10
        else:
            self.__age = age  # Set age as provided if greater than 10
    def set_ID(self, ID):
        self.__ID = ID        # Set the ID attribute
        
    def __str__(self):
        # Return a formatted string representing the person's details
        return f"Name: {self.get_name()} | Age: {self.get_age()} | ID: {self.get_ID()}"
    
    def get_age_group(self):
        # Determine the age group of the person.
        if self.get_age() <= 12:
            return "Child"
        elif 13 <= self.get_age() <= 64:
            return "Adult"
        else:
            return "Senior"


class Passenger(Person):
    """
    This is the child class called 'Passenger', inherited from the parent class 'Person', 
    containing a constructor function for initialization, getter and setter functions for setting 
    and fetching attributes, and a string function for displaying basic information.
    """
    def __init__(self, name, age, ID, ticket_num):
        super().__init__(name, age, ID)    # Call the parent class constructor
        self.set_ticket_num(ticket_num)    # Set ticket number using setter function

    def get_ticket_num(self):
        return self.__ticket_num           # Return the ticket number attribute
    def set_ticket_num(self, ticket_num):
        self.__ticket_num = ticket_num     # Set the ticket number attribute
        
    def __str__(self):
        # Return a formatted string representing the passenger's details including ticket number
        return super().__str__() + f" | Ticket Number: {self.get_ticket_num()}"
    
    def is_ticket_valid(self):
        # Check if the passenger's ticket number follows a valid format.
        ticket_num = self.get_ticket_num()
        return ticket_num.startswith("TK") 


class Pilot(Person):
    """
    This is the child class called 'Pilot', inherited from the parent class 'Person', containing a 
    constructor function for initialization, getter and setter functions for setting and fetching 
    attributes, and a string function for displaying basic information.
    """
    def __init__(self, name, age, ID, license_num):
        super().__init__(name, age, ID)    # Call the parent class constructor
        self.set_license_num(license_num)  # Set license number using setter function
        
    def get_license_num(self):
        return self.__license_num          # Return the license number attribute

    def set_license_num(self, license_num):
        self.__license_num = license_num   # Set the license number attribute

    def __str__(self):
        # Return a formatted string representing the pilot's details including license number
        return super().__str__() + f" | License Number: {self.get_license_num()}"
    
    def is_license_valid(self):
        # Verify if the pilot's license number follows a valid pattern.
        license_num = self.get_license_num()
        return license_num.startswith("PL") 


class Flight:
    """
    This is a class called 'Flight', containing a constructor function for initialization, 
    getter functions and setter functions for setting and fetching attributes, and a string function 
    for displaying basic information.
    """
    def __init__(self, flight_num, destination, departure_time):
        self.set_flight_num(flight_num)          # Set flight number using setter function
        self.set_destination(destination)        # Set destination using setter function
        self.set_departure_time(departure_time)  # Set departure time using setter function

    def get_flight_num(self):
        return self.__flight_num      # Return the flight number attribute
    def get_destination(self):
        return self.__destination     # Return the destination attribute
    def get_departure_time(self):
        return self.__departure_time  # Return the departure time attribute

    def set_flight_num(self, flight_num):
        self.__flight_num = flight_num          # Set the flight number attribute
    def set_destination(self, destination):
        self.__destination = destination        # Set the destination attribute
    def set_departure_time(self, departure_time):
        self.__departure_time = departure_time  # Set the departure time attribute

    def __str__(self):
        # Return a formatted string representing the flight's details
        return f"Flight Number: {self.get_flight_num()} | Destination: {self.get_destination()} | Departure time: {self.get_departure_time()}"

    def flight_summary(self):
        # Return a summary of the flight details.
        return f"Flight {self.get_flight_num()} to {self.get_destination()} departs at {self.get_departure_time()}."


class Booking:
    """
    This is a class called 'Booking', containing a constructor function for initialization, 
    getter functions and setter functions for setting and fetching attributes, and a string function 
    for displaying basic information.
    """
    def __init__(self, booking_id, passenger_name, flight_number):
        self.set_booking_id(booking_id)          # Set booking ID using setter function
        self.set_passenger_name(passenger_name)  # Set passenger name using setter function
        self.set_flight_number(flight_number)    # Set flight number using setter function

    def get_booking_id(self):
        return self.__booking_id      # Return the booking ID attribute
    def get_passenger_name(self):
        return self.__passenger_name  # Return the passenger name attribute
    def get_flight_number(self):
        return self.__flight_number   # Return the flight number attribute

    def set_booking_id(self, booking_id):
        self.__booking_id = booking_id          # Set the booking ID attribute
    def set_passenger_name(self, passenger_name):
        self.__passenger_name = passenger_name  # Set the passenger name attribute
    def set_flight_number(self, flight_number):
        self.__flight_number = flight_number    # Set the flight number attribute

    def __str__(self):
        # Return a formatted string representing the booking's details
        return f"Booking ID: {self.get_booking_id()} | Passenger Name: {self.get_passenger_name()} | Flight Number: {self.get_flight_number()}"

    def booking_summary(self):
        # Generate a summary of the booking details.
        return f"The booking ID is {self.get_booking_id()} for {self.get_passenger_name()} in the flight {self.get_flight_number()}"



"""
------------------------------------------------------------------------------------------------------------------------------
Part 2 - Data structure with objects (Binary Tree)
------------------------------------------------------------------------------------------------------------------------------
"""



class BinaryTree:
    """
    This class called 'BinaryTree', will create a binary tree data structure, which will be integrated
    to the class called 'Passenger' to execute functions like insert, search, delete, and update.
    These four functions will perform the programs that their names suggest, using the binary tree algorithm.
    """
    def __init__(self, root = None):
        self.set_root(root)   # Set the root of the tree
        self.set_left(None)   # Set the left child as None initially
        self.set_right(None)  # Set the right child as None initially

    def get_root(self):
        return self.__root   # Return the root of the tree
    def get_left(self):
        return self.__left   # Return the left child of the tree
    def get_right(self):
        return self.__right  # Return the right child of the tree

    def set_root(self, root):
        self.__root = root    # Set the root of the tree
    def set_left(self, left):
        self.__left = left    # Set the left child of the tree
    def set_right(self, right):
        self.__right = right  # Set the right child of the tree

    def compare_passenger(self, passenger1, passenger2):
        # Compare passengers based on their ID
        return passenger1.get_ID() < passenger2.get_ID()

    def insert_passenger(self, passenger):
        """
        This function will insert a passenger in the binary tree.
        """
        if self.__root:
            if self.compare_passenger(passenger, self.__root):
                if self.__left is None:
                    # Insert passenger as left child if no left child exists
                    self.__left = BinaryTree(passenger)
                else:
                    # Recurse to insert passenger in the left subtree
                    self.__left.insert_passenger(passenger)
            elif not self.compare_passenger(passenger, self.__root) and passenger.get_ID() != self.__root.get_ID():
                if self.__right is None:
                    # Insert passenger as right child if no right child exists
                    self.__right = BinaryTree(passenger)
                else:
                    # Recurse to insert passenger in the right subtree
                    self.__right.insert_passenger(passenger)
            else:
                print('The passenger already exists in the tree.')
        else:
                    # Set root as the passenger if tree is empty
            self.__root = passenger

    def search_passenger(self, passenger_id):
        """
        This function will search for a specific passenger in the binary tree based on their ID.
        """
        if self.__root:
            if passenger_id < self.__root.get_ID():
                if self.__left is None:
                    return False  # Return False if passenger not found in left subtree
                else:
                    return self.__left.search_passenger(passenger_id)
            elif passenger_id > self.__root.get_ID():
                if self.__right is None:
                    return False  # Return False if passenger not found in right subtree
                else:
                    return self.__right.search_passenger(passenger_id) 
            else:
                                  # Passenger found in the tree
                print("Passenger found:", self.__root)
                return True
        else:
            print("Error: the root of the tree is empty.")
            return False

    def delete_passenger(self, passenger_id):
        """
        This function will delete a passenger from the binary tree based on their ID.
        """
        if self is None:
                # Return self if the current node is None
            return self  

        if passenger_id < self.__root.get_ID():
            if self.__left is not None:
                # Recurse to delete passenger from the left subtree
                self.__left = self.__left.delete_passenger(passenger_id)
        elif passenger_id > self.__root.get_ID():
            if self.__right is not None:
                # Recurse to delete passenger from the right subtree
                self.__right = self.__right.delete_passenger(passenger_id)
        else:
                # Delete the node if the passenger ID matches
            return self._delete_node()

        return self

    def _delete_node(self):
        """
        This function will delete a node from the binary tree.
        """
        if self.__left is None and self.__right is None:
            return None          # Return None if the node has no children
        if self.__left is None:
            return self.__right  # Return the right child if no left child exists
        if self.__right is None:
            return self.__left   # Return the left child if no right child exists
        
            # Replace the node with the minimum value from the right subtree
        min_value = self.__right.find_min()
        self.__root = min_value
        self.__right = self.__right.delete_passenger(min_value.get_ID())
        return self

    def find_min(self):
        if self.__left is None:
            # Return the root if no left child exists
            return self.__root
        else:
            # Recurse to find the minimum value in the left subtree
            return self.__left.find_min()

    def update_passenger(self, target_id, new_passenger):
        """
        This function will update passenger information in the binary tree.
        """
        if self.__root:
            if target_id < self.__root.get_ID():
                if self.__left is not None:
                    # Recurse to update passenger in the left subtree
                    self.__left.update_passenger(target_id, new_passenger)
            elif target_id > self.__root.get_ID():
                if self.__right is not None:
                    # Recurse to update passenger in the right subtree
                    self.__right.update_passenger(target_id, new_passenger)
            else:
                    # Passenger found, updating to new details
                print(f"Passenger {target_id} found. Updating to new passenger details.")
                self.__root = new_passenger
        else:
            print("Error: the root of the tree is empty.")



"""
------------------------------------------------------------------------------------------------------------------------------
Part 3 - Searching and Sorting algorithms
------------------------------------------------------------------------------------------------------------------------------
"""



"""
The following three functions are search functions. They use the linear search, sorted linear search,
and binary search algorithms respectively, to search for the target from the objects.
"""
def linear_search(objects, target):
    # Normalize the target ID or number by stripping whitespace and converting to lowercase
    if isinstance(target, Passenger) or isinstance(target, Pilot):
        target_id = target.get_ID().strip().lower()
    elif isinstance(target, Flight):
        target_id = target.get_flight_num().strip().lower()
    elif isinstance(target, Booking):
        target_id = target.get_booking_id().strip().lower()
    else:
        return False  # Return False if target type is unrecognized

    # Iterate through each object to find the target by ID
    for obj in objects:
        if isinstance(target, Passenger) and obj.get_ID().strip().lower() == target_id:
            return True
        elif isinstance(target, Pilot) and obj.get_ID().strip().lower() == target_id:
            return True
        elif isinstance(target, Flight) and obj.get_flight_num().strip().lower() == target_id:
            return True
        elif isinstance(target, Booking) and obj.get_booking_id().strip().lower() == target_id:
            return True

    return False  # Return False if no match is found


def sorted_linear_search(objects, target):
    # Iterate through each object to find the target by ID in a sorted list
    for obj in objects:
        if isinstance(target, Passenger) and obj.get_ID() == target.get_ID():
            return True
        elif isinstance(target, Pilot) and obj.get_ID() == target.get_ID():
            return True
        elif isinstance(target, Flight) and obj.get_flight_num() == target.get_flight_num():
            return True
        elif isinstance(target, Booking) and obj.get_booking_id() == target.get_booking_id():
            return True
        # Since it's sorted, we can stop if we've passed the target
        elif isinstance(target, Passenger) and obj.get_ID() > target.get_ID():
            return False
        elif isinstance(target, Pilot) and obj.get_ID() > target.get_ID():
            return False
        elif isinstance(target, Flight) and obj.get_flight_num() > target.get_flight_num():
            return False
        elif isinstance(target, Booking) and obj.get_booking_id() > target.get_booking_id():
            return False
    return False

def binary_search(objects, target):
    # Binary search to find target in a sorted list
    low, high = 0, len(objects) - 1
    while low <= high:
        mid = (low + high) // 2
        obj = objects[mid]
        if isinstance(target, Passenger):
            obj_id, target_id = obj.get_ID(), target.get_ID()
        elif isinstance(target, Pilot):
            obj_id, target_id = obj.get_ID(), target.get_ID()
        elif isinstance(target, Flight):
            obj_id, target_id = obj.get_flight_num(), target.get_flight_num()
        elif isinstance(target, Booking):
            obj_id, target_id = obj.get_booking_id(), target.get_booking_id()
        else:
            return False
        
        if obj_id == target_id:
            return True
        elif obj_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return False

"""
The following functions are sorting functions. They insertion sort,
and selection sort algorithms respectively, to sort the objects.
"""

def insertion_sort(objects):
    # Insertion sort to arrange objects based on their ID
    for i in range(1, len(objects)):
        key = objects[i]
        j = i - 1
        while j >= 0:
            if isinstance(key, Passenger) and key.get_ID() < objects[j].get_ID():
                objects[j + 1] = objects[j]
            elif isinstance(key, Pilot) and key.get_ID() < objects[j].get_ID():
                objects[j + 1] = objects[j]
            elif isinstance(key, Flight) and key.get_flight_num() < objects[j].get_flight_num():
                objects[j + 1] = objects[j]
            elif isinstance(key, Booking) and key.get_booking_id() < objects[j].get_booking_id():
                objects[j + 1] = objects[j]
            else:
                break
            j -= 1
        objects[j + 1] = key
    return objects

def selection_sort(objects):
    # Selection sort to arrange objects based on their ID
    n = len(objects)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if isinstance(objects[i], Passenger) and objects[j].get_ID() < objects[min_index].get_ID():
                min_index = j
            elif isinstance(objects[i], Pilot) and objects[j].get_ID() < objects[min_index].get_ID():
                min_index = j
            elif isinstance(objects[i], Flight) and objects[j].get_flight_num() < objects[min_index].get_flight_num():
                min_index = j
            elif isinstance(objects[i], Booking) and objects[j].get_booking_id() < objects[min_index].get_booking_id():
                min_index = j
        objects[i], objects[min_index] = objects[min_index], objects[i]
    return objects



"""
------------------------------------------------------------------------------------------------------------------------------
Part 4 - File Processing Fucntions (Handling)
------------------------------------------------------------------------------------------------------------------------------
"""



import os

def save_new_records(filename, object_list):
    """
    Appends only new records to the file, preventing duplication.
    """
    existing_records = read_from_file(filename, type(object_list[0])) if object_list else []

    # Convert current records in memory to strings
    current_records = set(str(obj) for obj in existing_records)
    new_records = [obj for obj in object_list if str(obj) not in current_records]

    if not new_records:
        print("")
        print(f"No new records to save in {filename}.")
        print("")
        return
    with open(filename, 'a') as file:
        for obj in new_records:
            file.write(str(obj) + '\n')
     
    print("")
    print(f"New records saved to {filename} successfully!")
    print("")


def overwrite_file_with_updated_records(filename, object_list):
    """
    Overwrites the file with the current list of objects after deletion or modification.
    """
    with open(filename, 'w') as file:
        for obj in object_list:
            file.write(str(obj) + '\n')

    print("")
    print(f"File {filename} overwritten with updated records successfully!")
    print("")


def read_from_file(filename, class_type):
    if not os.path.exists(filename):
        return []

    object_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            attributes = line.strip().split(' | ')
            if class_type == Passenger and len(attributes) == 4:
                try:
                    name = attributes[0].split(': ')[1]
                    age = int(attributes[1].split(': ')[1])
                    ID = attributes[2].split(': ')[1]
                    ticket_num = attributes[3].split(': ')[1]
                    obj = Passenger(name, age,ID, ticket_num)
                except IndexError:
                    continue
                
            elif class_type == Pilot and len(attributes) == 4:
                try:
                    name = attributes[0].split(': ')[1]
                    age = int(attributes[1].split(': ')[1])
                    ID = attributes[2].split(': ')[1]
                    license_num = attributes[3].split(': ')[1]
                    obj = Pilot(name, age, ID, license_num)
                except IndexError:
                    continue
                
            elif class_type == Flight and len(attributes) == 3:
                try:
                    flight_num = attributes[0].split(': ')[1]
                    destination = attributes[1].split(': ')[1]
                    departure_time = attributes[2].split(': ')[1]
                    obj = Flight(flight_num, destination, departure_time)
                except IndexError:
                    continue
                
            elif class_type == Booking and len(attributes) == 3:
                try:
                    booking_id = attributes[0].split(': ')[1]
                    passenger_name = attributes[1].split(': ')[1]
                    flight_number = attributes[2].split(': ')[1]
                    obj = Booking(booking_id, passenger_name, flight_number)
                except IndexError:
                    continue
                
            else:
                continue
            
            object_list.append(obj)
    
    return object_list


# Get the directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define file paths using the absolute path
PASSENGER_FILE = os.path.join(base_dir, 'passenger_records.txt')
PILOT_FILE = os.path.join(base_dir, 'pilot_records.txt')
FLIGHT_FILE = os.path.join(base_dir, 'flight_records.txt')
BOOKING_FILE = os.path.join(base_dir, 'booking_records.txt')

# Global lists for each class to store records
passenger_list = []
pilot_list = []
flight_list = []
booking_list = []

# Function to load data from file at startup
def load_all_records():
    global passenger_list, pilot_list, flight_list, booking_list
    passenger_list.clear()
    pilot_list.clear()
    flight_list.clear()
    booking_list.clear()
    
    passenger_list = read_from_file(PASSENGER_FILE, Passenger)
    pilot_list = read_from_file(PILOT_FILE, Pilot)
    flight_list = read_from_file(FLIGHT_FILE, Flight)
    booking_list = read_from_file(BOOKING_FILE, Booking)
    
    print("All records loaded successfully from files.")

# Function to save all records to files
def save_all_records():
    os.system('clear')
    save_new_records(PASSENGER_FILE, passenger_list)
    save_new_records(PILOT_FILE, pilot_list)
    save_new_records(FLIGHT_FILE, flight_list)
    save_new_records(BOOKING_FILE, booking_list)

    print("\nAll records have been saved to their respective files.\n")
    time.sleep(2)


# Function to display loaded records (reads directly from files)
def display_loaded_records():
    os.system('clear')
    print("")
    print("Displaying records directly from files:")
    print("")
    print("Passengers:")
    print("")
    for record in read_from_file(PASSENGER_FILE, Passenger):
        print(record)
    print("\nPilots:")
    print("")
    for record in read_from_file(PILOT_FILE, Pilot):
        print(record)
    print("\nFlights:")
    print("")
    for record in read_from_file(FLIGHT_FILE, Flight):
        print(record)
    print("\nBookings:")
    print("")
    for record in read_from_file(BOOKING_FILE, Booking):
        print(record)
    input("\nPress Enter to return to the main menu.")



"""
------------------------------------------------------------------------------------------------------------------------------
Part 5 - User interface (Main and submenus)
------------------------------------------------------------------------------------------------------------------------------
"""



import os
import time

# Main Menu
def main_menu():
    """
    Displays the main menu and handles user input to navigate to other menus or perform actions.
    Continuously loops until the user chooses to exit.
    """
    while True:
        os.system('clear')  # Clears the console for a fresh menu display
        print("---------------------")
        print("      Main Menu      ")
        print("---------------------")
        print("")
        print("1. Passenger Management")
        print("")
        print("2. Insert Record")
        print("")
        print("3. Search Record")
        print("")
        print("4. Delete Record")
        print("")
        print("5. Display Records")
        print("")
        print("6. Write All Unsaved Records to File")
        print("")
        print("7. Display Loaded Records from File")
        print("")
        print("8. Exit")
        print("")
        choice = input("Select an option (1-8): ")
            
        if choice == "1":
            passenger_management_menu()  # Go to Passenger Management submenu
        elif choice == "2":
            insert_menu()  # Navigate to Insert Menu for other classes
        elif choice == "3":
            search_menu()  # Navigate to Search Menu for other classes
        elif choice == "4":
            delete_menu()  # Navigate to Delete Menu for other classes
        elif choice == "5":
            display_menu()  # Navigate to Display Menu for other classes
        elif choice == "6":
            save_all_records()  # Save all unsaved records to files
        elif choice == "7":
            display_loaded_records()  # Display records loaded from files
        elif choice == "8":
            print("")
            print("Exiting the program, Goodbye!")
            time.sleep(1.5)
            print("")
            os.system('clear')
            break  # Exit the program
        else:
            print("")
            print("Invalid choice, please try again.")  # Handle invalid input
            time.sleep(1.5)

# Passenger Management Menu for BinaryTree Operations
def passenger_management_menu():
    """
    Submenu for managing Passenger records in the BinaryTree.
    Allows insertion, deletion, searching, and updating of Passenger records.
    """
    
    binary_tree = BinaryTree()  # Instantiate a BinaryTree object for Passenger operations
    # Load existing passengers from file into the binary tree based on age
    global passenger_list
    passenger_list = read_from_file(PASSENGER_FILE, Passenger)
    for passenger in passenger_list:
        binary_tree.insert_passenger(passenger)

    while True:
        os.system('clear')
        print("---------------------------")
        print(" Passenger Management Menu ")
        print("---------------------------")
        print("")
        print("1. Insert a Passenger")
        print("")
        print("2. Search for a Passenger by ID")
        print("")
        print("3. Delete a Passenger by ID")
        print("")
        print("4. Update Passenger Information")
        print("")
        print("5. Display Passengers")
        print("")
        print("6. Back to Main Menu")
        print("")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            insert_passenger_tree(binary_tree)  # Insert a Passenger
        elif choice == "2":
            search_passenger_tree(binary_tree)  # Search for a Passenger
        elif choice == "3":
            delete_passenger_tree(binary_tree)  # Delete a Passenger
        elif choice == "4":
            update_passenger_tree(binary_tree)  # Update a Passenger
        elif choice == "5":
            display_passenger_records_tree()  # Display Passengers
        elif choice == "6":
            break  # Return to the main menu
        else:
            print("\nInvalid choice, please try again.")
            time.sleep(1.5)

# Insert Menu
def insert_menu():
    """
    Displays the insert menu and allows the user to insert a record into one of the categories.
    Handles the insertion process and confirmation of record addition.
    """
    while True:
        os.system('clear')
        print("---------------------")
        print("     Insert Menu     ")
        print("---------------------")
        print("")
        print("1. Insert into Passenger")
        print("")
        print("2. Insert into Pilot")
        print("")
        print("3. Insert into Flight")
        print("")
        print("4. Insert into Booking")
        print("")
        print("5. Write Records to File")
        print("")
        print("6. Back to Main Menu")
        print("")
        
        choice = input("Select an option (1-6): ")
        
        if choice == "1":
            add_passenger()  # Add a passenger record
        elif choice == "2":
            add_pilot()  # Add a pilot record
        elif choice == "3":
            add_flight()  # Add a flight record
        elif choice == "4":
            add_booking()  # Add a booking record
        elif choice == "5":
            print("")
            filename = input("Enter filename to save current records: ")
            combined_records = passenger_list + pilot_list + flight_list + booking_list
            save_new_records(filename, combined_records)
            print("")
            input("Press Enter to return to the insert menu: ")  # Pause to view confirmation
        elif choice == "6":
            break  # Go back to main menu
        else:
            print("")
            print("Invalid choice, please try again.")
            time.sleep(1.5)


# Search Menu
def search_menu():
    """
    Displays the search menu and allows the user to search for a record in each category.
    """
    while True:
        os.system('clear')
        print("---------------------")
        print("     Search Menu     ")
        print("---------------------")
        print("")
        print("1. Search Passenger")
        print("")
        print("2. Search Pilot")
        print("")
        print("3. Search Flight")
        print("")
        print("4. Search Booking")
        print("")
        print("5. Back to Main Menu")
        print("")
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            search_passenger()  # Search a passenger record
        elif choice == "2":
            search_pilot()  # Search a pilot record
        elif choice == "3":
            search_flight()  # Search a flight record
        elif choice == "4":
            search_booking()  # Search a booking record
        elif choice == "5":
            break  # Go back to main menu
        else:
            print("")
            print("Invalid choice, please try again.")
            time.sleep(1.5)


# Delete Menu
def delete_menu():
    """
    Displays the delete menu and allows the user to delete a record in each category.
    """
    while True:
        os.system('clear')
        print("---------------------")
        print("     Delete Menu     ")
        print("---------------------")
        print("")
        print("1. Delete Passenger")
        print("")
        print("2. Delete Pilot")
        print("")
        print("3. Delete Flight")
        print("")
        print("4. Delete Booking")
        print("")
        print("5. Back to Main Menu")
        print("")
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            delete_passenger()  # Delete a passenger record
        elif choice == "2":
            delete_pilot()  # Delete a pilot record
        elif choice == "3":
            delete_flight()  # Delete a flight record
        elif choice == "4":
            delete_booking()  # Delete a booking record
        elif choice == "5":
            break  # Go back to main menu
        else:
            print("")
            print("Invalid choice, please try again.")
            time.sleep(1.5)


# Display Menu
def display_menu():
    """
    Displays the display menu and allows the user to view all records in each category.
    """
    while True:
        os.system('clear')
        print("----------------------")
        print("     Display Menu     ")
        print("----------------------")
        print("1. Display Passenger Records")
        print("")
        print("2. Display Pilot Records")
        print("")
        print("3. Display Flight Records")
        print("")
        print("4. Display Booking Records")
        print("")
        print("5. Back to Main Menu")
        print("")
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            display_passenger_records()  # Display all passenger records
        elif choice == "2":
            display_pilot_records()  # Display all pilot records
        elif choice == "3":
            display_flight_records()  # Display all flight records
        elif choice == "4":
            display_booking_records()  # Display all booking records
        elif choice == "5":
            break  # Go back to main menu
        else:
            print("Invalid choice, please try again.")
            time.sleep(1.5)


def write_all_records_to_files():
    """
    Saves all records from each category to separate text files.
    """
    save_new_records('passenger_records.txt', passenger_list)
    save_new_records('pilot_records.txt', pilot_list)
    save_new_records('flight_records.txt', flight_list)
    save_new_records('booking_records.txt', booking_list)
    print("")
    print("All records saved to the files.")
    time.sleep(2.0)



"""
------------------------------------------------------------------------------------------------------------------------------
Part 6 - Helping Functions (Additional Part)
------------------------------------------------------------------------------------------------------------------------------
"""

"""
-----------------------------------------------------------------
The passenger helper functions.
-----------------------------------------------------------------
""" 

def insert_passenger_tree(binary_tree):
    os.system('clear')
    print("---------------------------")
    print("    Insert a Passenger     ")
    print("---------------------------")
    print("")
    name = input("Enter passenger name: ")
    print("")
    age = int(input("Enter passenger age: "))
    print("")
    ID = input("Enter passenger ID: ")
    print("")
    ticket_num = input("Enter ticket number: ")
    print("")

    # Insert into binary tree
    new_passenger = Passenger(name, age, ID, ticket_num)
    binary_tree.insert_passenger(new_passenger)

    # Also add to passenger list and save to file
    passenger_list.append(new_passenger)
    save_new_records(PASSENGER_FILE, passenger_list)

    print("\nPassenger inserted successfully!")
    print("")
    input("Press Enter to return to the menu.")


def search_passenger_tree(binary_tree):
    global passenger_list  # Access the global list for displaying full details
    os.system('clear')
    print("---------------------------")
    print("    Search for a Passenger ")
    print("---------------------------")
    print("")
    passenger_id = input("Enter passenger ID to search: ")
    print("")

    # Search in the binary tree by ID
    found = binary_tree.search_passenger(passenger_id)
    
    # Display results based on whether the passenger was found
    if found:
        # Fetch details from the passenger list or file for full information
        passenger_list = read_from_file(PASSENGER_FILE, Passenger)  # Refresh list from file
        for passenger in passenger_list:
            if passenger.get_ID() == passenger_id:
                # Display only the passenger details without additional "found" messages
                print("\nPassenger Details:")
                print(passenger)
                break
    else:
        print("\nPassenger not found.")
    
    print("")
    input("Press Enter to return to the menu.")


def delete_passenger_tree(binary_tree):
    os.system('clear')
    print("---------------------------")
    print("    Delete a Passenger     ")
    print("---------------------------")
    print("")
    passenger_id = input("Enter passenger ID to delete: ")
    print("")

    # Delete from binary tree
    binary_tree.delete_passenger(passenger_id)
    
    # Update the global list and save to file
    initial_count = len(passenger_list)
    passenger_list = [p for p in passenger_list if p.get_ID() != passenger_id]
    if len(passenger_list) < initial_count:
        overwrite_file_with_updated_records(PASSENGER_FILE, passenger_list)
        print(f"\nPassenger with ID {passenger_id} deleted successfully from file.")
    else:
        print("Passenger not found. Please enter a valid ID.")
    print("")
    input("Press Enter to return to the menu.")


def update_passenger_tree(binary_tree):
    os.system('clear')
    print("---------------------------")
    print("  Update Passenger Details ")
    print("---------------------------")
    print("")
    passenger_id = input("Enter passenger ID to update: ")
    print("")

    # Gather new details for the update
    name = input("Enter new name: ")
    print("")
    age = int(input("Enter new age: "))
    print("")
    ID = passenger_id  # Keep the same ID for the update
    ticket_num = input("Enter new ticket number: ")
    print("")
    updated_passenger = Passenger(name, age, ID, ticket_num)
    
    # Update in the binary tree
    binary_tree.update_passenger(passenger_id, updated_passenger)
    
    # Update in the passenger list and save to file
    for idx, passenger in enumerate(passenger_list):
        if passenger.get_ID() == passenger_id:
            passenger_list[idx] = updated_passenger  # Update the list
            break
    
    overwrite_file_with_updated_records(PASSENGER_FILE, passenger_list)
    print("\nPassenger updated successfully and changes saved to file.")
    print("")
    input("Press Enter to return to the menu.")


def display_passenger_records_tree():
    os.system('clear')
    print("-----------------------")
    print("  List of Passengers   ")
    print("-----------------------")
    print("")
    
    # Load passenger records from the file to ensure latest changes are displayed
    passenger_list_from_file = read_from_file(PASSENGER_FILE, Passenger)
    
    if passenger_list_from_file:
        for passenger in passenger_list_from_file:
            print(passenger)  # Display each passenger
    else:
        print("No passenger records found.")  # Message if list is empty
    
    print("")
    input("Press Enter to return to the menu.")


"""
-----------------------------------------------------------------
The passenger helper functions.
-----------------------------------------------------------------
"""  

def add_passenger():
    global passenger_list  # Access the global list
    os.system('clear')
    print("-----------------------")
    print("     Add Passenger     ")
    print("-----------------------")
    print("")
    name = input("Enter passenger name: ")
    print("")
    age = int(input("Enter passenger age: "))
    print("")
    ID = input("Enter passenger ID: ")
    print("")
    ticket_num = input("Enter ticket number: ")
    print("")
    # Create a new Passenger object and add it to the list
    new_passenger = Passenger(name, age, ID, ticket_num)
    passenger_list.append(new_passenger)  # Add to the passenger list
    # Save only the new record to avoid duplication
    save_new_records(PASSENGER_FILE, passenger_list)
    print("Passenger record added successfully!")
    print("")
    input("Press Enter to return to the menu: ")


def search_passenger():
    # Reload passenger records from the file to ensure any changes are captured
    global passenger_list
    passenger_list = read_from_file('passenger_records.txt', Passenger)  # Reload data from file
    os.system('clear')
    print("-----------------------")
    print("   Search Passenger    ")
    print("-----------------------")
    print("")
    passenger_id = input("Enter passenger ID to search: ")  # Get ID to search
    found = linear_search(passenger_list, Passenger("", 0, passenger_id, ""))  # Search passenger
    print("")
    print(f"Passenger {'found' if found else 'not found'}.")  # Display result
    print("")
    input("Press Enter to return to the menu: ")


def delete_passenger():
    global passenger_list  # Access the global list
    os.system('clear')
    print("-----------------------")
    print("   Delete Passenger    ")
    print("-----------------------")
    print("")
    passenger_id = input("Enter passenger ID to delete: ")
    print("")
    # Find and remove the passenger
    initial_count = len(passenger_list)
    passenger_list = [p for p in passenger_list if p.get_ID() != passenger_id]
    if len(passenger_list) < initial_count:
        # Overwrite the file with the updated list after deletion
        overwrite_file_with_updated_records(PASSENGER_FILE, passenger_list)
        print(f"Passenger with ID {passenger_id} deleted successfully.")
    else:
        print("Passenger not found. Please enter a valid ID.")
    print("")
    input("Press Enter to return to the menu: ")


def display_passenger_records():
    os.system('clear')
    print("-----------------------")
    print("  List of Passengers   ")
    print("-----------------------")
    print("")
    if passenger_list:
        for passenger in passenger_list:
            print(passenger)  # Display each passenger
    else:
        print("No passenger records found.")  # Message if list is empty
    print("")
    input("Press Enter to return to the menu: ")

"""
-----------------------------------------------------------------
The flight helper functions.
-----------------------------------------------------------------
"""  

def add_pilot():
    global pilot_list  # Access the global list
    os.system('clear')
    print("-----------------------")
    print("       Add Pilot       ")
    print("-----------------------")
    print("")
    name = input("Enter pilot name: ")
    print("")
    age = int(input("Enter pilot age: "))
    print("")
    ID = input("Enter pilot ID: ")
    print("")
    license_num = input("Enter license number: ")
    print("")
    # Create a new Pilot object and add it to the list
    new_pilot = Pilot(name, age, ID, license_num)
    pilot_list.append(new_pilot)
    # Save only the new record to avoid duplication
    save_new_records(PILOT_FILE, pilot_list)
    print("Pilot record added successfully!")
    print("")
    input("Press Enter to return to the menu: ")


def search_pilot():
    # Reload Pilot records from the file to ensure any changes are captured
    global pilot_list
    pilot_list = read_from_file('pilot_records.txt', Pilot)  # Reload data from file
    os.system('clear')
    print("-----------------------")
    print("     Search Pilot      ")
    print("-----------------------")
    print("")
    pilot_id = input("Enter pilot ID to search: ")  # Get ID to search
    found = linear_search(pilot_list, Pilot("", 0, pilot_id, ""))  # Search pilot
    print("")
    print(f"Pilot {'found' if found else 'not found'}.")  # Display result
    print("")
    input("Press Enter to return to the menu: ")


def delete_pilot():
    global pilot_list  # Access the global list
    os.system('clear')
    print("-----------------------")
    print("     Delete Pilot      ")
    print("-----------------------")
    print("")
    pilot_id = input("Enter pilot ID to delete: ")
    print("")
    # Find and remove the pilot
    initial_count = len(pilot_list)
    pilot_list = [p for p in pilot_list if p.get_ID() != pilot_id]
    if len(pilot_list) < initial_count:
        # Overwrite the file with the updated list after deletion
        overwrite_file_with_updated_records(PILOT_FILE, pilot_list)
        print(f"Pilot with ID {pilot_id} deleted successfully.")
    else:
        print("Pilot not found. Please enter a valid ID.")
    print("")
    input("Press Enter to return to the menu: ")


def display_pilot_records():
    os.system('clear')
    print("-----------------------")
    print("    List of Pilots     ")
    print("-----------------------")
    print("")
    if pilot_list:
        for pilot in pilot_list:
            print(pilot)  # Display each pilot
    else:
        print("No pilot records found.")  # Message if list is empty
    print("")
    input("Press Enter to return to the menu: ")

"""
-----------------------------------------------------------------
The flight helper functions.
-----------------------------------------------------------------
"""  

def add_flight():
    global flight_list  # Access the global list
    os.system('clear')
    print("-----------------------")
    print("      Add Flight       ")
    print("-----------------------")
    print("")
    flight_num = input("Enter flight number: ")
    print("")
    destination = input("Enter destination: ")
    print("")
    departure_time = input("Enter departure time (e.g., 10:30 AM): ")
    print("")
    # Create a new Flight object and add it to the list
    new_flight = Flight(flight_num, destination, departure_time)
    flight_list.append(new_flight)
    # Save only the new record to avoid duplication
    save_new_records(FLIGHT_FILE, flight_list)
    print("Flight record added successfully!")
    print("")
    input("Press Enter to return to the menu: ")


def search_flight():
    # Reload flight records from the file to ensure any changes are captured
    global flight_list
    flight_list = read_from_file('flight_records.txt', Flight)  # Reload data from file
    os.system('clear')
    print("-----------------------")
    print("    Search Flight      ")
    print("-----------------------")
    print("")
    flight_num = input("Enter flight number to search: ")  # Get flight number to search
    found = linear_search(flight_list, Flight(flight_num, "", ""))  # Search flight
    print("")
    print(f"Flight {'found' if found else 'not found'}.")  # Display result
    print("")
    input("Press Enter to return to the menu: ")


def delete_flight():
    global flight_list  # Access the global list
    os.system('clear')
    print("-----------------------")
    print("    Delete Flight      ")
    print("")
    flight_num = input("Enter flight number to delete: ")
    print("")
    # Find and remove the flight
    initial_count = len(flight_list)
    flight_list = [f for f in flight_list if f.get_flight_num() != flight_num]
    if len(flight_list) < initial_count:
        # Overwrite the file with the updated list after deletion
        overwrite_file_with_updated_records(FLIGHT_FILE, flight_list)
        print(f"Flight with number {flight_num} deleted successfully.")
    else:
        print("Flight not found. Please enter a valid flight number.")
    print("")
    input("Press Enter to return to the menu: ")


def display_flight_records():
    os.system('clear')
    print("-----------------------")
    print("    List of Flights    ")
    print("-----------------------")
    print("")
    if flight_list:
        for flight in flight_list:
            print(flight)  # Display each flight
    else:
        print("No flight records found.")  # Message if list is empty
    print("")
    input("Press Enter to return to the menu: ")

"""
-----------------------------------------------------------------
The booking helper functions.
-----------------------------------------------------------------
"""   

def add_booking():
    global booking_list  # Access the global list
    os.system('clear')
    print("-----------------------")
    print("     Add Booking       ")
    print("")
    booking_id = input("Enter booking ID: ")
    print("")
    passenger_name = input("Enter passenger name: ")
    print("")
    flight_number = input("Enter flight number: ")
    print("")
    # Create a new Booking object and add it to the list
    new_booking = Booking(booking_id, passenger_name, flight_number)
    booking_list.append(new_booking)
    # Save only the new record to avoid duplication
    save_new_records(BOOKING_FILE, booking_list)
    print("Booking record added successfully!")
    print("")
    input("Press Enter to return to the menu: ")


def search_booking():
    # Reload passenger records from the file to ensure any changes are captured
    global booking_list
    booking_list = read_from_file('booking_records.txt', Booking)  # Reload data from file
    
    os.system('clear')
    print("-----------------------")
    print("    Search Booking     ")
    print("-----------------------")
    print("")
    booking_id = input("Enter booking ID to search: ")  # Get booking ID to search
    found = linear_search(booking_list, Booking(booking_id, "", ""))  # Search booking
    print("")
    print(f"Booking {'found' if found else 'not found'}.")  # Display result
    print("")
    input("Press Enter to return to the menu: ")


def delete_booking():
    global booking_list  # Access the global list
    os.system('clear')
    print("-----------------------")
    print("    Delete Booking     ")
    print("")
    booking_id = input("Enter booking ID to delete: ")
    print("")
    # Find and remove the booking
    initial_count = len(booking_list)
    booking_list = [b for b in booking_list if b.get_booking_id() != booking_id]
    if len(booking_list) < initial_count:
        # Overwrite the file with the updated list after deletion
        overwrite_file_with_updated_records(BOOKING_FILE, booking_list)
        print(f"Booking with ID {booking_id} deleted successfully.")
    else:
        print("Booking not found. Please enter a valid ID.")
    print("")
    input("Press Enter to return to the menu: ")


def display_booking_records():
    os.system('clear')
    print("-----------------------")
    print("   List of Bookings    ")
    print("-----------------------")
    print("")
    if booking_list:
        for booking in booking_list:
            print(booking)  # Display each booking
    else:
        print("No booking records found.")  # Message if list is empty
    print("")   
    input("Press Enter to return to the menu: ")



"""
------------------------------------------------------------------------------------------------------------------------------
Part 7 - Execution
------------------------------------------------------------------------------------------------------------------------------
"""


if __name__ == "__main__":
    load_all_records()
    main_menu()