# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.10-bullseye

# Instalación de utilidades adicionales
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Configuración del directorio de trabajo
WORKDIR /workspace

# Copia el requirements
COPY requirements.txt /workspace/requirements.txt

# Instala dependencias de Python
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Por defecto, usa bash
CMD [ "bash" ]
