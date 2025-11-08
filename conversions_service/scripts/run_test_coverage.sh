#!/usr/bin/env bash
set -e
chmod +x conversions_service/scripts/run_test_coverage.sh

poetry run pytest \
  --cov=devcypher_toolbox/conversions_service \
  --cov-report term \
  --cov-report xml:coverage.xml
