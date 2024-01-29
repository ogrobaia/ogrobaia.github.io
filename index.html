from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Pasta onde as imagens estão localizadas
image_folder = "static"

# Mapeamento de nomes de colunas para nomes de imagens
column_image_mapping = {
    "Mês": "mês.png",
    "Loja": "loja.png",
    "Turno": "turno.png",
    "Vigilante": "vigilante.png",
    "Fiscal": "fiscal.png",
    "Setor": "setor.png",
    "Valor": "valor.png",
    "Classificação": "classificação.png",
}


# Função para obter a lista de nomes de arquivos de imagens na pasta
def get_image_files():
    image_files = []
    for filename in os.listdir(image_folder):
        if filename.endswith(".png"):
            image_files.append(filename)
    return image_files


@app.route("/", methods=["GET", "POST"])
def index():
    image_files = get_image_files()
    selected_image = None

    if request.method == "POST":
        selected_column = request.form["seletor"]
        if selected_column in column_image_mapping:
            selected_image = column_image_mapping[selected_column]

    return render_template(
        "index.html",
        column_image_mapping=column_image_mapping,
        image_files=image_files,
        selected_image=selected_image,
    )


if __name__ == "__main__":
    app.run(debug=True)
