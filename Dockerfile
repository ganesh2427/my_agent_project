FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg git

# Set workdir
WORKDIR /app

# Copy everything
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose default Streamlit port
EXPOSE 7860

# Run your app
CMD ["bash", "start.sh"]