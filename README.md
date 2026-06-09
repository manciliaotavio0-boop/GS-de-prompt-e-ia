Mission Control AI - EnviroSat:

Integrantes:

* Otávio Mancilia - RM: 570225
* Tiago Muhlmann - RM: 569569
* Wesley Marques - RM:573915

Descrição do Projeto:

O Mission Control AI é um sistema de monitoramento de satélite desenvolvido para a Global Solution 2026 da FIAP.

O projeto utiliza inteligência artificial para analisar dados de telemetria de um satélite chamado EnviroSat, responsável pelo monitoramento ambiental de queimadas, desmatamento e áreas de preservação.

Problema:

O monitoramento ambiental depende do envio contínuo de dados por satélites. Falhas de energia, superaquecimento ou problemas de comunicação podem comprometer a identificação rápida de queimadas e outros eventos ambientais.

Solução:

O sistema simula um centro de controle espacial capaz de:

* Monitorar dados de telemetria.
* Detectar situações críticas.
* Gerar alertas automáticos.
* Utilizar IA para interpretar os dados e sugerir ações.

Tecnologias Utilizadas:

* Python
* Ollama Cloud
* GitHub
* VS Code

Parâmetros Monitorados:

* Temperatura do satélite
* Nível de energia
* Precisão do GPS
* Buffer de imagens

Regras de Alerta:

* Temperatura acima de 80°C
* Energia abaixo de 20%
* GPS abaixo de 75%
* Buffer de imagens acima de 80%

Uso da Inteligência Artificial:

A IA recebe os dados de telemetria e produz uma análise em linguagem natural contendo:

* Estado da missão
* Problemas detectados
* Impacto ambiental
* Recomendações

Proposta de Valor:

O sistema auxilia equipes ambientais a identificar rapidamente possíveis falhas em satélites de monitoramento.

Ao antecipar problemas operacionais, é possível reduzir atrasos no recebimento de informações críticas sobre queimadas e desmatamento.

 Modelo de Negócio

Software como Serviço (SaaS) para órgãos ambientais, empresas de monitoramento e instituições governamentais.

Impacto Esperado:

* Maior confiabilidade no monitoramento ambiental.
* Redução do tempo de resposta a queimadas.
* Melhor acompanhamento de áreas de preservação.

Estrutura do Projeto:

mission-control-ai/

* main.py
* README.md
* requirements.txt
* src/
* prompts/
* assets/

Como Executar:

1. Clonar o repositório.
2. Instalar as dependências:

pip install -r requirements.txt

3. Executar:

python main.py


Adicionar o link do repositório após a publicação.
