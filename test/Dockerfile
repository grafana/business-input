# Get the latest version of Playwright
FROM mcr.microsoft.com/playwright:v1.57.0-noble@sha256:3bed4b1a12f2338642f3d8cba28e291deef3c66bd4a964bbeb3e57bbff511dbd

# Set the work directory for the application
WORKDIR app

# COPY the needed files to the app folder in Docker image
COPY .. .

# Install the dependencies in Node environment
RUN yarn install

# Run tests
CMD ["yarn", "e2e"]
