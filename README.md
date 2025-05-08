# Python Project: README Generator

This project provides a Python script (`main.py`) to scan directories and generate README files for Ansible roles and Terraform modules. The script uses the OpenAI API to analyze the files in a directory and create a README file that adheres to best practices for the identified project type.

## Features

- **Directory Scanning**: Recursively scans a directory and its subdirectories to collect file data.
- **Project Type Identification**: Automatically identifies whether the directory contains an Ansible role, a Terraform module, or an unknown project type.
- **README Generation**: Generates a README file tailored to the project type using the OpenAI API.

## Prerequisites

- Python 3.x
- OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <repository-directory>
   ```
3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script and provide the directory to scan:
   ```bash
   python3 main.py
   ```
2. Enter the path to the directory you want to scan when prompted.
3. The script will generate a `README.md` file in the specified directory.

## How It Works

1. **Scanning**: The script reads all files in the specified directory and its subdirectories.
2. **Project Type Detection**:
   - If the directory contains Ansible-related files (e.g., `tasks/main.yml`), it identifies the project as an Ansible role.
   - If the directory contains Terraform files (e.g., `.tf` files), it identifies the project as a Terraform module.
   - Otherwise, it labels the project type as unknown.
3. **README Generation**: The script uses the OpenAI API to generate a README file based on the project type and the collected file data.

## Example

To generate a README for an Ansible role:

1. Place the Ansible role files in a directory (e.g., `my-ansible-role/`).
2. Run the script and specify the directory path:
   ```bash
   python3 main.py
   ```
3. The script will create a `README.md` file in the `my-ansible-role/` directory.

## Limitations

- The script relies on the OpenAI API for README generation, so an active internet connection and a valid API key are required.
- The generated README is based on the file structure and content; it does not invent details.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.