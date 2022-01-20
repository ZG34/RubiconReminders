# to RUN APP IN CMD PROMPT: cd to StratNotes directory, or place strat_notes in default CMD directory:
# then run 'python strat_notes_terminalvers.py'

from os import listdir
from datetime import datetime

# this assigns dt variable as date + timestamp
dt = (datetime.now())
# establishing 0 as start for the numeration of each noted item per session
# n = 1
# n += 1            # TODO numerate note items per entry


# open existing or create a new file prompt:
p1 = input("(V)iew or (N)ew [V/N]: ").upper()
if p1 == "V":
    # this views file directory of existing notes if first input is (view)
    for file in listdir():
        if file.endswith(".txt"):
            print(file)
    # below opens existing file, allows multiple note lines, and dates it when finished with session.
    old_file = (input("which file would you like to open: "))
    hdl = open(old_file + ".txt", "r+")  # using r+ by default places text at beginning, overwriting.
    for line in hdl:  # as long as you first READ the file, then r+ becomes APPEND TO END.
        print(line.strip())
    of_note = input("Add Note: ")
    if of_note == "done":  # FIXME add accept on any 'done' check for upper and lowercase
        # specifies notes were reviewed if first note entry is "done"
        hdl.write(" REVIEWED: ")
        hdl.write(str(dt))
    # if first entered note is not 'done', continue asking for more notes until entry == 'done'
    else:
        hdl.write('\n')
        hdl.write(of_note)
        hdl.write('\n')
        while of_note != "done":
            of_note = input("Add more notes: ")
            while of_note != "done":
                hdl.write(of_note)
                hdl.write('\n')
        else:
            hdl.write("SESSION END: ")
            hdl.write(str(dt))
            hdl.write('\n')
        hdl.close()

# below is the block for generating and noting in a new file, if line 15 == 'N'
elif p1 == "N":
    new_file = input("new file name: ")
    hdl = open(new_file, "a")
    nf_note = input("Add Note: ")
    if nf_note == "done":
        print("finished")
    else:
        hdl.write(nf_note)
        hdl.write('\n')
        while nf_note != "done":
            nf_note = input("Add more notes: ")
            while nf_note != "done":
                hdl.write(nf_note)
                hdl.write('\n')
                break
        else:
            hdl.write("SESSION END: ")
            hdl.write(str(dt))
            hdl.write('\n')
    hdl.close()
else:
    print("Error: please enter V or N")

