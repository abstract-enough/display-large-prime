#!/bin/bash


enable_lmod
module load container_env python3

crun python -u display_largest_prime.py
