FROM python:3.8-slim

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y git

# Clona Sublist3r y lo instala
RUN git clone https://github.com/aboul3la/Sublist3r.git /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "sublist3r.py"]
