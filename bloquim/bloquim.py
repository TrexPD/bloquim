import PySimpleGUI as sg
from datetime import datetime
from help import sobre_app


# Escolha de temas
sg.theme("darkgrey")

# Tamanho da janela
WIN_W = 40
WIN_H = 25


new_file_name: str = "Documento de texto.txt"
file_new: str = "Novo arquivo           Ctrl + N"
file_open: str = "Abrir arquivo            Ctrl + O"
file_save: str = "Salvar arquivo         Ctrl + S"
file_save_as: str = "Salvar arquivo como..."
file_print: str = "Imprimir arquivo        Ctrl + P"
exit: str = "Sair"
hora_data: str = "Hora e data atual"
sobre: str = "Sobre"


# menu de cabeçalho!
menu_layout = (
    ["Arquivo", [file_new, file_open, file_save, file_save_as, "---", file_print, "---", exit]],
    ["Editar", [hora_data]],
    ["Ajuda", [sobre]])


# layout de configuração
layout = [
    [sg.Menu(menu_layout, background_color='#424556', text_color='white', font=('futura', 9))],
    [sg.Multiline(
    font=("Futura", 12),
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
        no_window=True, icon='.\\resources\\image\\bloco-de-anotacoes.ico',)
    except:
        return ''
    if file_name not in (None, "") and not isinstance(file_name, tuple):
        try:
            with open(file_name, "rt", encoding='utf-8') as file:
                window["body_main"].update(value=file.read())
        except UnicodeDecodeError:
            return sg.Popup("""
                                Aviso!

O arquivo que você quer abrir é incompativél!
""",
        grab_anywhere=True,
        background_color = 'black',
        button_type=5,
        font='Futura',
        icon='.\\resources\\image\\bloco-de-anotacoes.ico',
        auto_close=True,
        no_titlebar=True
    )           
    return file_name

# Salva o arquivo 
def save_file(file_name: str):
    if len(values['body_main']) > 0:
        if file_name not in (None, ""):
            with open(file_name, "wt", encoding='utf-8') as file:
                file.write(values.get("body_main"))
        else:
            save_file_as()


def save_file_as() -> str:
    try:
        file_name: str = sg.popup_get_file("Open File", no_window=True, 
        icon='.\\resources\\image\\bloco-de-anotacoes.ico', save_as=True)
        # file_name: str = sg.popup_get_file(
        #     "Escolha em qual pasta o arquivo será salvo!",
        #     save_as = True,
        #     no_window = False,
        #     default_extension = ".txt",
        #     file_types = (("Text", ".txt", '.py', '.rs', '.csv')),
        #     initial_folder = '', # Escolhe qual será o 'path' inical!
        #     history = True, # Mostra o historico de 'paths' pesquisados!
        #     background_color = '#424556',
        #     button_color = '#333645',
        #     size=(30, 15),
        #     icon='bloco-de-anotacoes.ico'
        # )
    except:
        return 'Arquivo incompativél!'
    if file_name not in (None, "") and not isinstance(file_name, tuple):
        with open(file_name, "wt", encoding='utf-8') as file:
            file.write(values.get("body_main"))
    return file_name


# def tornar_caixa_baixa():
#     return window["body_main"].update(value=str(values["body_main"]).lower())


# def tornar_caixa_alta():
#     return window["body_main"].update(value=str(values["body_main"]).upper())
    

# Insere a data e hora atual
def inserir_hora_data():
    return window["body_main"].update(value=str(values["body_main"]) + str(f'\n{datetime.now()}'))



while True:
    event, values = window.read()    

    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Sair'):
        if len(values['body_main']) > 0:     
            if sg.popup_yes_no('Você não salvou as alterações do arquivo, tem certeza que deseja sair?',
        title="Aviso do bloquim!", button_color='#333645', icon='.\\resources\\image\\bloco-de-anotacoes.ico', 
        background_color = '#424556') == 'Yes':
                break
        else:
            break
    if event in (file_new, "n:78"):
        new_file_name = new_file()
    if event in (file_open, "o:79"):
        new_file_name = open_file()
    if event in (file_save, "s:83"):
        save_file(new_file_name)
    if event == (file_save_as):
        filename = save_file_as()
    if event == (hora_data):
        inserir_hora_data()
    if event == sobre:
        sobre_app()
