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
    command = host.check_output("timedatectl status | grep 'Time zone'")

    assert re.match("Europe/Warsaw", command) is None


@pytest.mark.parametrize('service', [
  'node_exporter'
])
def test_node_exporter_service(host, service):
  service_name = host.service_name(service)

  assert service_name.is_running

  assert service_name.is_enabled
