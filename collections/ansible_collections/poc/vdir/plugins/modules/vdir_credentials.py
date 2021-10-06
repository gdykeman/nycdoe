#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Henrik Wallström <henrik@wallstroms.nu>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r'''
---
module: configure vdir credentials
short_description: configure vdir credentials
description:
     - Configure virtual directory physical path credentials
options:
  name:
    description:
      - The name of the virtual directory
    type: str
    required: yes
  site:
    description:
      - The site name under which the virtual directory exists.
    type: str
    required: yes
  username:
    description:
      - The username for the virtual directory physical path credential
  password:
    description:
      - The password for the virtual directory physical path credential
    type: str
'''

EXAMPLES = r'''
- name: Configure virtual directory physical path credentials
  poc.iis.vdir_credentials:
    name: alpha_vdir
    site: "Default Web Site"
    username: alphauser
    password: alphapassword

'''
