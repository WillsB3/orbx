#!/usr/bin/env bash

HOST=0.0.0.0
PORT=8080
TMP_DIR=tmp

if [ ! -d "$TMP_DIR" ] ; then
    echo "Missing data directory: $TMP_DIR .. creating now";
    mkdir $TMP_DIR
fi

if [ `command -v rlwrap` ]; then
    CMD="rlwrap dev_appserver.py"
else
    CMD=dev_appserver.py
fi

$CMD app.yaml \
    --log_level=info \
    --skip_sdk_update_check \
    --datastore_path=tmp/data \
    --blobstore_path=tmp/blobstore \
    --smtp_port=1025 \
    --smtp_host=localhost \
    --host=$HOST \
    --port=$PORT \
    --require_indexes=1 \
    $@
