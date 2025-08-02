#!/usr/bin/env bash

echo "Run apply migration..."
alembic upgrade head
echo "Migration applied"

exec "$@"