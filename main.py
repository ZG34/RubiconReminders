# tkinter GUI functions
from tkinter import Tk, Text, Button, Listbox, END, Entry, Scrollbar, Menu, Label
# os imports for creating note directory, adding and removing text files, and changing working dir to note dir
from os import getcwd, path, listdir, chdir, remove, makedirs
# datetime used to display save function has run at time clicked
from datetime import datetime

# project module holding menu bar functions
import menu_contents


# generates note directory
def directory_generator():
    current_directory = getcwd()
    final_directory = path.join(current_directory, r'note_folder')
    if not path.exists(final_directory):
        makedirs(final_directory)
        print("directory created")


directory_generator()

# changes working directory to generated note directory
chdir("note_folder")

# creates a global working_note variable to store active note, so that listbox.curselection does not break when
# double-clicking away from listbox and then trying to save file
working_note = ()


# main GUI and functions
def main_gui():
    window = Tk()
    window.geometry("400x400")
    window.config(bg="#000000")
    window.title("Rubicon Reminders")

    # function to refresh window
    def go_home():
        window.destroy()
        main_gui()
        print("refreshed window")

    # main listbox interface
    lbox = Listbox(window)
    lbox.place(x=10, y=10)

    # populates listbox with note file names
    for file in listdir():
        lbox.insert(END, file)

    # entry box for adding a new note
    add_note_entry = Entry(window)
    add_note_entry.place(x=15, y=268)
    add_note_entry.config(width=17)
    add_note_label = Label(window, text="Enter New Note Title:", bg="#000000", fg="#FFFFFF")
    add_note_label.place(x=12, y=245)

    # function to add a named note to the listbox population
    def add_note():
        title = add_note_entry.get()
        hdl = open(title + ".txt", "w")
        hdl.close(), go_home()

    # function for opening and reading selected note
    def open_note(event):
        lbox_selection = lbox.curselection()[0]
        file = lbox.get(lbox_selection)
        global working_note
        working_note = file
        with open(file, 'r+') as file:
            file = file.read()
        text_output.delete('1.0', END)
        text_output.insert(END, file)

    # function for writing additional text to opened file
    def save_note_cmd():
        file = working_note
        hdl = open(file, 'w')
        note = text_output.get('1.0', 'end')
        for line in note:
            hdl.write(line)
        hdl.close()
        # displays note-save functionality is working correctly
        dt = datetime.now()
        save_confirm.delete("1.0", "end")
        save_confirm.insert("1.0", "Note saved: " + str(dt))
        print("note saved")

    # separate function for save via hotkey, triggered by event
    def save_note_hotkey(event):
        file = working_note
        hdl = open(file, 'w')
        note = text_output.get('1.0', 'end')
        for line in note:
            hdl.write(line)
        hdl.close()
        # displays note-save functionality is working correctly
        dt = datetime.now()
        save_confirm.delete("1.0", "end")
        save_confirm.insert("1.0", "Note saved: " + str(dt))
        print("note saved")

    # function for deleting a selected note from listbox and directory
    def del_note():
        lbox_selection = lbox.curselection()[0]
        file = lbox.get(lbox_selection)
        remove(file)
        go_home()

    # GUI buttons
    def buttons():
        add_note_button = Button(window, command=add_note)
        add_note_button.place(x=15, y=290)
        add_note_button.config(width=14, height=1, text="ADD NEW NOTE", relief="raised")

        del_note_button = Button(window, command=del_note)
        del_note_button.place(x=8, y=180)
        del_note_button.config(width=17, height=1, text="DELETE SELECTED NOTE", relief="raised")

        save_note_button = Button(window, command=save_note_cmd)
        save_note_button.pack(side="bottom", fill='x')
        save_note_button.config(height=1, text="--- SAVE NOTE ---", bg="#8E001C", font=("RobotoRoman", 11, "bold"),
                                relief="groove", fg="#FFB302")

    buttons()

    # text area to display confirm message when save is successful.
    save_confirm = Text(window, height=1, width=50)
    save_confirm.pack(side='bottom')

    # text area to display selected note from listbox
    text_output = Text(window, wrap="word")
    text_output.pack(side="right", fill="y",)
    text_output.config(width=29)

    # scrollbar, tied to text_output
    text_scroll = Scrollbar(window, command=text_output.yview)
    text_scroll.pack(side="right", fill="y")
    text_output['yscrollcommand'] = text_scroll.set

    # binds selected listbox item to be opened on selection, into text_output
    lbox.bind("<<ListboxSelect>>", open_note)

    # binds ctrl-s as hotkey to save text_output back to file
    text_output.bind("<Control-s>", save_note_hotkey)

    # menu bar
    menu_bar = Menu(window)
    menu_bar.add_command(label="Help", command=menu_contents.help_screen)
    menu_bar.add_command(label="View Note Folder", command=menu_contents.view_note_folder)
    window.config(menu=menu_bar)

    window.resizable(False, False)
    window.mainloop()


main_gui()
