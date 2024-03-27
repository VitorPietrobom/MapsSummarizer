import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from GoogleAPIUsing import get_place_details, search_places
from OpenAIAPIUsing import generate_summary

def get_user_input():
    user_input = entry.get()
    if user_input.strip():
        return user_input
    else:
        messagebox.showerror("Error", "Please enter a valid input.")

def on_submit():
    activity = get_user_input()
    num_places = int(num_places_entry.get()) 
    if activity and num_places:
        results = search_places(activity)
        num_places_to_process = min(len(results), num_places)
        progress_bar['maximum'] = num_places_to_process
        
        # Show loading bar
        progress_bar.start()
        
        # Start processing places
        root.after(10, process_places, results, num_places_to_process, 0)

def process_places(results, num_places, place_index):
    if place_index < num_places:
        place_id = results[place_index]['place_id']
        details = get_place_details(place_id)
        summary = generate_summary(details)
        
        # Append the place name and summary to the text widget
        text_output.insert(tk.END, f"Name: {details['name']}\n")
        text_output.insert(tk.END, f"Summary: {summary}\n")
        text_output.insert(tk.END, "-" * 50 + "\n\n")
        
        # Update progress bar
        progress_bar.step(1)
        
        # Schedule the next processing iteration
        root.after(10, process_places, results, num_places, place_index + 1)
    else:
        # Hide loading bar
        progress_bar.stop()

# Create main window
root = tk.Tk()
root.title("Activity Finder")

# Create input label and entry widget for activity
activity_label = ttk.Label(root, text="What do you want to do?")
activity_label.grid(row=0, column=0, padx=10, pady=5)
entry = ttk.Entry(root, width=30)
entry.grid(row=0, column=1, padx=10, pady=5)

# Create input label and entry widget for number of places
num_places_label = ttk.Label(root, text="Number of places to search:")
num_places_label.grid(row=1, column=0, padx=10, pady=5)
num_places_entry = ttk.Entry(root, width=10)
num_places_entry.grid(row=1, column=1, padx=10, pady=5)

# Create submit button
submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create text widget to display output
text_output = tk.Text(root, wrap=tk.WORD, width=60, height=20)
text_output.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create progress bar with determinate mode
progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=200)
progress_bar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()

