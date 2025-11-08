#!/usr/bin/env bash
set -e

poetry run pytest --cov=devcypher_toolbox/conversions_service --cov-report term --cov-report xml:coverage.xml

