FROM python:3.11-slim

# Imposta la cartella di lavoro
WORKDIR /app

# Copia file di configurazione e script
COPY requirements.txt .
COPY bot.py .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Comando di avvio
CMD ["python", "bot.py"]
