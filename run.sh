#!/usr/bin/env bash

gunicorn server:app --bind 127.0.0.1:5010
