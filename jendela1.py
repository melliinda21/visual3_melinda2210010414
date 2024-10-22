import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#8B8378")
window =sg.Window(title="Profile",
                  layout=[[sg.Text("SELAMAT DATANG DIKELAS",
                                font=("Arial",25,"italic","bold","underline"))],
                        [sg.Text("NPM      : 2210010414")],
                          [sg.Text("Nama     : Melinda")],
                          [sg.Text("Kelas    : 5B NonReg BJM")],
                          [sg.Text("Matkul   : Visual 3")],
                          ],size=(400,200),font=("Times", 20))
window()
window.close()