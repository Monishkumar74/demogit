#!/bin/bash

max_retries=2
results_dir="test_results"
mkdir -p "$results_dir"

#collect all tests

tests=$(pytest --collect-only -q )

for test in $tests; do 
    echo "Running $test"
    retries=0

    while [ $retries -le $max_retries ]; do
        pytest "$test"
        status=$?
        if[$status -eq 0]; then
            echo "$test PASSED on attempt $((retries+1))"
            break
        esle
            echo "$test FAILED on attempt $((retries+1))"
            retries=$((retries+1))
            if [ $retries -gt $max_retries ]; then 
                echo "$test FAILED after $max_retries" | tee -a "$results_dir/fail
            fi
        fi
    done   
done