# Ansible Role: Docker

This Ansible role installs and configures Docker on various operating systems. It supports multiple distributions including Archlinux, Alpine, Debian, and RedHat-based systems.

## Table of Contents

- [Purpose](#purpose)
- [Requirements](#requirements)
- [Role Variables](#role-variables)
- [Dependencies](#dependencies)
- [Example Playbook](#example-playbook)
- [License](#license)
- [Author Information](#author-information)

## Purpose

The purpose of this Ansible role is to streamline the installation and configuration of Docker on different Linux distributions. It ensures that Docker is installed with the necessary configurations and dependencies, making it easier to manage Docker environments across multiple servers.

## Requirements

This role requires Ansible 2.9 or higher. It is tested on the following platforms:

- Archlinux
- Alpine
- Debian
- RedHat-based systems (e.g., CentOS, Fedora)

## Role Variables

The main variables for this role are defined in `defaults/main.yml`. The following is a list of the most important variables:

- `docker_edition`: Docker edition to install (e.g., 'ce' for Community Edition).
- `docker_package`: Docker package name.
- `docker_package_state`: Desired state of the Docker package (e.g., 'present').
- `docker_install_compose_plugin`: Whether to install Docker Compose plugin.
- `docker_compose_version`: Version of Docker Compose to install.
- `docker_users`: List of system users to add to the Docker group.

For distribution-specific variables, refer to the respective files in the `vars` directory:

- `vars/Archlinux.yml`
- `vars/Alpine.yml`
- `vars/Debian.yml`
- `vars/RedHat.yml`

## Dependencies

This role does not have any external dependencies. However, it uses the following Ansible collections:

- `community.general`
- `ansible.builtin`

## Example Playbook

Here is an example playbook that uses this role:

```yaml
---
- name: Install and configure Docker
  hosts: all
  become: true
  roles:
    - role: ansible-role-docker
      vars:
        docker_edition: 'ce'
        docker_install_compose_plugin: true
        docker_compose_version: '2.10.2'
        docker_users:
          - user1
          - user2
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author Information

This role was created and is maintained by [Your Name or Organization].

---

This README.md file follows Ansible best practices by clearly defining the role's purpose, requirements, variables, dependencies, and usage. It also includes a license section and author information for proper attribution.