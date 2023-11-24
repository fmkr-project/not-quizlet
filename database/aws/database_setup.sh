#!/bin/bash

# Get the directory of the current script
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Define the location of the .env file relative to the script directory
env_location="$script_dir/../../backend/env/.env"

# Check if the .env file exists
if [ ! -f "$env_location" ]; then
    echo "Error: .env file not found at $env_location"
    exit 1
fi

# Load Environment Variables
set -o allexport
source "$env_location"
set +o allexport

# Use environment variables to connect to the database
mysql -h $DATABASE_ENDPOINT -P $DATABASE_PORT -u $MASTER_USERNAME_DATABASE -p $PASSWORD_DATABASE
