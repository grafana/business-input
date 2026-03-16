# Get the latest version of Playwright
FROM mcr.microsoft.com/playwright:v1.58.2-noble@sha256:6446946a1d9fd62d9ae501312a2d76a43ee688542b21622056a372959b65d63d

# Set the work directory for the application
WORKDIR app

# COPY the needed files to the app folder in Docker image
COPY .. .

# Install the dependencies in Node environment
RUN yarn install

# Run tests
CMD ["yarn", "e2e"]
