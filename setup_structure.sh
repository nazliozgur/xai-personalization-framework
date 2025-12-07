#!/bin/bash
# XAE-Frame Project Structure Setup Script
# Run this in your project root directory

echo "Creating XAE-Frame project structure..."

# Create main directories
mkdir -p data/raw
mkdir -p data/processed
mkdir -p data/models
mkdir -p notebooks
mkdir -p src/data
mkdir -p src/models
mkdir -p src/explainability
mkdir -p src/adaptive
mkdir -p src/ethical
mkdir -p src/business_impact
mkdir -p src/transfer_learning
mkdir -p src/api/routes
mkdir -p src/dashboard/views
mkdir -p src/dashboard/components
mkdir -p src/utils
mkdir -p scripts
mkdir -p tests/unit
mkdir -p tests/integration
mkdir -p configs
mkdir -p docs
mkdir -p logs

# Create .gitkeep files to preserve empty directories
touch data/raw/.gitkeep
touch data/processed/.gitkeep
touch data/models/.gitkeep
touch logs/.gitkeep

# Create __init__.py files for Python packages
touch src/__init__.py
touch src/data/__init__.py
touch src/models/__init__.py
touch src/explainability/__init__.py
touch src/adaptive/__init__.py
touch src/ethical/__init__.py
touch src/business_impact/__init__.py
touch src/transfer_learning/__init__.py
touch src/api/__init__.py
touch src/api/routes/__init__.py
touch src/dashboard/__init__.py
touch src/dashboard/views/__init__.py
touch src/dashboard/components/__init__.py
touch src/utils/__init__.py
touch tests/__init__.py
touch tests/unit/__init__.py
touch tests/integration/__init__.py

echo "Project structure created successfully!"
echo ""
echo "Directory tree:"
tree -L 2 -I '__pycache__|*.pyc|.git' || ls -R
