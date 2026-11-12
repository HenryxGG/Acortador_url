# Acortador_url
🔗 Acortador de Enlaces Web

Una aplicación web sencilla, rápida y responsiva construida con Python y Flask que permite convertir enlaces largos en URLs cortas y limpias, con soporte para alias personalizados. Proyecto desarrollado como parte de mi portafolio de desarrollo web.

🚀 Características

Acortamiento instantáneo: Genera códigos alfanuméricos aleatorios de 6 caracteres.

Alias personalizados: Permite a los usuarios elegir su propio texto personalizado para el enlace corto (ej. tudominio.com/mi-proyecto).

Copiado rápido: Botón integrado con JavaScript para copiar el enlace generado al portapapeles con un solo clic.

Diseño moderno: Interfaz limpia y responsiva estilizada con Tailwind CSS.

Listo para producción: Configurado para despliegue serverless en Vercel.

🛠️ Tecnologías Utilizadas

Backend: Python 3, Flask

Frontend: HTML5, Tailwind CSS (vía CDN), JavaScript

Despliegue: GitHub & Vercel

💻 Instalación y Ejecución Local

Si deseas correr este proyecto en tu propia computadora, sigue estos pasos:

Clona el repositorio:

git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio


Crea y activa un entorno virtual:

python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate


Instala las dependencias:

pip install -r requirements.txt


Ejecuta la aplicación:

python app.py


Abre tu navegador y ve a http://127.0.0.1:5000.

📁 Estructura del Proyecto

├── static/             # Archivos estáticos (CSS)
├── templates/          # Plantillas HTML (index.html, success.html)
├── app.py              # Lógica principal y rutas de Flask
├── requirements.txt    # Dependencias del proyecto
├── vercel.json         # Configuración de despliegue para Vercel
└── README.md           # Documentación del proyecto


Desarrollado por Henry Guerrero 