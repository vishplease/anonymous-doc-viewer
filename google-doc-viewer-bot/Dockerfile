# Base image with Python
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install necessary dependencies for Chromium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    libxshmfence1 \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy files
COPY requirements.txt .
COPY google_doc_viewers.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and required browsers
RUN playwright install --with-deps chromium

# Set entrypoint
CMD ["python", "google_doc_viewers.py"]
