#!/bin/sh

echo "-> Starting $APP_NAME"
echo "Entry point args: ${*:-<none>}"
echo ""


start () {
    "start_$STAGE"
}

start_development () {
  echo "Starting in development"
  export FLASK_ENV=development
  python api.py
}

start_production () {
    echo "Starting in production"
}

start_staging() {
    echo "Starting in staging"
}

start_shell () {
    echo "Starting to shell"
    bash
}

COMMAND=$1; shift
STAGE=$1;

case $COMMAND in
    start)
        start $*
    ;;
    *)
        echo "[!] Invalid or no command specified. Available commands: start, shell"
        exit 1
    ;;
esac

exit $?