#!/bin/bash

init() {
    echo "Activation of env ..."
    source bin/activate
}

dist() {
    echo "Build the wheel ..."
    python setup.py bdist_wheel
}

deploy() {
    echo "Install the app in the env ..."
    pip install -e .
}


check_exec() {
    if [ $1 != '0' ]; then
        echo "... ko"
        exit $1
    fi;
    echo "... ok"

}

init
check_exec $?
dist
check_exec $?
deploy 
check_exec $?
