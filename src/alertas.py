def avaliar(dados):

    alertas = []

    if dados["temperatura"] > 80:
        alertas.append("Temperatura crítica")

    if dados["energia"] < 20:
        alertas.append("Energia baixa")

    if dados["gps"] < 75:
        alertas.append("Falha de GPS")

    if dados["buffer_imagens"] > 80:
        alertas.append("Buffer quase cheio")

    return alertas