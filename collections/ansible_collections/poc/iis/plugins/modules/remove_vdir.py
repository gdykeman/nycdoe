#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Henrik Wallström <henrik@wallstroms.nu>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r'''
---
module: remove_vdir
short_description: deletes a virtual directory
description:
     - Removes a virtual directory in IIS.
options:
  name:
    description:
      - The name of the virtual directory to remove
    type: str
    required: yes
  site:
    description:
      - The site name under which the virtual directory exists.
    type: str
    required: yes
  application:
    description:
      - The application under which the virtual directory bound to.
    type: str
'''

EXAMPLES = r'''
- name: Remove a virtual directory if it exists
  poc.iis.remove_vidr:
    name: somedirectory
    site: somesite

'''
