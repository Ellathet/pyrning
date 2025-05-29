.PHONY: install dev

help:
	@echo "Available commands:"
	@echo "  install     - Install dependencies using uv"
	@echo "  dev         - Run development server with hot reload"

install:
	uv sync

dev:
	uv run fastapi dev app/main.py --host 0.0.0.0 --port 8000