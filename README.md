Ansible role ableton.clang
==========================

This role installs the [clang][clang] compiler and associated utilities on the given
Ansible host.

Requirements
------------

Ansible >= 2.10, and a Debian-flavored Linux host.

For macOS, clang should be provided via Xcode. On Windows, clang is available from
[Chocolatey][chocolatey], but this role does not presently support that.

Role Variables
--------------

The following variables influence how `clang` is installed on the host:

- `clang_versions`: A list of clang versions to install. Multiple clang versions can be
  installed on a host side-by-side. However, this role doesn't provide symlinks to the
  binaries, so you must either take care of this in your playbooks, or ensure that your
  application requests a specific clang version during compilation.

See the [`defaults/main.yml`](defaults/main.yml) file for full documentation on required
and optional role variables.

Example Playbook
----------------

```yaml
---
- name: Install clang on hosts
  hosts: "all"
  vars:
    clang_versions:
      - 5.0
      - 6.0
      - 7
      - 11
      - 12

  roles:
    - ableton.clang
```

License
-------

MIT

Maintainers
-----------

This project is maintained by the following GitHub users:

- [@ala-ableton](https://github.com/ala-ableton)
- [@nre-ableton](https://github.com/nre-ableton)


[chocolatey]: https://community.chocolatey.org/packages/llvm
[clang]: https://clang.llvm.org/
