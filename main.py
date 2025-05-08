import logging
import os
from openai import OpenAI

import httpx
import argparse
from mistralai import Mistral

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set your OpenAI API key
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
mistral_client = Mistral(api_key=os.getenv("OPENAI_API_KEY"))

# Create an HTTPX client with proxy and SSL verification disabled
httpx_client = httpx.Client(proxy=os.getenv("HTTP_PROXY"), verify=True)

def scan_directory_and_generate_readme(directory, model):
    logging.info(f"Scanning directory: {directory}")
    file_data = {}

    # Walk through the directory and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                file_data[file_path] = f.read()

    # Analyze the files to determine the project type
    project_type = identify_project_type(file_data)
    logging.info(f"Identified project type: {project_type}")

    # Generate README content based on the project type
    readme_content = generate_readme(file_data, project_type, model)
    logging.info("README content generated successfully.")

    # Save the README file
    readme_path = os.path.join(directory, "README_AI.md")
    with open(readme_path, 'w') as readme_file:
        readme_file.write(readme_content)
    logging.info(f"README file saved at: {readme_path}")

    return readme_content, project_type

def identify_project_type(file_data):
    if any("tasks" in path and path.endswith(".yml") for path in file_data):
        return "ansible"
    elif any(path.endswith(".tf") for path in file_data):
        return "terraform"
    else:
        return "unknown"

def generate_readme(file_data, project_type, model):
    logging.info(f"Generating README for project type: {project_type}")

    api = ""
    response_content = "Not Available"

    if project_type == "ansible":
        prompt = """
        You are an expert in Ansible best practices. Based on the following files, generate a README.md file that describes the Ansible role, its purpose, variables, dependencies, and usage. Ensure the README follows Ansible best practices.
        Files: {files}
        """.format(files=list(file_data.keys()))
    elif project_type == "terraform":
        prompt = """
        You are an expert in Terraform and HashiCorp recommendations. Based on the following files, generate a README.md file that describes the Terraform module, its purpose, inputs, outputs, and usage. Ensure the README follows HashiCorp best practices.
        Files: {files}
        """.format(files=list(file_data.keys()))
    else:
        prompt = """
        Based on the following files, generate a README.md file that describes the project, its purpose, and usage. Ensure the README is as accurate as possible.
        Files: {files}
        """.format(files=list(file_data.keys()))

    if api == "mistral":
        # Call Mistral API to generate the README content
        logging.info("Calling Mistral API")
        # response = mistral_client.chat.complete(
        #     messages=[
        #         {
        #             "role": "user",
        #             "content": prompt,
        #         },
        #     ],
        #     model=model,
        #     max_tokens=1500)
        # response_content = response.choices[0].message.content

    else:
        # Call OpenAI API to generate the README content
        logging.info("Calling OpenAI API")

        openai_client.base_url = "https://api.mistral.ai/v1"
 
        # Example: Make a request to the Mistral API
        response = openai_client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            max_tokens=1500,
            temperature=0.7,
        )

        response_content = response_content = response.choices[0].message.content
        print(response_content)

    return response_content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a README file for a given directory.")
    parser.add_argument("--directory", required=True, help="Path to the directory to scan.",
                        default="/workspaces/Daisei/tests/ansible/ansible-role-docker-master")
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", "mistral-large-latest"),
                        help="OpenAI model to use for generating the README.")
    parser.add_argument("--api_key", default=os.getenv("OPENAI_API_KEY"), help="OpenAI API key.")

    args = parser.parse_args()

    if not args.api_key:
        print("Error: OpenAI API key is required. Set it via the --api_key parameter or the OPENAI_API_KEY environment variable.")
        exit(1)

    try:
        readme, project_type = scan_directory_and_generate_readme(args.directory, args.model)
        print(f"README generated for project type: {project_type}")
    except Exception as e:
        print(f"Error: {e}")
