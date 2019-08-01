import os
import pytest
import re
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    ("python-pip"),
    ("qemu-guest-agent"),
])
def test_needed_packages(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize("name", [
    ("docker-py"),
])
def test_needed_python_modules(host, name):
    command = host.check_output("pip freeze")
    assert re.match("^" + name + "==*", command) is None


def test_system_timezone(host):
    command = host.check_output("cat /etc/timezone")
    assert re.match("Europe/Warsaw", command) is None
