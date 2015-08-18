#/bin/bash -x
 
function _snip_complete_()
{
    local cmd="${1##*/}"
    local word=${COMP_WORDS[COMP_CWORD]}
    local line=${COMP_LINE}
    local xpat='!*'

    COMPREPLY=( $(compgen -W "$(snip list)" -- "${word}" ))
}
 
complete -F _snip_complete_ snip