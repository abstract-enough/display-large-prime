#!/bin/bash


enable_lmod
module load container_env python3

crun python -u prime_html.py
