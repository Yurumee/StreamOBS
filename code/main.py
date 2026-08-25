if __name__ == '__main__':
    import tkinter
    from stream_url_generator import generate_url_pair, open_window
    
    root = tkinter.Tk(screenName='StreamOBS', baseName='streamobs', className='StreamOBS')
    tela_largura = root.winfo_screenwidth()
    tela_altura = root.winfo_screenheight()
    x_desejado = int((tela_largura / 2) - (350 / 2))
    y_desejado = int((tela_altura / 2) - (100 / 2))

    root.geometry(f'350x100+{x_desejado}+{y_desejado}')

    texto_boas_vindas = tkinter.Label(root, text='StreamOBS: Gerador de URL para transmissão de tela')
    botao_gerar_urls = tkinter.Button(root, text='Gerar URLS', width=10, command=open_window)

    texto_boas_vindas.pack(pady=10)
    botao_gerar_urls.pack(pady=10)

    root.mainloop()