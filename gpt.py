#sistema operativo base
FROM debian:11

# Actualiza el sistema operativo
RUN apt-get update
# Instala las dependencias necesarias para la ejecución de GPT-Neo
RUN apt-get install -y curl sudo python3 python3-pip git chromium
RUN curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
RUN apt install -y nodejs
# Copia el script de Python a la imagen Docker
WORKDIR /app
COPY gpt.py ./
COPY index.js ./

# Descarga el modelo de GPT-Neo desde Python y copia los archivos a la imagen Docker
RUN pip3 install transformers
# Define el directorio de trabajo

RUN npm i venom-bot child-process
RUN pip install torch
# Define el comando predeterminado a ejecutar cuando se inicie el contenedor
CMD ["node", "index.js"]
