#!/bin/bash

comm -12 <(python check_phoebus.py widget "$1" | sort) <(python check_phoebus.py widget "$2" | sort)
