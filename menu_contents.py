from tkinter import Tk, Label
from os import startfile, path, getcwd, chdir


def help_screen():
    window = Tk()
    window.geometry("250x422")
    window.title("Help")

    bindings = Label(window, text="---Note Bindings--- \n \n"
                                  "[Ctrl-s] = Save Note \n"
                                  "[Del] = Delete selected note file \n"
                                  "[Enter] = Add New Note w/ Entered Title \n \n "
                                  "---TODO Bindings--- \n \n"
                                  "[Ctrl-s] = Save Lists \n"
                                  "[Del] = Delete selected archived todo \n"
                                  "[Tab] = Add new todo \n"
                                  "[Tab] = Move todo between active/archive ")
    bindings.pack(pady=10)

    functionality = Label(window, text="\n ---USER TIPS--- \n \n"
                                       " Add an entry by entering it above \n "
                                       "the 'add new' button,\n then click button or hotkey. \n \n"
                                       " Note Edits must be saved \n [Save Button, or Ctrl-S] \n before clicking a "
                                       "different "
                                       "note from the list.\n Otherwise, text will be lost. \n \n"
                                       "")
    functionality.pack(pady=10)

    window.mainloop()


def view_note_folder():
    parent_path = path.dirname(getcwd())
    chdir(parent_path)
    startfile('note_folder')
    # return to note directory in application after opening to view in explorer
    chdir('note_folder')

