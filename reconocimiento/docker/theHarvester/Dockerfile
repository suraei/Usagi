FROM python:3.8-slim

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y git

# Clona theHarvester y lo instala
RUN git clone https://github.com/laramies/theHarvester.git /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "theHarvester.py"]
