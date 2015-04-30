#!/bin/bash
COUNTER=12
  while [  $COUNTER -lt 101 ]; do
    echo "Executing iteration ${COUNTER}..."
    mpiexec -n 8 python halos_over_time.py $COUNTER
    let COUNTER=COUNTER+8
  done
