#!/bin/bash
for i in $(seq -f "%04g" 12 100); do
  if [ ! -e output/halos_over_time${i}.png ]; then
    i=$(printf "%g\n" "${i}")
    echo "${i}" 
    mpiexec -n 1 python halos_over_time.py ${i}
  fi
done
