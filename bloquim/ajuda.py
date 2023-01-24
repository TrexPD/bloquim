import PySimpleGUI as sg


# Mostra uma janela de sobre o app!
def info_app():
    return sg.Popup(
"""
Esse programa foi criado por Paulo Daniel!


Versão:     0.1.5
Licença:    GNU General Public License v3.0
Github:      https://github.com/TrexPD/bloquim
        """,
        title='Sobre o bloquim!',
        grab_anywhere=True,
        background_color = '#424556',
        button_type=5,
        font=('Futura', 15),
        icon='.\\resources\\image\\bloco-de-anotacoes.ico'
)