# 🛩️ LRU Management System

This is an Integrated Aircraft LRU Data & Lifecycle Management System.

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose

### Setup and Run
1.  **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd <name-of-the-project-folder>
    ```

2.  **Set up environment variables**
    ```bash
    cp .env.example .env
    ```
    *Note: The lead developer should provide the team with the correct `SECRET_KEY` to add to this file.*

3.  **Build and start the containers**
    ```bash
    docker-compose up --build -d
    ```

4.  **Access the applications**
    -   **Frontend**: http://localhost:3000
    -   **Backend API**: http://localhost:8000

### Development
- To see logs: `docker-compose logs -f`
- To stop services: `docker-compose down`
