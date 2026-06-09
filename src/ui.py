def run_cli(engine):

    print("MISSION CONTROL AI")
    print("Digite sair para encerrar\n")

    while True:

        pergunta = input(">>> ")

        if pergunta.lower() == "sair":
            break

        print(engine.analyze(pergunta))