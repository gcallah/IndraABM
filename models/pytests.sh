#!/bin/bash

export user_type="test"
export test_dir="tests"
export ignores="(bigbox)"

if [ -z "$1" ]; then
  export capture=""
else
  export capture="--nocapture"
fi

nosetests --ignore-files=$ignores --exe --verbose --with-coverage --cover-package=models $capture
