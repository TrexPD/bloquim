import PySimpleGUI as sg
from re import findall, sub



class Summary:
    def __init__(self, content: str):
        self.text = content

    def number_of_lines(self) -> int:
        quebra_de_linha = findall('\n', self.text)
        linhas = len(quebra_de_linha)
        if linhas == 0 or linhas > 0:
            return linhas + 1

    def amount_of_characters(self) -> int: 
        return len(self.text.replace('\n', ''))

    def amount_of_letters(self) -> int:  
        letters: list = findall(r'[a-zA-ZÀ-ú]', self.text)
        return len(letters)

    def amount_of_words(self) -> int:
        words: list = sub(r"\W+", " ", self.text)
        return len(words.split())

    def amount_of_numbers(self) -> int:
        numbers: list = findall(r'\d', self.text)
        return len(numbers)





def sumario(file: str):
    summary = Summary(file)
    resumo: str = f"""
Quantidade de caracteres:       {summary.amount_of_characters()}
Quantidade de letras:               {summary.amount_of_letters()}
Quantidade de números:           {summary.amount_of_numbers()}
Quantidade de linhas:               {summary.number_of_lines()}
Quantidade de palavras:           {summary.amount_of_words()}
"""
    return sg.Popup(resumo,
        title='Sumário do arquivo!',
        grab_anywhere=True,
        background_color = '#424556',
        button_type=5,
        font=('Futura', 15),
        icon='.\\resources\\image\\bloco-de-anotacoes.ico'
)