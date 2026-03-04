# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY calculator.py .
COPY test_calculator.py .

# Create logs directory
RUN mkdir -p logs

# Run tests during build to verify code
RUN python -m unittest test_calculator -v

# Default command: run the calculator
CMD ["python", "calculator.py"]
