# ANSI -> Escape sequence

# \033[31m
# \033[ - Representação de cores
# \033[0;33;44m
    # 0  -> Style
    # 33 -> Text
    # 44 -> Background
    # m  -> Fechamento

# Códigos para estilo
    # 0 -> None
    # 1 -> Bold
    # 4 -> Underline
    # 7 -> Negative

# Códigos para cores
    # 30 - Black
    # 31 - Red
    # 32 - Green
    # 33 - Yellow
    # 34 - Blue
    # 35 - Magenta
    # 36 - Cyan
    # 37 - White

# Background
    # 40 - Black
    # 41 - Red
    # 42 - Green
    # 43 - Yellow
    # 44 - Blue
    # 45 - Magenta
    # 46 - Cyan
    # 47 - White


print('\033[0;30;41mTeste\033[m')
print('\033[4;33;46mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;37mTeste\033[m')