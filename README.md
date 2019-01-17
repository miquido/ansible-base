# ansible-base

## Synopsis

This role privides basic system configuration.

## Variables

Installing needed system packages:
```
needed_packages:
  - python-pip
  - qemu-guest-agent
```

Additional system packages (it doesn't overwrite the "needed_packages" variable):
```
needed_packages: []
```

Installing needed Python modules:
```
needed_python_modules:
  - docker-py
```

Setting the correct timezone:
```
system_time_zone: Europe/Warsaw
```

## Usage

```
---

- hosts: all
  become: yes
  gather_facts: False
  roles:
    - ansible-base
```
