# PASOS PARA INICIAR EL PROYECTO FLASK

1. Clonar el repositorio:
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo

2. Crear y activar el entorno virtual:
   python3 -m venv venv
   source venv/bin/activate        # En Windows: venv\Scripts\activate

3. Instalar las dependencias:
   pip install -r requirements.txt

4. Crear archivo .env con las variables de entorno:
   SECRET_KEY=clave-super-secreta

5. Crear archivo .flaskenv con la configuración de Flask CLI:
   FLASK_APP=run.py
   FLASK_ENV=development

6. Ejecutar el servidor:
   flask run

7. Probar en el navegador:
   http://127.0.0.1:5000

8. Ejecutar tests (opcional):
   pytest
