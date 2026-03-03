#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-dev.txt
uvicorn services.api.app.main:app --reload
