import PySimpleGUI as sg


# Mostra uma janela de sobre o app!
def sobre_app():
    return sg.Popup(
        """
Esse programa foi criado por Paulo Daniel!


Versão:     0.0.5
Licensa:    MIT
Github:      https://github.com/TrexPD
        """,
        title='Sobre o bloquim!',
        
        grab_anywhere=True,
        background_color = '#424556',
        button_type=5,
        font=('Futura', 10),
        icon='.\\resources\\image\\bloco-de-anotacoes.ico'
)