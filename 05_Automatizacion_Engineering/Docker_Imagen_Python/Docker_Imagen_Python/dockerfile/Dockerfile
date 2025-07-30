# Usar la imagen base de Python 3.12 slim
FROM python:3.12-slim

# Establecer una variable de entorno para evitar buffering en logs
ENV PYTHONUNBUFFERED=1

# Instalar SQLite3, PostgreSQL y dependencias necesarias para Jupyter
RUN apt-get update && apt-get install -y \
    sqlite3 \
    libsqlite3-dev \
    build-essential \
    python3-dev \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar Jupyter Notebook, matplotlib y dependencias adicionales
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install jupyterlab notebook ipykernel matplotlib psycopg2-binary

# Crear directorio de trabajo
WORKDIR /app

# Copiar todos los archivos al contenedor
COPY . /app

# Exponer los puertos para Jupyter Notebook y otro servicio
EXPOSE 8888
EXPOSE 8080

# Iniciar Jupyter Notebook sin autenticación
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8080", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
