import random

def coletar():

    dados = {
        "temperatura": random.randint(20, 100),
        "energia": random.randint(0, 100),
        "gps": random.randint(70, 100),
        "buffer_imagens": random.randint(0, 100)
    }

    return dados