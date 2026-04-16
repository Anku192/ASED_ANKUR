# Use Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements first (for faster builds)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Run both ML and DL scripts
CMD ["sh", "-c", "python ased_machine_learning_py.py && python ased_deep_learning.py"]