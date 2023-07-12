from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title("Dangerous Writing App")
window.config(bg="beige", highlightthickness=0)
window.minsize(width=1500, height=900)

# App home screen canvas
start_canvas = Canvas(width=1600, height=800, bg="beige", highlightthickness=0)
canvas_text = start_canvas.create_text(
    800, 150, width=1500, justify="center",
    text="\nThis is a very dangerous writing app!\n"
         "\nOnce you start typing you cannot stop!\n"
         "\nIf you do nothing for 5 seconds, everything will disappear!",
    fill="brown", font=("Courier", 30, "bold"))
logo_image = PhotoImage(file="logo.png")
start_canvas.create_image(800, 500, image=logo_image)
start_canvas.grid(row=1, column=0)

# Time goes at top of window
timer_canvas = Canvas(width=1000, height=50, bg="beige", highlightthickness=0)
timer_text = timer_canvas.create_text(
    500, 10, justify="center", text="Time remaining: 5", fill="steel blue", font=("Times", 30, "bold"), anchor=N
)
timer_canvas.grid(row=0, column=0)

# Global variables to used to control timer functionality in count_down function
Key_Has_Been_Pressed = False
Text_Has_Been_Saved = False


def start():
    # Hide home screen during writing session
    start_button.grid_forget()
    start_canvas.grid_forget()

    # Create text box
    text = Text(height=25, width=115, padx=50, pady=50, font=("Times", 20))
    text.focus()  # Puts cursor in textbox.
    text.grid(row=1, column=0)

    def count_down(count):
        global Key_Has_Been_Pressed, Text_Has_Been_Saved
        # Reconfigure timer based on {count} variable every time this function is called
        timer_canvas.itemconfig(timer_text, text=f"Time remaining: {count}")

        if Text_Has_Been_Saved:  # If user clicks 'save' button, timer is reset and paused
            Text_Has_Been_Saved = False
            timer_canvas.itemconfig(timer_text, text="Time remaining: 5")
        elif Key_Has_Been_Pressed:  # If user presses a key, timer is reset and run
            Key_Has_Been_Pressed = False
            count_down(5)
        elif count > 0:
            window.after(1000, count_down, count - 1)
        elif count == 0:  # If timer reaches zero, text is lost, and user is returned to home screen
            text.destroy()
            save_button.grid_forget()
            start_canvas.grid(row=1, column=0)
            start_button.grid(row=2, column=0)

    # Initial call of timer function
    count_down(5)

    def check_keystroke(e):  # Detect keypress and update global variable
        global Key_Has_Been_Pressed
        Key_Has_Been_Pressed = True

    # Bind the Mouse button event
    window.bind('<KeyPress>', check_keystroke)

    def save():
        # If save button is pressed, update global variable
        global Text_Has_Been_Saved
        Text_Has_Been_Saved = True

        files = [('All Files', '*.*'), ('Text Document', '*.txt')]
        path = asksaveasfilename(filetypes=files, defaultextension=".txt")
        if path:  # If user chooses a file name and filepath...
            with open(path, "w") as file:
                file.write(text.get("1.0", END))  # Gets current value in textbox at line 1, character 0
        else:   # If user cancels out of file dialogue window...
            text.destroy()  # ...text is lost and user is returned to home screen
            save_button.grid_forget()
            start_canvas.grid(row=1, column=0)
            start_button.grid(row=2, column=0)

        text.destroy()  # After user successfully saves, they are returned to home screen
        timer_canvas.itemconfig(timer_text, text="Time remaining: 5")
        save_button.grid_forget()
        start_canvas.grid(row=1, column=0)
        start_button.grid(row=2, column=0)

    save_button = Button(text="Save", bg="white", highlightthickness=0, command=save)
    save_button.grid(row=2, column=0)


start_button = Button(text="Start writing!", bg="white", highlightthickness=0, command=start)
start_button.grid(row=2, column=0)

window.mainloop()
