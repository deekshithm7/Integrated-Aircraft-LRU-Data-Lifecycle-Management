# 🛩️ LRU Management System

This is an Integrated Aircraft LRU Data & Lifecycle Management System.

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js & npm

### Setup and Run
1.  **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd lru-management
    ```

2.  **Set up environment variables**
    ```bash
    cp .env.example .env
    ```
    *Note: You can edit the `.env` file if needed, but the defaults are set up for Docker.*

3.  **Build and start the containers**
    ```bash
    docker-compose up --build -d
    ```

4.  **Access the applications**
    -   **Frontend**: [http://localhost:3000](http://localhost:3000)
    -   **Backend API**: [http://localhost:8000](http://localhost:8000)

### Development
- To see logs: `docker-compose logs -f`
- To stop services: `docker-compose down`
