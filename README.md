# ansible-base

[![Build Status](https://www.travis-ci.org/miquido/ansible-base.svg?branch=master)](https://www.travis-ci.org/miquido/ansible-base) 
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Twitter URL](https://img.shields.io/twitter/follow/miquido.svg?style=social&label=Follow%20%40Miquido)](https://twitter.com/miquido)

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

## Test the role

Use your shell and put
```
molecule test
```

You have to also install needed Python module:
```
pip install docker-py
```
