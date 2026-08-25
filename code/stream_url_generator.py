import secrets
from hyperlink_generator import hyperlink
import tkinter
import webbrowser

def open_window():
        window_link = tkinter.Toplevel()
        window_link.title('StreamOBS Links')

        tela_largura = window_link.winfo_screenwidth()
        tela_altura = window_link.winfo_screenheight()
        x_desejado = int((tela_largura / 2) - (300 / 2))
        y_desejado = int((tela_altura / 2) - (200 / 2))

        window_link.geometry(f'300x200+{x_desejado}+{y_desejado}')

        links = generate_url_pair()

        texto_url = tkinter.Label(window_link, text='Links Gerados!')
        texto_url.pack()

        transmission = tkinter.Label(window_link, text='Ir para transmissão de tela')
        transmission.pack(side='top', anchor='center', pady=10)

        button_transmission = tkinter.Button(window_link, width=20, text='LINK DE TRANSMISSÃO', command=lambda: webbrowser.open(links[0]))
        button_transmission.pack(side='top', anchor='center')

        watching = tkinter.Label(window_link, text='Copiar link para assistir transmissão')
        watching.pack(side='top', anchor='center', pady=10)

        button_watching = tkinter.Button(window_link, width=20, text='LINK PARA ASSISTIR', command=lambda: window_link.clipboard_append(links[1]))
        button_watching.pack(side='top', anchor='center')

        copyright_text = tkinter.Label(window_link, text='Todos os direitos reservados Ⓒ 2026 Ana Alice')
        copyright_text.pack(side='bottom', anchor='center')

def generate_url_pair():
    url_transmission = 'https://vdo.ninja/?push={SOMESTREAMID}&ss&q=0'
    url_visualize = 'https://vdo.ninja/?v={SOMESTREAMID}&vb=10000&scale=100'
    stream_id = secrets.token_urlsafe(32)

    if '-' in stream_id:
        stream_id = stream_id.replace('-', '_')      

    url_transmission = url_transmission.format(SOMESTREAMID=stream_id)
    url_visualize = url_visualize.format(SOMESTREAMID=stream_id)

    url_pair = (url_transmission, url_visualize)
    print(url_pair)

    return url_pair
