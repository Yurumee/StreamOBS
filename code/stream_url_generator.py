import secrets
from hyperlink_generator import hyperlink

def generate_url_pair():
    url_transmission = 'https://vdo.ninja/?push={SOMESTREAMID}&ss&q=0'
    url_visualize = 'https://vdo.ninja/?v={SOMESTREAMID}&vb=10000&scale=100'
    stream_id = secrets.token_urlsafe(32)

    url_transmission = url_transmission.format(SOMESTREAMID=stream_id)
    url_visualize = url_visualize.format(SOMESTREAMID=stream_id)

    link_stream = hyperlink(url_transmission, 'URL PARA TRANSMISSAO')
    link_watch = hyperlink(url_visualize, 'URL PARA ASSISTIR')

    return f'Transmita sua tela aqui: {link_stream} \n Compartilhe este link para assistir: {link_watch}' 