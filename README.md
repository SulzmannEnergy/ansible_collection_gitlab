⚠️ This collection is no longer maintained.

# GitLab Ansible Colletion

Ansible collection with roles to install GitLab community edition, enterprise edition and GitLab runners.

[![Tests](https://img.shields.io/github/actions/workflow/status/srv6d/ansible_collection_gitlab/molecule.yml?branch=main&label=Tests)](https://github.com/SRv6d/ansible_collection_gitlab/actions/workflows/molecule.yml)
[![Ansible Galaxy](https://img.shields.io/badge/Ansible%20Galaxy-srv6d.gitlab-blue)](https://galaxy.ansible.com/srv6d/gitlab)

## Example Playbook

```yaml
- hosts: gitlab_ce
  roles:
    - srv6d.gitlab.ce
  vars:
    gitlab_external_url: "https://git.example.com"
    gitlab_letsencrypt_enable: true
    gitlab_disable_signup: true
    gitlab_root_user_password: "TopSecretPassword!"

- hosts: gitlab_runners
  roles:
    - srv6d.gitlab.runner
  vars:
    gitlab_runner_ci_server_url: "https://git.example.com"
    gitlab_runner_registration_token: "Eyohzaemaiso1ahshahj6Ohpeigh2g"
```

## Included Roles

| Role                  | Description                                |
| --------------------- | ------------------------------------------ |
| `srv6d.gitlab.ce`     | Install GitLab Omnibus Community Edition.  |
| `srv6d.gitlab.ee`     | Install GitLab Omnibus Enterprise Edition. |
| `srv6d.gitlab.runner` | Install a GitLab runner.                   |

## Role Variables

### `srv6d.gitlab.ce` / `srv6d.gitlab.ee`

| Variable                                  | Required | Default | Input                     | Comments                                                                                                                               |
| ----------------------------------------- | -------- | ------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| gitlab_external_url                       | **yes**  | _null_  | `str`                     | GitLab URL.                                                                                                                            |
| gitlab_disable_signup                     | no       | `false` | `bool`                    | Disable user sign-up.<br />⚠️ Reactivating signup has to be done using the GUI in addition to setting this variable to `false`.        |
| gitlab_root_user_password                 | no       | _null_  | `str`                     | GitLab root user password.                                                                                                             |
| gitlab_root_user_blocked                  | no       | `false` | `bool`                    | Block GitLab root user.<br />⚠️ Unblocking the root user has to be done using the GUI in addition to setting this variable to `false`. |
| gitlab_nginx_listen_addresses             | no       | _null_  | `list[str]`               | GitLab NGINX listen addresses. If none are defined only unix sockets will be created in '/run/gitlab'.                                 |
| gitlab_nginx_ssl_certificate              | no       | _null_  | `str`                     | Path to GitLab SSL certificate.                                                                                                        |
| gitlab_nginx_ssl_certificate_key          | no       | _null_  | `str`                     | Path to GitLab SSL private key.                                                                                                        |
| gitlab_registry_nginx_listen_addresses    | no       | _null_  | `list[str]`               | GitLab registry NGINX listen addresses. If none are defined only unix sockets will be created in '/run/gitlab'.                        |
| gitlab_registry_nginx_listen_port         | no       | _null_  | `int`                     | GitLab registry NGINX listen port.                                                                                                     |
| gitlab_registry_nginx_ssl_certificate     | no       | _null_  | `str`                     | Path to GitLab registry SSL certificate.                                                                                               |
| gitlab_registry_nginx_ssl_certificate_key | no       | _null_  | `str`                     | Path to GitLab registry SSL private key.                                                                                               |
| gitlab_letsencrypt_enable                 | no       | `false` | `bool`                    | Manage certificates automatically using LetsEncrypt.                                                                                   |
| gitlab_registry_enable                    | no       | `true`  | `bool`                    | Enable GitLab container registry site-wide.                                                                                            |
| gitlab_registry_external_url              | no       | _null_  | `str`                     | GitLab container registry URL.                                                                                                         |
| gitlab_smtp_enable                        | no       | `false` | `bool`                    | Enable GitLab SMTP.                                                                                                                    |
| gitlab_smtp_address                       | no       | _null_  | `str`                     | GitLab SMTP server address.                                                                                                            |
| gitlab_smtp_port                          | no       | `465`   | `int`                     | GitLab SMTP server port.                                                                                                               |
| gitlab_smtp_user_name                     | no       | _null_  | `str`                     | GitLab SMTP server user name.                                                                                                          |
| gitlab_smtp_user_password                 | no       | _null_  | `str`                     | GitLab SMTP server user password.                                                                                                      |
| gitlab_smtp_domain                        | no       | _null_  | `str`                     | GitLab SMTP domain.                                                                                                                    |
| gitlab_smtp_authentication                | no       | _null_  | `str` `"login"`/`"plain"` | GitLab SMTP authentication.                                                                                                            |
| gitlab_smtp_enable_starttls_auto          | no       | _null_  | `bool`                    | Enable SMTP starttls.                                                                                                                  |
| gitlab_smtp_tls                           | no       | _null_  | `bool`                    | Enable SMTP TLS.                                                                                                                       |
| gitlab_email_from                         | no       | _null_  | `str`                     | GitLab Email address that will be used to send Email.                                                                                  |
| gitlab_email_display_name                 | no       | _null_  | `str`                     | GitLab Email display name.                                                                                                             |

### `srv6d.gitlab.runner`

| Variable                             | Required | Default                         | Input       | Comments                                                                       |
| ------------------------------------ | -------- | ------------------------------- | ----------- | ------------------------------------------------------------------------------ |
| gitlab_runner_ci_server_url          | **yes**  | _null_                          | `str`       | GitLab runner CI server URL.                                                   |
| gitlab_runner_registration_token     | **yes**  | _null_                          | `str`       | GitLab runner CI server registration token.                                    |
| gitlab_runner_tags                   | no       | _null_                          | `list[str]` | GitLab runner tags.                                                            |
| gitlab_runner_executor               | no       | `"docker"`                      | `str`       | GitLab runner executor.                                                        |
| gitlab_runner_run_untagged           | no       | `false`                         | `bool`      | Run untagged jobs.                                                             |
| gitlab_runner_limit                  | no       | `{{ ansible_processor_nproc }}` | `int`       | Maximum number of builds processed by the runner. Defaults to number of cores. |
| gitlab_runner_docker_image           | no       | `"ubuntu:latest"`               | `str`       | The default Docker image to run jobs with.                                     |
| gitlab_runner_docker_privileged      | no       | `false`                         | `bool`      | Run job containers in privileged mode.                                         |
| gitlab_runner_docker_runtime         | no       | _null_                          | `str`       | The runtime for Docker containers.                                             |
| gitlab_runner_allow_custom_build_dir | no       | `true`                          | `bool`      | Allow user to define a custom build directory for a job.                       |

## Supported distributions

The roles in this collection are tested on the following, but may also work with other debain based distributions:

- Ubuntu
  - 20.04 LTS (Focal Fossa)
  - 22.04 LTS (Jammy Jellyfish)

## Requirements

- `ansible`
- `passlib`

These can be obtained by running `pip3 install -r requirements.txt` in
the base of the repository.

## License

[GNU General Public License v3.0](./LICENSE)

## Author Information

Marvin Vogt (git@srv6d.space)
