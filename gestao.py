from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Pasta onde as imagens estão localizadas
image_folder = "static"

# Mapeamento de nomes de colunas para URLs dos gráficos
column_chart_mapping = {
    "Data": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwLhUU91HJTLP2jwfLkJ1sD8lrhpkVwy8Ea8hEYOx4VCDU5BamiCk0FEawL8gEMN3OFrEyNPTYHvfD/pubchart?oid=500388460&amp;format=interactive",
    "Mês": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwLhUU91HJTLP2jwfLkJ1sD8lrhpkVwy8Ea8hEYOx4VCDU5BamiCk0FEawL8gEMN3OFrEyNPTYHvfD/pubchart?oid=1643534116&format=interactive",
    "Loja": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwLhUU91HJTLP2jwfLkJ1sD8lrhpkVwy8Ea8hEYOx4VCDU5BamiCk0FEawL8gEMN3OFrEyNPTYHvfD/pubchart?oid=693678060&format=interactive",
    "Turno": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwLhUU91HJTLP2jwfLkJ1sD8lrhpkVwy8Ea8hEYOx4VCDU5BamiCk0FEawL8gEMN3OFrEyNPTYHvfD/pubchart?oid=599875144&format=interactive",
    "Vigilante": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwLhUU91HJTLP2jwfLkJ1sD8lrhpkVwy8Ea8hEYOx4VCDU5BamiCk0FEawL8gEMN3OFrEyNPTYHvfD/pubchart?oid=1836405538&format=interactive",
    "Fiscal": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwLhUU91HJTLP2jwfLkJ1sD8lrhpkVwy8Ea8hEYOx4VCDU5BamiCk0FEawL8gEMN3OFrEyNPTYHvfD/pubchart?oid=391302009&format=interactive",
    "Setor": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwLhUU91HJTLP2jwfLkJ1sD8lrhpkVwy8Ea8hEYOx4VCDU5BamiCk0FEawL8gEMN3OFrEyNPTYHvfD/pubchart?oid=391302009&format=interactive",
    "Valor": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwLhUU91HJTLP2jwfLkJ1sD8lrhpkVwy8Ea8hEYOx4VCDU5BamiCk0FEawL8gEMN3OFrEyNPTYHvfD/pubchart?oid=391302009&format=interactive",
    "Classificação": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwLhUU91HJTLP2jwfLkJ1sD8lrhpkVwy8Ea8hEYOx4VCDU5BamiCk0FEawL8gEMN3OFrEyNPTYHvfD/pubchart?oid=391302009&format=interactive",
    "Perda2024": "https://docs.google.com/spreadsheets/d/e/2PACX-1vTOB_dRsW9zmewOw4eBR385CVCDQUDOpxBzNq9TfcZl9TyCEXfvU8FHIKrR71p5dSkLC5Rgkgm2uf0c/pubchart?oid=983004117&amp;format=interactive",
    "Perda": "https://docs.google.com/spreadsheets/d/e/2PACX-1vTOB_dRsW9zmewOw4eBR385CVCDQUDOpxBzNq9TfcZl9TyCEXfvU8FHIKrR71p5dSkLC5Rgkgm2uf0c/pubchart?oid=1461239993&amp;format=interactive",
    "Acompanhados": "https://docs.google.com/spreadsheets/d/e/2PACX-1vTOB_dRsW9zmewOw4eBR385CVCDQUDOpxBzNq9TfcZl9TyCEXfvU8FHIKrR71p5dSkLC5Rgkgm2uf0c/pubchart?oid=460858368&amp;format=interactive",
}


@app.route("/", methods=["GET", "POST"])
def index():
    selected_charts = []

    if request.method == "POST":
        selected_column = request.form["seletor"]
        if selected_column in column_chart_mapping:
            selected_chart = column_chart_mapping[selected_column]
            if selected_chart not in selected_charts:
                if len(selected_charts) >= 3:
                    selected_charts.pop(0)  # Remove o gráfico mais antigo da fila
                selected_charts.append(selected_chart)

    return render_template(
        "index.html",
        column_chart_mapping=column_chart_mapping,
        selected_charts=selected_charts,
    )


if __name__ == "__main__":
    app.run(debug=True)
