"""Molecule tests for the default scenario."""

import os

import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("version", ["5.0", "6.0", "7", "11", "12"])
def test_clang_versions_installed(host, version):
    """Test that expected clang versions were installed."""
    clang_link_file = host.file(f"/usr/bin/clang-{version}")
    assert clang_link_file.is_symlink
    clang_bin_file = host.file(clang_link_file.linked_to)
    assert clang_bin_file.mode == 0o0755
