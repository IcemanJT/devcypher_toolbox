#!/usr/bin/env bash
set -e

poetry run pytest \
  --cov=conversions_service \
  --cov-report=xml:coverage.xml \
  --cov-report=html:htmlcov \
  tests