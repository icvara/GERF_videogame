#!/bin/sh
echo -ne '\033c\033]0;GERF_Prototype_test\a'
base_path="$(dirname "$(realpath "$0")")"
"$base_path/Linux_GERF_Prototype_test.x86_64" "$@"
