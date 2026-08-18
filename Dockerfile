# Use an official lightweight Python runtime
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all local project files into the container
COPY . /app

# Install the required Python packages
RUN pip install pandas streamlit

# Expose port 8501 for the Streamlit dashboard
EXPOSE 8501

# Command to run the dashboard when the container launches
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]