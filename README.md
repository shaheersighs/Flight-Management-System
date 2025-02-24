# Flight Management System 
This Python program implements a Flight Management System using Object-Oriented Programming (OOP) and Data Structures & Algorithms concepts. It allows users to insert, search, delete, and display records for passengers, pilots, flights, and bookings using a menu-driven interface. 

Object-Oriented Design

Implements five main classes:
Person (Parent), Passenger (Child), Pilot (Child), Flight and Booking.
Uses encapsulation (private variables, getters, setters) and inheritance (Passenger & Pilot inherit from Person).
Binary Tree for Passenger Management

A BinaryTree class manages passenger records.
Supports insert, search, delete, and update operations.
Search Algorithms

Linear Search: Iterates through a list to find an object.
Sorted Linear Search: Optimized for sorted lists.
Binary Search: Faster search on sorted lists.
Sorting Algorithms

Bubble Sort: Swaps adjacent elements.
Insertion Sort: Moves elements to their correct positions.
Selection Sort: Finds the smallest element and swaps.
File Processing

Saves records (passengers, pilots, flights, bookings) to text files.
Reads previously saved records when the program starts.
Interactive Menu (Jupyter Notebook Compatible)

Uses clear_output(wait=True) to refresh the screen in Jupyter Notebook.
Implements a main menu with submenus for Inserting records, Searching records, Deleting records, Displaying records, Saving records to a file, Validates user input to handle errors.

Program Flow:

Program starts & reads saved records.
User selects an option from the main menu.
Navigates to the respective submenu.
Performs operations (Insert, Search, Delete, Display).
Returns to the main menu after each operation.
User can save data or exit the program.

This Flight Management System demonstrates OOP principles, efficient data handling with Binary Trees, and classic sorting/searching algorithms. It provides an interactive text-based user interface that works efficiently in Jupyter Notebook.
 

