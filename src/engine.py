from src.telemetria import coletar
from src.alertas import avaliar

class MissionEngine:

    def is_ready(self):
        return True

    def status_snapshot(self):

        dados = coletar()

        return (
            f"Temperatura: {dados['temperatura']}°C\n"
            f"Energia: {dados['energia']}%\n"
            f"GPS: {dados['gps']}%\n"
            f"Buffer: {dados['buffer_imagens']}%"
        )

    def analyze(self, pergunta_usuario):

        dados = coletar()

        alertas = avaliar(dados)

        return (
            f"\nPergunta: {pergunta_usuario}\n\n"
            f"Dados:\n{dados}\n\n"
            f"Alertas:\n{alertas}"
        )