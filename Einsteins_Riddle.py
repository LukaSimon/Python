from tkinter import *

window = Tk()
window.title("Einsteins riddle")
window.configure(background='white')
window.attributes('-fullscreen', True)

frame1 = Frame(window, borderwidth=0, relief=FLAT, background='white')
frame1.pack(side=TOP, padx=10, pady=10)

text_label = Label(window,
                   text="The situation:\n1. There are five houses in five different colors.\n2. In each house lives a person with "
                        "a different nationality.\n3. Each one drinks a different beverage, smokes a different "
                        "cigearette brand and keeps a different pet.\n4. No one keeps the same pet, smokes the same "
                        "cigearette brand and drinks the same beverage.\n",
                   background='white')
text_label.pack()

text_label_quest = Label(window, text="The question: Who owns the fish?\n", background='white')
text_label_quest.pack()

hint_status = False
short_status = False

hints_1 = """
Hints:
The Brit lives in the red house.
The Swede keeps dogs as pets.
The Dane drinks tea.
The green house is on the left of the white house.
The green house's owner drinks coffee.
The person who smokes Pall Mall rears birds.
The owner of the yellow house smokes Dunhill.
The man living in the center house drinks milk.
The Norwegian lives in the first house.
The man who smokes blends lives next to the one who keeps cats.
The man who keeps horses lives next to the man who smokes Dunhill.
The owner who smokes BlueMaster drinks beer.
The German smokes Prince.
The Norwegian lives next to the blue house.
The man who smokes blend has a neighbor who drinks water.
"""

short = """
Shorts:
The entry has to follow a certain form.

Example: c1 Bl
Color = c, Nationality = n, Drink/Beverage = d, Pet = p, Smoke = s
Houses: 1 - 5
Space and the entry (Overall five characters)

Blue = Bl, Green = Gr, Red = Re, Yellow = Ye, White = Wh
Brit = Br, Dane = Dk, German = Ge, Norwegian = No, Swede = Se
Beer = Be, Coffee = Co, Milk = Mi, Tea = Te, Water = Wa
Bird = Bi, Cat = Ca, Dog = Do, Fish = Fi, Horse = Ho
Blends = Bl, Blue Master = Bm, Dunhill = Dh, Pall Mall = Pm, Prince = Pr
"""


def hint_off():
    global hint_status
    hint_window.destroy()
    hint_status = False


def short_off():
    global short_status
    short_window.destroy()
    short_status = False


def hint():
    global hint, hint_status, hint_window
    if hint_status:
        hint_off()
    hint_window = Tk()
    hint_window.wm_title("Hint 1")
    hint_window.attributes('-topmost', True)
    hint_window.configure(background='white')
    hint_text = Frame(hint_window, borderwidth=0, relief=FLAT, background='white')
    hint_text.pack(side=TOP, padx=0, pady=0)
    label = Label(hint_text, text=hints_1, background='white', anchor='s')
    label.pack(side=LEFT, fill="both")
    frameButtons = Frame(hint_window, borderwidth=0, relief=FLAT, background='white')
    frameButtons.pack(side=TOP, padx=0, pady=0)
    okButton = Button(hint_window, text="OK", width=10, command=hint_off, background='white')
    okButton.pack(pady=10, padx=10)
    page_2 = Button(hint_window, text="Page 2", width=10, command=short_def, background='white')
    page_2.pack(pady=10, padx=10)
    hint_window.mainloop()


def short_def():
    global short, short_status, short_window
    short_window = Tk()
    short_window.wm_title("Shorts")
    short_window.attributes('-topmost', True)
    short_window.configure(background='white')
    short_text = Frame(short_window, borderwidth=0, relief=FLAT, background='white')
    short_text.pack(side=TOP, padx=0, pady=0)
    label = Label(short_window, text=short, background='white', anchor='s')
    label.pack(side=LEFT, fill="both")
    frame_buttons = Frame(short_window, borderwidth=0, relief=FLAT, background='white')
    frame_buttons.pack(side=TOP, padx=0, pady=0)
    okButton = Button(short_window, text="OK", width=10, command=short_off, background='white')
    okButton.pack()
    short_window.mainloop()


def check():
    check_window = Tk()
    check_window.wm_title("Check")
    check_window.attributes('-topmost', True)
    check_window.configure(background='white')
    incorrect = "Your solution is incorrect."
    correct = "Your solution is correct."
    if solution[1] == tabel[1] and solution[2] == tabel[2] and solution[3] == tabel[3] and solution[4] == tabel[4] and solution[5] == tabel[5]:
        check_label = Label(check_window, text=correct, background='white', anchor='s')
        check_label.pack(side=LEFT, fill="both")
    else:
        check_label = Label(check_window, text=incorrect, background='white', anchor='s')
        check_label.pack(side=LEFT, fill="both")


tabel = [
    ["Categ", "01", "02", "03", "04", "05"],
    ["Color", "--", "--", "--", "--", "--"],
    ["Natio", "--", "--", "--", "--", "--"],
    ["Bever", "--", "--", "--", "--", "--"],
    [" Pet ", "--", "--", "--", "--", "--"],
    ["Smoke", "--", "--", "--", "--", "--"]
]

test = Label(window, text=tabel[0], background='white')
test_2 = Label(window, text=tabel[1], background='white')
test_3 = Label(window, text=tabel[2], background='white')
test_4 = Label(window, text=tabel[3], background='white')
test_5 = Label(window, text=tabel[4], background='white')
test_6 = Label(window, text=tabel[5], background='white')
test.pack()
test_2.pack()
test_3.pack()
test_4.pack()
test_5.pack()
test_6.pack()

answer_window = Tk()
answer_window.wm_title("Answer")
answer_window.attributes('-topmost', True)


def tab():
    tab_1 = Label(answer_window, text=tabel[0], background='white')
    tab_2 = Label(answer_window, text=tabel[1], background='white')
    tab_3 = Label(answer_window, text=tabel[2], background='white')
    tab_4 = Label(answer_window, text=tabel[3], background='white')
    tab_5 = Label(answer_window, text=tabel[4], background='white')
    tab_6 = Label(answer_window, text=tabel[5], background='white')
    tab_1.pack()
    tab_2.pack()
    tab_3.pack()
    tab_4.pack()
    tab_5.pack()
    tab_6.pack()


entry_var = StringVar()
entry = Entry(window, textvariable=entry_var, width=50, background='white')
entry.focus_set()
entry.bind("<Return>")
entry.pack(padx=10, pady=10)


def clear():
    entry.delete(0, END)


solution = [
    ["Categ", "1", "2", " 3", " 4", " 5"],
    ["Color", "Ye", "Bl", "Re", "Gr", "Wh"],
    ["Natio", "No", "Dk", "Br", "Ge", "Sw"],
    ["Bever", "Wa", "Te", "Mi", "Co", "Be"],
    [" Pet ", "Ca", "Ho", "Bi", "Fi", "Do"],
    ["Smoke", "Dh", "Bl", "Pm", "Pr", "Bm"]
]


def code():
    feed = entry_var.get()
    answer = feed[3] + feed[4]
    if feed[0] == 'c':
        if feed[1] == str(1):
            tabel[1][1] = answer
        if feed[1] == str(2):
            tabel[1][2] = answer
        if feed[1] == str(3):
            tabel[1][3] = answer
        if feed[1] == str(4):
            tabel[1][4] = answer
        if feed[1] == str(5):
            tabel[1][5] = answer
    if feed[0] == 'n':
        if feed[1] == str(1):
            tabel[2][1] = answer
        if feed[1] == str(2):
            tabel[2][2] = answer
        if feed[1] == str(3):
            tabel[2][3] = answer
        if feed[1] == str(4):
            tabel[2][4] = answer
        if feed[1] == str(5):
            tabel[2][5] = answer
    if feed[0] == 'd':
        if feed[1] == str(1):
            tabel[3][1] = answer
        if feed[1] == str(2):
            tabel[3][2] = answer
        if feed[1] == str(3):
            tabel[3][3] = answer
        if feed[1] == str(4):
            tabel[3][4] = answer
        if feed[1] == str(5):
            tabel[3][5] = answer
    if feed[0] == 'p':
        if feed[1] == str(1):
            tabel[4][1] = answer
        if feed[1] == str(2):
            tabel[4][2] = answer
        if feed[1] == str(3):
            tabel[4][3] = answer
        if feed[1] == str(4):
            tabel[4][4] = answer
        if feed[1] == str(5):
            tabel[4][5] = answer
    if feed[0] == 's':
        if feed[1] == str(1):
            tabel[5][1] = answer
        if feed[1] == str(2):
            tabel[5][2] = answer
        if feed[1] == str(3):
            tabel[5][3] = answer
        if feed[1] == str(4):
            tabel[5][4] = answer
        if feed[1] == str(5):
            tabel[5][5] = answer
    for widget in answer_window.winfo_children():
        widget.destroy()
    tab()
    clear()


frame4 = Frame(window, borderwidth=0, relief=FLAT, background='white')
frame4.pack(side=TOP, padx=10, pady=0)
hint_button = Button(window, text="Hint", width=10, command=hint, background='white')
hint_button.pack()

runButton = Button(window, text="Run", width=10, command=code, background='white')
runButton.pack()

quitButton = Button(window, text="Quit", width=10, command=window.destroy, background='white')
check_btton = Button(window, text="Check", width=10, command=check, background='white')
check_btton.pack()
quitButton.pack()

window.mainloop()
