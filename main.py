import os
from mistralai import Mistral

# Initialize Mistral API client
mistral_client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
model = "mistral-large-latest"

def scan_directory_and_generate_readme(directory):
    file_data = {}

    # Walk through the directory and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                file_data[file_path] = f.read()

    # Analyze the files to determine the project type
    project_type = identify_project_type(file_data)

    # Generate README content based on the project type
    readme_content = generate_readme(file_data, project_type)

    # Save the README file
    readme_path = os.path.join(directory, "README_AI.md")
    with open(readme_path, 'w') as readme_file:
        readme_file.write(readme_content)

    return readme_content, project_type


def identify_project_type(file_data):
    if any("tasks" in path and path.endswith(".yml") for path in file_data):
        return "ansible"
    elif any(path.endswith(".tf") for path in file_data):
        return "terraform"
    else:
        return "unknown"


def generate_readme(file_data, project_type):
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

    # Call Mistral API to generate the README content
    response = mistral_client.chat.complete(
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        model=model,
        max_tokens=1500)
    
    print(response.choices[0].message.content)

    return response.choices[0].message.content


if __name__ == "__main__":
    directory_to_scan = input("Enter the directory to scan: ")
    readme, project_type = scan_directory_and_generate_readme(
        directory_to_scan)
    print(f"README generated for project type: {project_type}")
