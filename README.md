**Gestão de Desempenho - Relatório de Ações de Segurança RJ**


Descrição do Projeto


Este projeto é uma aplicação web que exibe gráficos interativos e informações sobre ações de segurança em um ambiente de loja. Utiliza Flask como backend e HTML para o frontend. A aplicação permite selecionar e visualizar gráficos baseados em dados específicos.

Estrutura do Projeto
O projeto é composto por duas partes principais:

Código Python (Flask)
Código HTML
Código Python (Flask)
O backend da aplicação é implementado utilizando o framework Flask. Ele gerencia a seleção e exibição dos gráficos.

app = Flask(__name__): Inicializa a aplicação Flask.
image_folder: Define a pasta onde as imagens estão localizadas.
column_chart_mapping: Mapeia nomes de colunas para URLs dos gráficos.
index(): Rota principal que renderiza a página index.html. Permite a seleção e exibição de gráficos baseados na escolha do usuário.
Código HTML
O HTML define a estrutura e o estilo da interface do usuário. Ele inclui links, uma área para gráficos e um formulário incorporado do Google.


Todo o projeto utiliza ferramentas gratuitas sem custo para a empresa.
