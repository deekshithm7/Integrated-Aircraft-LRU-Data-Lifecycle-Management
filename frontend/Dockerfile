# Use a specific, recent, stable Active LTS Node.js version
FROM node:22.5.0-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy the rest of the application source code
COPY . .

# Expose the port Vite runs on
EXPOSE 3000

# Command to run the Vite dev server and expose it to the host
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
