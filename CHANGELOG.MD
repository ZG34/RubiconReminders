# Changelog

### 1/21/22
* Added - text wrap on word in text output area.

### v0.2 - 1/20/22
* Added - [View Note Folder] menu item
* Added - [Help] menu item, which display keybinds and app functionality.
* Added - GUI display to show user that text file is being saved properly.


* Bugfix - Can now click anywhere and still manage to save to correct file. 
  * Previously, double-clicking away from listbox selection would break ability to save.

* Changed - changed program name.

###1/17/22
* Added - hotkey [ctrl-s] to save file text


* Bugfix - now able to properly delete text and save. 
  * Previously, deleted text would not register as deleted when saving.

### 1/14/22
* Added - scrollbar for text area
* Refactored code with more descriptive variable and function names

### v0.1 - 1/13/22
* First iteration of note taking GUI (main)
  * Create note folder
  * Create or delete new note(txt) files
  * Display contents of note folder in listbox
  * View contents of note in text area
  * Save additions to text area to opened note file

### v0.0 - 1/4/22
* Added functional command line script which: 
    * Prompts user for input to open existing local file or create new local note file.
    * Takes note entry, creating a new line of text per entry and finishing on 'done' entry.
    * Dates and closes note on 'done' entry.
    * On existing note open, allows 'done' entry and prints to file 'reviewed' with date time stamp.
* Project start. 
