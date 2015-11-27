#!/bin/bash

PATH=$PATH:$HOME/.local/bin

function virtualenv_prompt() {
    if [ -n "$VIRTUAL_ENV" ]; then
        echo "(${VIRTUAL_ENV##*/}) "
    fi
}

export PS1='$(virtualenv_prompt)\u@\H $ '

eval "$(vex --shell-config bash)"
