# Hanoi Tower
This program implements an interactive graphical interface for the Towers of Hanoi game using the tkinter library in Python. The user can manually move the disks between the towers by selecting the source and destination towers. The program provides feedback on invalid moves and updates the graphical interface to reflect the current state of the game.

Description of the Code
Imports:

The tkinter and messagebox modules from tkinter are imported to create the graphical user interface (GUI) and display popup messages.
Class Pila (Stack):

The Pila class represents a stack of disks in the Towers of Hanoi game, serving as an abstract data structure.
Method __init__: Initializes the stack with a given capacity and an empty list of items.
Method vacia: Checks if the stack is empty.
Method insertar: Pushes a disk onto the stack.
Method suprimir: Pops and returns the top disk from the stack if it is not empty.
Method mostrar: Returns the list of disks in the stack.
Function VerificaMovimiento (Verify Move):

Verifies if a move of a disk from a source stack to a destination stack is valid.
Parameters: pila_origen (source stack) and pila_destino (destination stack), both instances of the Pila class.
Return: A tuple (valido, mensaje), where valido is a boolean indicating if the move is valid, and mensaje is a string explaining why the move is invalid.
Function mover_disco_manual (Move Disk Manually):

Moves a disk from a source stack to a destination stack if the move is valid.
Updates the graphical interface and checks if the game is completed.
Shows a warning message if the move is invalid.
Function seleccionar_pila (Select Stack):

Allows the user to select a source stack and a destination stack to move a disk.
Uses a global variable seleccion to store the selected stack.
Updates a label to show the selected stack.
Function actualizar_interfaz (Update Interface):

Updates the graphical interface to reflect the current state of the stacks.
Draws the towers and disks on a tkinter Canvas.
Function iniciar_juego (Start Game):

Initializes the game with the number of disks specified by the user.
Creates three stacks and places the disks on the first stack.
Initializes the global variable seleccion to None.
Graphical Interface Configuration:

Creates the main window using tkinter.
Adds an entry field for the user to input the number of disks.
Adds a button to start the game.
Creates a Canvas to draw the towers and disks.
Adds a label to show the selected stack.
Adds buttons for the user to select the stacks and move the disks manually.
Tutorial
Step 1: Setting Up the Environment
Make sure you have Python installed on your system. You can download it from python.org.

Step 2: Running the Program
Save the provided code into a file named main.py. Open a terminal or command prompt, navigate to the directory where main.py is located, and run the following command:

Step 3: Using the Program
Enter the Number of Disks:

In the entry field, input the number of disks you want to play with.
Click the "Iniciar Juego" button to start the game.
Select Source and Destination Stacks:

Click on the buttons labeled "Pila 1", "Pila 2", or "Pila 3" to select the source stack.
Click on another button to select the destination stack.
The program will attempt to move the top disk from the source stack to the destination stack.
Invalid Moves:

If you attempt an invalid move (e.g., moving a larger disk onto a smaller disk), a warning message will be displayed explaining why the move is invalid.
Completing the Game:

The game is completed when all disks are moved to the third stack.
A congratulatory message will be displayed when the game is completed.
Example Usage
Start the Program:

Run python main.py to start the program.
Input Number of Disks:

Enter 3 in the entry field and click "Iniciar Juego".
Move Disks:

Click "Pila 1" to select the source stack.
Click "Pila 3" to move the top disk from "Pila 1" to "Pila 3".
Repeat the process to move all disks to "Pila 3".
Invalid Move:

If you try to move a larger disk onto a smaller disk, a warning message will be displayed.
Complete the Game:

Move all disks to "Pila 3" to complete the game and see the congratulatory message.
With this interactive graphical interface, you can manually play the Towers of Hanoi game, receive feedback on invalid moves, and see the game state updated in real-time.