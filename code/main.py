if __name__ == '__main__':
    import tkinter
    from stream_url_generator import generate_url_pair, open_window
    
    root = tkinter.Tk(screenName='StreamOBS', baseName='streamobs', className='StreamOBS')
    root.geometry('350x100')

    texto_boas_vindas = tkinter.Label(root, text='StreamOBS: Gerador de URL para transmissão de tela')
    botao_gerar_urls = tkinter.Button(root, text='Gerar URLS', width=10, command=open_window)

    texto_boas_vindas.pack(pady=10)
    botao_gerar_urls.pack(pady=10)

    root.mainloop()