from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Pasta onde as imagens estão localizadas
image_folder = "static"

# Mapeamento de nomes de colunas para URLs dos gráficos
column_chart_mapping = {
    "Data do fato ?": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsvLY4iX339sxm8INvlUtRfMKs58S1Q8VEWKncGz9aztZ8n3NMJP14IonrXhR5yhM1XbllH6POKUB5/pubchart?oid=903930057&format=interactive",
    "Loja": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsvLY4iX339sxm8INvlUtRfMKs58S1Q8VEWKncGz9aztZ8n3NMJP14IonrXhR5yhM1XbllH6POKUB5/pubchart?oid=1205414947&format=interactive",
    "Segurança": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwLhUU91HJTLP2jwfLkJ1sD8lrhpkVwy8Ea8hEYOx4VCDU5BamiCk0FEawL8gEMN3OFrEyNPTYHvfD/pubchart?oid=693678060&format=interactive",
    "Fiscal": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsvLY4iX339sxm8INvlUtRfMKs58S1Q8VEWKncGz9aztZ8n3NMJP14IonrXhR5yhM1XbllH6POKUB5/pubchart?oid=1828690874&format=interactive",
    "Setor": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsvLY4iX339sxm8INvlUtRfMKs58S1Q8VEWKncGz9aztZ8n3NMJP14IonrXhR5yhM1XbllH6POKUB5/pubchart?oid=344571032&format=interactive",
    "Tipo de Ocorrência": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsvLY4iX339sxm8INvlUtRfMKs58S1Q8VEWKncGz9aztZ8n3NMJP14IonrXhR5yhM1XbllH6POKUB5/pubchart?oid=1835121208&format=interactive",
    "Perda2024": "https://docs.google.com/spreadsheets/d/e/2PACX-1vTOB_dRsW9zmewOw4eBR385CVCDQUDOpxBzNq9TfcZl9TyCEXfvU8FHIKrR71p5dSkLC5Rgkgm2uf0c/pubchart?oid=374117186&format=interactive",
    "Perda": "https://docs.google.com/spreadsheets/d/e/2PACX-1vTOB_dRsW9zmewOw4eBR385CVCDQUDOpxBzNq9TfcZl9TyCEXfvU8FHIKrR71p5dSkLC5Rgkgm2uf0c/pubchart?oid=1461239993&format=interactive",
    "Codigos": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsvLY4iX339sxm8INvlUtRfMKs58S1Q8VEWKncGz9aztZ8n3NMJP14IonrXhR5yhM1XbllH6POKUB5/pubchart?oid=1794182638&format=interactive",
    "Recuperado": "https://docs.google.com/spreadsheets/d/e/2PACX-1vTOB_dRsW9zmewOw4eBR385CVCDQUDOpxBzNq9TfcZl9TyCEXfvU8FHIKrR71p5dSkLC5Rgkgm2uf0c/pubchart?oid=696171317&format=interactive",
    "Recuperado2": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsvLY4iX339sxm8INvlUtRfMKs58S1Q8VEWKncGz9aztZ8n3NMJP14IonrXhR5yhM1XbllH6POKUB5/pubchart?oid=1256223449&format=interactive",
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_charts = []

    if request.method == "POST":
        selected_column = request.form["seletor"]
        if selected_column in column_chart_mapping:
            selected_chart = column_chart_mapping[selected_column]
            if selected_chart not in selected_charts:
                # Limita a exibição a até 3 gráficos, removendo o mais antigo caso necessário
                if len(selected_charts) >= 3:
                    selected_charts.pop(0)
                selected_charts.append(selected_chart)

    return render_template(
        "index.html",
        column_chart_mapping=column_chart_mapping,
        selected_charts=selected_charts,
    )

if __name__ == "__main__":
    # Adiciona a opção de porta configurável por variável de ambiente
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
