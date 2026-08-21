# Get the latest version of Playwright
FROM mcr.microsoft.com/playwright:v1.61.1-noble@sha256:5b8f294aff9041b7191c34a4bab3ac270157a28774d4b0660e9743297b697e48

# Set the work directory for the application
WORKDIR /app

# COPY the needed files to the app folder in Docker image
COPY .. .

# Install the dependencies in Node environment
RUN npm ci

# Run tests
CMD ["npm", "run", "e2e"]
