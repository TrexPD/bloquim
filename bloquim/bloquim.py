import PySimpleGUI as sg
from datetime import datetime
from help import sobre_app
from rich.syntax import Syntax
from rich.console import Console
from pathlib import Path



# Escolha de temas
sg.theme("darkgrey")

# Tamanho da janela
WIN_W = 60
WIN_H = 30


new_file_name: str =     "Documento de texto.txt"
file_new: str =          "Novo arquivo           Ctrl + N"
file_open: str =         "Abrir arquivo            Ctrl + O"
file_save: str =         "Salvar arquivo         Ctrl + S"
file_save_as: str =      "Salvar arquivo como..."
file_print: str =        "Imprimir arquivo        Ctrl + P"
hora_data: str =         "Hora e data atual"
maiuscula: str =         "Converter para MAIÚSCULAS"
minuscula: str =         "Converter para minúsculas"
p_letra_maiuscula: str = "Converter 1° letra para maiúsculo"
sobre: str =             "Sobre"
exit: str =              "Sair"



# menu de cabeçalho!
menu_layout = (
    ["Arquivo", [file_new, file_open, file_save, file_save_as, "---", file_print, "---", exit]],
    ["Editar", ['Inserir', [hora_data], 'Converter letras para...', [maiuscula, minuscula, p_letra_maiuscula]]],
    ['Visualizar', ['Sumário do arquivo']],
    ["Ajuda", [sobre]])


# layout de configuração
layout = [
    [sg.Menu(menu_layout, background_color='#424556', text_color='white', font=('futura', 9))],
    [sg.Multiline(
    font="Futura",
    text_color="white",
    size=(WIN_W, WIN_H),
    key="body_main",
    pad=0,
    sbar_background_color='grey', 
    sbar_trough_color='white', 
    auto_refresh=True,
    background_color='#333645',
    focus=True)
    ]
]


# Janela principal
window = sg.Window(
    title = f"{new_file_name[:-4]} - Bloquim",
    layout = layout,
    margins = (0, 0),
    resizable = True,
    return_keyboard_events = True,
    enable_close_attempted_event = True,
    icon = '.\\resources\\image\\bloco-de-anotacoes.ico'
)



window.read(timeout=1)
window["body_main"].expand(expand_x=True, expand_y=True)

# cria um novo arquivo de texto!
def new_file() -> str:
    if len(values['body_main']) > 0: 
        if sg.popup_yes_no('Você não salvou as alterações do arquivo, tem certeza que deseja criar um novo?', 
        title="Aviso do bloquim!", button_color='#333645', background_color='#424556',
        icon='.\\resources\\image\\bloco-de-anotacoes.ico') == 'Yes':
            window["body_main"].update(value="")
    filename = new_file_name
    return filename


def open_file() -> str:
    try:
        file_name: str = sg.popup_get_file("Open File", 
        no_window=True, icon='.\\resources\\image\\bloco-de-anotacoes.ico')
    except:
        return 'Erro ao abrir o arquivo! :('
    else:
        try:
            with open(file_name, "rt", encoding='utf-8') as file:
                window["body_main"].update(value=file.read())
        except UnicodeDecodeError:
            return sg.Popup("""
                                Aviso!

O arquivo que você quer abrir é incompativél!""", 
grab_anywhere=True, background_color = 'black', button_type=5, font='Futura',
icon='.\\resources\\image\\bloco-de-anotacoes.ico', auto_close=True, no_titlebar=True)           
        except FileNotFoundError:
            return new_file_name
        else:
            return file_name


# Salva o arquivo como '.txt' por padrão!
def save_file(file_name: str):
    if (len(values['body_main']) > 0) and file_name not in (None, ""):
        with open(file_name, "wt", encoding='utf-8') as file:
            file.write(values.get("body_main"))
            return file_name


# Salva o arquivo com nome e formato que você quiser!
def save_file_as() -> str:
    try:
        file_name: str = sg.popup_get_file("Open File", no_window=True, 
        icon='.\\resources\\image\\bloco-de-anotacoes.ico', save_as=True)
    except:
        return 'Arquivo incompativél, tente outro arquivo!'
    else:
        if (len(values['body_main']) > 0) and (file_name not in (None, "")):
            with open(file_name, "wt", encoding='utf-8') as file:
                file.write(values.get("body_main"))
                return file_name
        else:
            return new_file_name

#------------------------ EDITAR OPÇÕES ---------------------------------

# Insere a data e hora atual
def inserir_hora_data():
    return window["body_main"].update(value=str(values["body_main"]) + str(datetime.now()))

def tornar_caixa_alta():
    return window["body_main"].update(value=str(values["body_main"]).upper())

def tornar_caixa_baixa():
    return window["body_main"].update(value=str(values["body_main"]).lower())

def tornar_1_letra_caixa_alta():
    return window["body_main"].update(value=str(values["body_main"]).capitalize())


while True:
    event, values = window.read()    

    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == exit):
        if len(values['body_main']) > 0:     
            if sg.popup_yes_no('Você não salvou as alterações do arquivo, tem certeza que deseja sair?',
        title="Aviso do bloquim!", button_color='#333645', icon='.\\resources\\image\\bloco-de-anotacoes.ico', 
        background_color = '#424556') == 'Yes':
                break
        else:
            break
    if event in (file_new, "n:78"):
        window.set_title(new_file())
    if event in (file_open, "o:79"):
        abrir: str = open_file()
        if abrir == '__TIMEOUT__':
            window.set_title(new_file_name)  
        else:
            window.set_title(abrir)

    if event in (file_save, "s:83"):
        window.set_title(save_file(new_file_name))
    if event == (file_save_as):
        window.set_title(save_file_as())
    if event == (hora_data):
        inserir_hora_data()
    if event == (maiuscula):
        tornar_caixa_alta()
    if event == (minuscula):
        tornar_caixa_baixa()
    if event == (p_letra_maiuscula):
        tornar_1_letra_caixa_alta()
    if event == sobre:
        sobre_app()
