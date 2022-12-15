import pytest


def test_gitlab_runner_package(host):
    """The GitLab runner package is installed."""
    gitlab_runner_package = host.package("gitlab-runner")

    assert gitlab_runner_package.is_installed


@pytest.mark.parametrize(
    "command", ("gitlab-runner status", "gitlab-runner health-check")
)
def test_gitlab_runner_health(host, command):
    """GitLab runner is healthy."""
    host.run_test(command)
