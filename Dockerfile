FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    python3-pyqt5 \
    libgl1-mesa-glx \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]