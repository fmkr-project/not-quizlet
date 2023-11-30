#!/bin/bash

# Function to install Python dependencies
install_python_dependencies() {
    echo "Installing Python dependencies..."
    pip install -r ../../backend/requirements.txt --break-system-packages
    if [ $? -ne 0 ]; then
        echo "Failed to install Python dependencies."
        exit 1
    fi
    echo "Python dependencies installed successfully."
}

# Function to install Node dependencies
install_node_dependencies() {
    echo "Installing Node.js dependencies..."
    npm install --prefix ../../frontend
    if [ $? -ne 0 ]; then
        echo "Failed to install Node.js dependencies."
        exit 1
    fi
    echo "Node.js dependencies installed successfully."
}

# Main installation function
main() {
    echo "Starting project setup..."

    if [ -d "../../backend" ] && [ -d "../../frontend" ]; then
        install_python_dependencies
        install_node_dependencies
        echo "Project setup completed successfully."
    else
        echo "Required directories (backend/frontend) not found."
        exit 1
    fi
}

# Execute the main function
main
