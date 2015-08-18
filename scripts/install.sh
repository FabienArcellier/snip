#!/bin/bash

SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd );

function main
{
    set -o errexit
    set -o pipefail
    set -o nounset

    mkdir -p /usr/lib/snip

    cp -r ${SCRIPT_DIR}/../src/* /usr/lib/snip/
    chmod 755 "/usr/lib/snip/snip.py"

    if [ -d /etc/bash_completion.d ]
      then
      mv "/usr/lib/snip/snip_bashcompletion.sh" "/etc/bash_completion.d/snip"
      . /etc/bash_completion.d/snip
      else
      rm "/usr/lib/snip/snip_bashcompletion.sh"
    fi


    if [ ! -h "/usr/bin/snip" ]
      then
      ln -s "/usr/lib/snip/snip.py" "/usr/bin/snip"
    fi
}

main "$@"
