"""
Integration test script that runs both the NestJS API server and Python client.
This demonstrates the full-stack interaction between Python ML models and NestJS API.
"""

import subprocess
import time
import os
import sys
import requests
import json
import signal

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

def start_nestjs_server():
    """Start the NestJS server in a subprocess"""
    print("Starting NestJS API server...")
    dataapi_dir = os.path.join(project_root, "apps", "dataapi")
    
    # This command will start the NestJS API server in the background
    server_process = subprocess.Popen(
        ["pnpm", "run", "start"],
        cwd=dataapi_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        preexec_fn=os.setsid  # Used later to kill process group
    )
    
    # Wait for the server to start
    print("Waiting for server to start...")
    max_attempts = 30
    attempts = 0
    server_url = "http://localhost:3000/api"
    
    while attempts < max_attempts:
        try:
            response = requests.get(server_url)
            if response.status_code == 200:
                print("NestJS API server is running!")
                return server_process
        except requests.RequestException:
            pass
        
        time.sleep(1)
        attempts += 1
        print(f"Waiting for server... ({attempts}/{max_attempts})")
    
    print("Failed to start server within the timeout period.")
    kill_process_group(server_process)
    sys.exit(1)

def kill_process_group(process):
    """Kill a process and all its children"""
    try:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        print("Server process terminated.")
    except Exception as e:
        print(f"Error killing process: {e}")

def run_api_client_tests():
    """Run tests against the API"""
    base_url = "http://localhost:3000/api"
    
    print("\n" + "=" * 60)
    print("TESTING THE NESTJS API".center(60))
    print("=" * 60 + "\n")
    
    # Test the root endpoint
    print("1. Testing root endpoint...")
    response = requests.get(base_url)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test the models endpoint
    print("\n2. Testing models endpoint...")
    response = requests.get(f"{base_url}/models")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test prediction with linear regression model
    print("\n3. Testing linear regression prediction...")
    response = requests.post(
        f"{base_url}/models/linear_regression/predict",
        json={"data": {"x": 7}}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test prediction with classification model
    print("\n4. Testing random forest classification...")
    response = requests.post(
        f"{base_url}/models/random_forest/predict",
        json={"data": {"features": [4, 5, 6]}}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    print("\n" + "=" * 60)
    print("API TESTS COMPLETED".center(60))
    print("=" * 60 + "\n")

def main():
    """Main function that orchestrates the integration test"""
    try:
        # Start the NestJS server
        server_process = start_nestjs_server()
        
        # Run client API tests
        run_api_client_tests()
        
    except KeyboardInterrupt:
        print("\nInterrupted by user. Shutting down...")
    except Exception as e:
        print(f"Error during test: {e}")
    finally:
        # Clean up the server process
        if 'server_process' in locals():
            kill_process_group(server_process)

if __name__ == "__main__":
    main()
