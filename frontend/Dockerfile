# Use a specific, recent, stable Active LTS Node.js version
FROM node:22.5.0-alpine

# Set the working directory
WORKDIR /app

# Copy package files and install dependencies first
# This creates a layer with all the node_modules
COPY package*.json ./
RUN npm install

# Now copy the rest of the application source code
COPY . .

# Expose the port Vite runs on
EXPOSE 3000

# Command to run the Vite dev server and expose it to the host
CMD ["npm", "run", "dev"]
