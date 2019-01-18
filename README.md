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
needed_packages_extra: []
```

Installing needed Python modules:
```
needed_python_modules:
  - docker-py
```

Additional Python modules (it doesn't overwrite the "needed_python_modules" variable):
```
needed_python_modules_extra: []
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
