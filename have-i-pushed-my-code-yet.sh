#!/bin/bash
test "$(git rev-parse @{u})" = "$(git rev-parse HEAD)" -a "$(git diff --name-only)" = "" || (echo "ERROR: you have not pushed your last commit"; exit 1)