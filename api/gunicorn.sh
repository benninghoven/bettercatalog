#!/bin/bash
APP_DIR="/Users/guchiyam/Desktop/CPSC/cpsc-362/github/api"
unicorn --chdir $APP_DIR main:app -w 2 --threads 2 -b 0.0.0.0:8000