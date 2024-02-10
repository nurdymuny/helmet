#!/usr/bin/env python3
import argparse
import os
import yaml
from getpass import getpass

# Function to create chart and templates directories
def create_directory_structure(chart_name):
    chart_directory = f"{chart_name}-chart"
    templates_directory = os.path.join(chart_directory, "templates")
    os.makedirs(templates_directory, exist_ok=True)
    return chart_directory, templates_directory

# Function to write YAML content to a file
def write_yaml_file(path, content):
    with open(path, "w") as file:
        yaml.dump(content, file, default_flow_style=False)

# Input validation functions
def validate_port(port):
    if not 0 < port < 65536:
        raise ValueError("Port number must be between 1 and 65535.")
    return port

def validate_protocol(protocol):
    if protocol.upper() not in ["TCP", "UDP"]:
        raise ValueError("Protocol must be TCP or UDP.")
    return protocol.upper()

# Generate basic Chart.yaml
def generate_chart_yaml(chart_directory, name, description="A Helm chart for Kubernetes"):
    chart_yaml = {
        "apiVersion": "v2",
        "name": name,
        "description": description,
        "version": "0.1.0",
    }
    write_yaml_file(os.path.join(chart_directory, "Chart.yaml"), chart_yaml)

# Placeholder for additional YAML generation functions for deployment, service, etc.

def interactive_mode():
    print("Entering interactive mode for Helm chart creation.")
    name = input("Enter the name of your application/chart: ")
    port = validate_port(int(input("Enter the port number your application uses: ")))
    protocol = validate_protocol(input("Enter the protocol (TCP/UDP): "))
    # Placeholder for further interactive input handling

    # After collecting inputs, call the main creation functions with these inputs

def parse_arguments():
    parser = argparse.ArgumentParser(description="Enhanced Helmet: A tool to create Helm charts with extended capabilities.")
    parser.add_argument("--name", type=str, help="Name of the application or Helm chart.")
    parser.add_argument("--port", type=int, help="Port number the application uses.")
    parser.add_argument("--protocol", type=str, choices=['TCP', 'UDP'], help="Protocol used by the application (TCP/UDP).")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode to input configurations step by step.")
    # Add additional argument parsers as needed for new features
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.interactive:
        interactive_mode()
    else:
        # If not in interactive mode, validate and use the arguments provided
        port = validate_port(args.port)
        protocol = validate_protocol(args.protocol)
        # Assuming name is mandatory for both interactive and non-interactive modes
        name = args.name
        chart_directory, templates_directory = create_directory_structure(name)
        generate_chart_yaml(chart_directory, name)
        # Call other functions to create additional Kubernetes object files as needed

if __name__ == "__main__":
    main()
