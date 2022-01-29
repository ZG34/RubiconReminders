# this file holds the functionality for the to-do interface, inside a notebook framework which may be scaled to include
# the main note-taking app in another notebook tab.

from tkinter import (
    Tk,
    Frame,
    Text,
    Button,
    Checkbutton,
    Entry,
    Label,
    Listbox,
    END,
    Menu,
)
from tkinter.ttk import Notebook
import json
from datetime import datetime

# button labels as constants
ADD_NEW = "^ Enter & Add TODO ^"
ARCHIVE = "^ Archive Entry v"
DEL_ENTRY = "-Remove Archive-"

# reference file to save and restore state of listbox between instances, using JSON.
FILE1 = "todo_active"
FILE2 = "todo_archive"


class NotebookMain(Tk):
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.window = Frame(self.parent)

        def notebook_assets(self):
            self.notebook1 = Notebook(
                self.parent)
            self.page1 = Frame(self.notebook1, bg="#000000")
            #self.page2 = Frame(self.notebook1)
            self.notebook1.add(self.page1, text="TODO")
            #self.notebook1.add(self.page2, text="NOTES")
            self.notebook1.pack()

            def todo_screen():
                def column1():
                    def add_entry(event):
                        todo = entry_1.get()
                        active_lbox.insert(
                            "end", todo)

                    def archive_entry(event):
                        selection = active_lbox.curselection()[0]
                        grabber = active_lbox.get(selection)
                        archive_lbox.insert("end", grabber)
                        active_lbox.delete(selection)

                    def de_archive_entry(event):
                        selection = archive_lbox.curselection()[0]
                        grabber = archive_lbox.get(selection)
                        active_lbox.insert("end", grabber)
                        archive_lbox.delete(selection)

                    def delete_active(event):
                        selection = active_lbox.curselection()[0]
                        active_lbox.delete(selection)

                    def delete_archive(event):
                        selection = archive_lbox.curselection()[0]
                        archive_lbox.delete(selection)

                    def save_state(event):
                        note = active_lbox.get(0, "end")
                        note2 = archive_lbox.get(0, "end")
                        with open(FILE1, "w") as f:
                            json.dump(note, f)
                            # json.dump(note2, f)
                        with open(FILE2, "w") as f2:
                            json.dump(note2, f2)
                        dt = datetime.now()
                        timestamp = f"{dt.hour}:{dt.minute}"
                        save_confirm.delete("1.0", "end")
                        save_confirm.insert("1.0", "TODO saved: " + str(timestamp))

                    def load_state():
                        with open(FILE1, "r+") as f:
                            data = json.load(f)
                            for v in data:
                                active_lbox.insert(END, v)
                        with open(FILE2, "r+") as f2:
                            data = json.load(f2)
                            for v in data:
                                archive_lbox.insert(END, v)

                    entry_1 = Entry(self.page1, highlightbackground="#9E9E9E", highlightthickness=1)
                    entry_1.grid(row=2, column=1, ipadx=20, pady=3)
                    entry_1.bind("<Tab>", add_entry)

                    active_lbox = Listbox(self.page1, width=18, highlightbackground="#9E9E9E",
                                          highlightthickness=1, font=("RobotoRoman", 12))
                    active_lbox.grid(row=4, column=1, pady=3)
                    active_lbox.bind("<Tab>", archive_entry)
                    active_lbox.bind("<Control-s>", save_state)
                    active_lbox.bind("<Delete>", delete_active)



                    archive_lbox = Listbox(self.page1, height=3, width=27, highlightbackground="#9E9E9E",
                                           highlightthickness=1, fg="#606060")
                    archive_lbox.grid(row=6, column=1, pady=3)
                    archive_lbox.bind("<Tab>", de_archive_entry)
                    archive_lbox.bind("<Delete>", delete_archive)
                    archive_lbox.bind("<Control-s>", save_state)

                    add_entry_button = Button(self.page1, text=ADD_NEW, command=lambda: add_entry(entry_1), width=20,
                                              relief="raised")
                    add_entry_button.grid(row=3, column=1, pady=3)

                    archive_entry_button = Button(self.page1, text=ARCHIVE, command=lambda: archive_entry(active_lbox),
                                                  width=20, relief="raised")
                    archive_entry_button.grid(row=5, column=1, pady=3)

                    delete_archived_button = Button(
                        self.page1, text=DEL_ENTRY, command=lambda: delete_archive(archive_lbox),
                        width=20, relief="raised")
                    delete_archived_button.grid(row=7, column=1, pady=3)

                    save_button = Button(self.page1, text="SAVE TODO", command=lambda: save_state(self.window))
                    save_button.grid(row=9, column=1)
                    save_button.config(font=("RobotoRoman", 11, "bold"), width=20, bg="#8E001C", fg="#FFB302")

                    save_confirm = Text(self.page1, height=1, width=23)
                    save_confirm.grid(row=8, column=1, pady=2)

                    try:
                        load_state()
                    except FileNotFoundError:
                        pass

                column1()

            todo_screen()

            def note_screen():
                pass

        notebook_assets(self)


def run():
    root = Tk()
    app = NotebookMain(root)
    root.mainloop()

# running here and on main.py resulted in break
# if __name__ == "__main__":
#     run()