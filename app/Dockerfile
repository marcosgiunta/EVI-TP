FROM python:3.10
# Establecer el directorio de trabajo en /app. COPY sirve para copiar los archivos de la aplicación al contenedor
WORKDIR /app
COPY . /app
# Installar las dependencias del archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 
# Comando para ejecutar la aplicación
CMD ["python", "app.py"]