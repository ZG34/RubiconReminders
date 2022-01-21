from tkinter import Tk, Label
from os import startfile, path, getcwd, chdir


def help_screen():
    window = Tk()
    window.geometry("200x400")
    window.title("Help")

    bindings = Label(window, text="---KEYBINDINGS--- \n \n"
                                  "[Ctrl-s] = Save Note")
    bindings.pack(pady=10)

    functionality = Label(window, text="\n ---USER TIPS--- \n \n"
                                       " Add a new note by entering it above \n "
                                       "the 'add new note' button,\n then click button. \n \n"
                                       " If note edits are not SAVED \n before clicking a different note \n from"
                                       " the list, text will be lost.")
    functionality.pack(pady=10)

    window.mainloop()


def view_note_folder():
    parent_path = path.dirname(getcwd())
    chdir(parent_path)
    startfile('note_folder')
    # return to note directory in application after opening to view in explorer
    chdir('note_folder')

