import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Function to open the quiz window
def open_quiz_window(category):
    # Close the main window
    main_window.destroy()
    
    # Create a new window for the quiz
    quiz_window = tk.Tk()
    quiz_window.title(f"{category} Quiz")

    # Establish connection to the database
    conn = sqlite3.connect("questions.db")
    cursor = conn.cursor()
    
    # Fetch questions from the selected category
    cursor.execute(f"SELECT question, option_a, option_b, option_c, option_d, correct_answer FROM {category}")
    questions = cursor.fetchall()
    conn.close()
    
    # Initialize current question index
    current_question = [0]  # Use a mutable object to keep track of the index across function calls
    
    # Variable to store the user's selected answer
    user_answer = tk.StringVar(value="")  # Set to empty string to avoid preselection

    # Function to display the next question
    def display_question():
        if current_question[0] < len(questions):
            question_text, opt_a, opt_b, opt_c, opt_d, correct_answer = questions[current_question[0]]
            question_label.config(text=question_text)
            option_a_rb.config(text=opt_a, value='A')
            option_b_rb.config(text=opt_b, value='B')
            option_c_rb.config(text=opt_c, value='C')
            option_d_rb.config(text=opt_d, value='D')
            # Clear previous selection
            user_answer.set("")  # Reset the selection for each new question
        else:
            messagebox.showinfo("Quiz Complete", "You've completed the quiz!")
            quiz_window.destroy()

    # Function to check the answer and move to the next question
    def submit_answer():
        if user_answer.get() == questions[current_question[0]][5]:  # Check against correct_answer
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", "Incorrect. Try Again.")
        
        # Move to the next question
        current_question[0] += 1
        display_question()
    
    # Widgets for displaying questions and options
    question_label = tk.Label(quiz_window, text="")
    question_label.pack()
    
    # Create radio buttons for options
    option_a_rb = tk.Radiobutton(quiz_window, variable=user_answer)
    option_b_rb = tk.Radiobutton(quiz_window, variable=user_answer)
    option_c_rb = tk.Radiobutton(quiz_window, variable=user_answer)
    option_d_rb = tk.Radiobutton(quiz_window, variable=user_answer)
    
    option_a_rb.pack()
    option_b_rb.pack()
    option_c_rb.pack()
    option_d_rb.pack()

    # Submit button to check answer and move to the next question
    submit_button = tk.Button(quiz_window, text="Submit Answer", command=submit_answer)
    submit_button.pack()

    # Display the first question
    display_question()

# Create the main window for selecting a category
main_window = tk.Tk()
main_window.title("Select Quiz Category")

# Label and dropdown for selecting category
tk.Label(main_window, text="Choose a category:").pack()
category = tk.StringVar()
category_menu = ttk.Combobox(main_window, textvariable=category, values=["DS3850", "DS3841", "BIO1020", "ECON3610", "COMM2025"])
category_menu.pack()

# Start Quiz Button
start_button = tk.Button(main_window, text="Start Quiz Now", command=lambda: open_quiz_window(category.get()))
start_button.pack()

main_window.mainloop()