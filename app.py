import string
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Almacenamiento de datos en memoria (lista de diccionarios) para las urls recortadas (Temporal)
# {id: {original_url: url, short_url: short_url, created_at: datetime}} Como los datos son temporales, se usara un diccionario de python para almacenarlos.
url_database = {}

def generar_codigo(length=6):
    """Genera una cadena aleatoria de letras y números para el link corto."""
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url_larga = request.form.get('url_larga')
        alias_personalizado = request.form.get('alias', '').strip()  # <-- Asegúrate de que esta línea exista
        # Validar que no esté vacío
        if not url_larga:
            return render_template('index.html', error="Por favor ingresar una URL válida.")


        # Lógica para el alias personalizado vs código aleatorio
        if alias_personalizado:
            #validar que no exista ya en la base de datos
            if alias_personalizado in url_database:
                return render_template('index.html', error="El alias {alias_personalizado} ya existe. Por favor ingrese otro.")
            codigo = alias_personalizado
        else:
            # Generar un código único
            codigo = generar_codigo()
            while codigo in url_database:
                codigo = generar_codigo()

        # Guardar en nuestra base de datos simulada
        url_database[codigo] = url_larga

        #construir el link acortado para mostrarlo en la vista de éxito
        link_corto = request.host_url + codigo
        return render_template('success.html', link_corto=link_corto, url_larga=url_larga)

    return render_template('index.html')

@app.route('/<codigo>')
def redirigir(codigo):
    """Busca el código corto y redirige a la URL original."""
    url_larga = url_database.get(codigo)
    if url_larga:
        return redirect(url_larga)
    return "¡Ups! Este enlace no existe o ha expirado.", 404

if __name__ == '__main__':
    app.run(debug=True)