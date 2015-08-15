#!/bin/bash

SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd );

function main
{
    set -o errexit
    set -o pipefail
    set -o nounset

    chmod 755 "${SCRIPT_DIR}/../snip.py"
    ln -s "${SCRIPT_DIR}/../snip.py" "/usr/bin/snip"
}

main "$@"
