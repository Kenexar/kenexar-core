#!/bin/bash

echo "Check for venv/"

if [ -d "venv/" ]; then
  [[ "$VIRTUAL_ENV" ]] && source "venv/scripts/activate"
else
  eval python3 -m venv venv/
  source "venv/scripts/activate"

  echo "Installing Requirements"
  eval "pip3 install -r req"
fi

echo "Run pylint to create a Difference between versions"
# shellcheck disable=SC2046
eval pylint $(git ls-files '*.py')