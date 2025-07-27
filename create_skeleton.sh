# Create top-level directories
mkdir -p backend frontend docker scripts docs

echo "✅ Created top-level directories: backend, frontend, docker, scripts, docs"

# Create the complete backend directory structure
mkdir -p backend/config/settings
mkdir -p backend/apps/accounts backend/apps/aircraft backend/apps/lru backend/apps/flight_activities backend/apps/installation_removal backend/apps/maintenance backend/apps/reports backend/apps/documents backend/apps/common
mkdir -p backend/core/services backend/core/validators backend/core/constants
mkdir -p backend/media/documents backend/media/reports
mkdir -p backend/templates
mkdir -p backend/fixtures

# Add __init__.py files to make directories Python packages
touch backend/config/__init__.py
touch backend/config/settings/__init__.py
touch backend/apps/__init__.py
touch backend/core/__init__.py
touch backend/core/services/__init__.py    # <-- ADDED
touch backend/core/validators/__init__.py  # <-- ADDED
touch backend/core/constants/__init__.py   # <-- ADDED

for app in accounts aircraft lru flight_activities installation_removal maintenance reports documents common; do
    touch backend/apps/$app/__init__.py
done

echo "✅ Created detailed backend directory structure."
echo "➡️  Next, you will initialize the frontend with Vite."
