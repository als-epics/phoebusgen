#!/bin/bash

comm -12 <(python check_phoebus.py "$1" | sort) <(python check_phoebus.py "$2" | sort)
