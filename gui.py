# Projeto de introdução a GUI (Graphic User Interface)

import PySimpleGUI as psg

#Desenhar o layout da tela
layout = [
    [psg.Text('***'), psg.Text('-----------------------------'),psg.Text('***')],
    [psg.Text('***'), psg.Button(' --- Clique Aqui! ---'), psg.Text('***')],
    [psg.Text('***'), psg.Text('-----------------------------'),psg.Text('***')],
    ]

window = psg.Window('Minha primeira Gui Python...', layout)

while True:
    evento, valor = window.read()

    if evento == psg.WIN_CLOSED:
        break
    else:
        psg.popup('--- Programação em Python ---\n''Botão clicado!')

window.close()
