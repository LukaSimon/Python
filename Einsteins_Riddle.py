from tkinter import *

window = Tk()
window.title("Einsteins Rätsel")
window.configure(background='white')
window.attributes('-fullscreen', True)

frame1 = Frame(window, borderwidth=0, relief=FLAT, background='white')
frame1.pack(side=TOP, padx=10, pady=10)

text_label = Label(window,
                   text="Die Situation:\n1. Es gibt 5 Häuser mit fünf Farben.\n2. In jedem Haus wohnt eine Person mit "
                        "einer anderen Nationalität.\n3. Jeder der fünf trinkt ein Getränk, raucht eine "
                        "Zigarettenmarke und hat ein Haustier.\n4. Niemend hat das gleiche Tier, raucht dieselbe "
                        "Zigarettenmarke und trinkt dasselbe Getränk.\n",
                   background='white')
text_label.pack()

text_label_frage = Label(window, text="Die Frage: Wer besitzt den Fisch?\n", background='white')
text_label_frage.pack()

hinweis_status = False
kuerzel_status = False

hinweise = """
Hinweise:
Der Brite wohnt in dem roten Haus.
Der Schwede hält Hunde.
Der Däne trinkt Tee.
Das grüne Haus ist links neben dem weißen Haus.
Die Person im grünen Haus trinkt Kaffee.
Die Person, die Pall Mall raucht, hat Vögel.
Die Person im gelben Haus raucht Dunhill.
Die Person in der Mitte trinkt Milch.
Der Norweger lebt im ersten Haus.
Die Person, die Blends raucht, wohnt neben dem Katzenbesitzer.
Die Person, die Pferde hat, lebt neben der Person, die Dunhill raucht.
Die Person, die BlueMaster raucht, trinkt Bier.
Der Deutsche raucht Prince.
Der Norweger lebt neben dem blauen Haus.
Die Person, die Blends raucht,hat einen Nachbarn, der Wasser trinkt.
"""

kuerzel = """
Bitte Zweierkürzel verwenden.
Kürzel:
Die Eingabe muss ein bestimmtes Muster verfolgen.

Bsp.: c1 Ge
Farbe = c, Nationalität = n, Getränk = d, Haustier= p, Marke = s
Hausnummer 1 - 5
Leerstelle und die Eingabe (Insgesamt 5 Stellen)

Blau = Bl, Gelb = Ge, Grün = Gr, Rot = Ro, Weiß = We
Brite = Br, Däne = Dk, Deutsche = Ge, Norweger = No, Schwede = Se
Bier = Bi, Kaffee = Ka, Milch = Mi, Tee = Te, Wasser = Wa
Fisch = Fi, Hund = Hu, Katze = Ka, Pferd = Pf, Vogel = Vo
Blends = Bl, Blue Master = Bm, Dunhill = Dh, Pall Mall = Pm, Prince = Pr
"""


def hinweis_off():
    global hinweis_status
    hinweis_fenster.destroy()
    hinweis_status = False


def kuerzel_off():
    global kuerzel_status
    kuerzel_fenster.destroy()
    kuerzel_status = False


def hinweis_1():
    global hinweise, hinweis_status, hinweis_fenster
    if hinweis_status:
        hinweis_off()
    hinweis_fenster = Tk()
    hinweis_fenster.wm_title("Hinweise 1")
    hinweis_fenster.attributes('-topmost', True)
    hinweis_fenster.configure(background='white')
    hinweis_text = Frame(hinweis_fenster, borderwidth=0, relief=FLAT, background='white')
    hinweis_text.pack(side=TOP, padx=0, pady=0)
    label = Label(hinweis_text, text=hinweise, background='white', anchor='s')
    label.pack(side=LEFT, fill="both")
    frameButtons = Frame(hinweis_fenster, borderwidth=0, relief=FLAT, background='white')
    frameButtons.pack(side=TOP, padx=0, pady=0)
    okButton = Button(hinweis_fenster, text="OK", width=10, command=hinweis_off, background='white')
    okButton.pack(pady=10, padx=10)
    seite_2 = Button(hinweis_fenster, text="Seite 2", width=10, command=kuerzel_def, background='white')
    seite_2.pack(pady=10, padx=10)
    hinweis_fenster.mainloop()


def kuerzel_def():
    global kuerzel, kuerzel_status, kuerzel_fenster
    kuerzel_fenster = Tk()
    kuerzel_fenster.wm_title("Kürzel")
    kuerzel_fenster.attributes('-topmost', True)
    kuerzel_fenster.configure(background='white')
    kuerzel_text = Frame(kuerzel_fenster, borderwidth=0, relief=FLAT, background='white')
    kuerzel_text.pack(side=TOP, padx=0, pady=0)
    label = Label(kuerzel_fenster, text=kuerzel, background='white', anchor='s')
    label.pack(side=LEFT, fill="both")
    frame_buttons = Frame(kuerzel_fenster, borderwidth=0, relief=FLAT, background='white')
    frame_buttons.pack(side=TOP, padx=0, pady=0)
    okButton = Button(kuerzel_fenster, text="OK", width=10, command=kuerzel_off, background='white')
    okButton.pack()
    kuerzel_fenster.mainloop()


def check():
    check_fenster = Tk()
    check_fenster.wm_title("Check")
    check_fenster.attributes('-topmost', True)
    check_fenster.configure(background='white')
    falsch = "Deine Lölung ist nicht korrekt"
    korrekt = "Deine Lölung ist korrekt"
    if loesung[1] == tabelle[1] and loesung[2] == tabelle[2] and loesung[3] == tabelle[3] and loesung[4] == tabelle[4] and loesung[5] == tabelle[5]:
        check_label = Label(check_fenster, text=korrekt, background='white', anchor='s')
        check_label.pack(side=LEFT, fill="both")
    else:
        check_label = Label(check_fenster, text=falsch, background='white', anchor='s')
        check_label.pack(side=LEFT, fill="both")


tabelle = [
    ["Kateg", "01", "02", "03", "04", "05"],
    ["Color", "--", "--", "--", "--", "--"],
    ["Natio", "--", "--", "--", "--", "--"],
    ["Drink", "--", "--", "--", "--", "--"],
    ["Haust", "--", "--", "--", "--", "--"],
    ["Smoke", "--", "--", "--", "--", "--"]
]

test = Label(window, text=tabelle[0], background='white')
test_2 = Label(window, text=tabelle[1], background='white')
test_3 = Label(window, text=tabelle[2], background='white')
test_4 = Label(window, text=tabelle[3], background='white')
test_5 = Label(window, text=tabelle[4], background='white')
test_6 = Label(window, text=tabelle[5], background='white')
test.pack()
test_2.pack()
test_3.pack()
test_4.pack()
test_5.pack()
test_6.pack()

antwort_fenster = Tk()
antwort_fenster.wm_title("Antwort")
antwort_fenster.attributes('-topmost', True)


def tab():
    tab_1 = Label(antwort_fenster, text=tabelle[0], background='white')
    tab_2 = Label(antwort_fenster, text=tabelle[1], background='white')
    tab_3 = Label(antwort_fenster, text=tabelle[2], background='white')
    tab_4 = Label(antwort_fenster, text=tabelle[3], background='white')
    tab_5 = Label(antwort_fenster, text=tabelle[4], background='white')
    tab_6 = Label(antwort_fenster, text=tabelle[5], background='white')
    tab_1.pack()
    tab_2.pack()
    tab_3.pack()
    tab_4.pack()
    tab_5.pack()
    tab_6.pack()


eingabe_var = StringVar()
entry = Entry(window, textvariable=eingabe_var, width=50, background='white')
entry.focus_set()
entry.bind("<Return>")
entry.pack(padx=10, pady=10)


def clear():
    entry.delete(0, END)


loesung = [
    ["Kateg", "1", "2", " 3", " 4", " 5"],
    ["Color", "Ge", "Bl", "Ro", "Gr", "We"],
    ["Natio", "No", "Dk", "Br", "Ge", "Se"],
    ["Drink", "Wa", "Te", "Mi", "Ka", "Bi"],
    ["Haust", "Ka", "Pf", "Vo", "Fi", "Hu"],
    ["Smoke", "Dh", "Bl", "Pm", "Pr", "Bm"]
]


def code():
    eintrag = eingabe_var.get()
    antwort = eintrag[3] + eintrag[4]
    if eintrag[0] == 'c':
        if eintrag[1] == str(1):
            tabelle[1][1] = antwort
        if eintrag[1] == str(2):
            tabelle[1][2] = antwort
        if eintrag[1] == str(3):
            tabelle[1][3] = antwort
        if eintrag[1] == str(4):
            tabelle[1][4] = antwort
        if eintrag[1] == str(5):
            tabelle[1][5] = antwort
    if eintrag[0] == 'n':
        if eintrag[1] == str(1):
            tabelle[2][1] = antwort
        if eintrag[1] == str(2):
            tabelle[2][2] = antwort
        if eintrag[1] == str(3):
            tabelle[2][3] = antwort
        if eintrag[1] == str(4):
            tabelle[2][4] = antwort
        if eintrag[1] == str(5):
            tabelle[2][5] = antwort
    if eintrag[0] == 'd':
        if eintrag[1] == str(1):
            tabelle[3][1] = antwort
        if eintrag[1] == str(2):
            tabelle[3][2] = antwort
        if eintrag[1] == str(3):
            tabelle[3][3] = antwort
        if eintrag[1] == str(4):
            tabelle[3][4] = antwort
        if eintrag[1] == str(5):
            tabelle[3][5] = antwort
    if eintrag[0] == 'p':
        if eintrag[1] == str(1):
            tabelle[4][1] = antwort
        if eintrag[1] == str(2):
            tabelle[4][2] = antwort
        if eintrag[1] == str(3):
            tabelle[4][3] = antwort
        if eintrag[1] == str(4):
            tabelle[4][4] = antwort
        if eintrag[1] == str(5):
            tabelle[4][5] = antwort
    if eintrag[0] == 's':
        if eintrag[1] == str(1):
            tabelle[5][1] = antwort
        if eintrag[1] == str(2):
            tabelle[5][2] = antwort
        if eintrag[1] == str(3):
            tabelle[5][3] = antwort
        if eintrag[1] == str(4):
            tabelle[5][4] = antwort
        if eintrag[1] == str(5):
            tabelle[5][5] = antwort
    for widget in antwort_fenster.winfo_children():
        widget.destroy()
    tab()
    clear()


frame4 = Frame(window, borderwidth=0, relief=FLAT, background='white')
frame4.pack(side=TOP, padx=10, pady=0)
hinweis_button = Button(window, text="Hinweis", width=10, command=hinweis_1, background='white')
hinweis_button.pack()

runButton = Button(window, text="Einloggen", width=10, command=code, background='white')
runButton.pack()

quitButton = Button(window, text="Quit", width=10, command=window.destroy, background='white')
check_btton = Button(window, text="Check", width=10, command=check, background='white')
check_btton.pack()
quitButton.pack()

window.mainloop()
