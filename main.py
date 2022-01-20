# tkinter GUI functions
from tkinter import Tk, Text, Button, Listbox, END, Entry, Scrollbar
# os imports for creating note directory, adding and removing text files, and changing working dir to note dir
from os import getcwd, path, listdir, chdir, remove, makedirs
# datetime used to display save function has run at time clicked
from datetime import datetime


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

# creates a global working_note variable, so that listbox.cureselection does not break when double-clicking away from
# listbox and then trying to save file
working_note = ()


# main GUI and functions
def main_gui():
    window = Tk()
    window.geometry("400x400")
    window.config(bg="#000000")

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
    add_note_entry.place(x=5, y=230)
    add_note_entry.config(width=21)

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
        add_note_button.place(x=5, y=255)
        add_note_button.config(width=17, height=1, text="ADD NEW NOTE")

        del_note_button = Button(window, command=del_note)
        del_note_button.place(x=5, y=185)
        del_note_button.config(width=18, height=1, text="DELETE SELECTED NOTE")

        save_note_button = Button(window, command=save_note_cmd)
        save_note_button.pack(side="bottom", fill='x')
        save_note_button.config(height=2, text="SAVE NOTE", bg="#00FF00")
    buttons()

    # text output widgets
    save_confirm = Text(window, height=1, width=50)
    save_confirm.pack(side='bottom')

    text_output = Text(window)
    text_output.pack(side="right", fill="y")
    text_output.config(width=29)

    text_scroll = Scrollbar(window, command=text_output.yview)
    text_scroll.pack(side="right", fill="y")
    text_output['yscrollcommand'] = text_scroll.set

    lbox.bind("<<ListboxSelect>>", open_note)

    text_output.bind("<Control-s>", save_note_hotkey)

    window.resizable(False, False)
    window.mainloop()


main_gui()
