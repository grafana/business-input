# Get the latest version of Playwright
FROM mcr.microsoft.com/playwright:v1.57.0-noble

# Set the work directory for the application
WORKDIR app

# COPY the needed files to the app folder in Docker image
COPY .. .

# Run tests
CMD ["yarn", "e2e"]
