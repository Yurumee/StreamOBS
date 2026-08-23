def hyperlink(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)

# mais sobre como essa mascara funciona e o funcionamento do OST8 para criação dos hyperlinks pode ser visto no link abaixo
# https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda