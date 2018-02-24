#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A vue_ema.taskapp beat -l INFO
