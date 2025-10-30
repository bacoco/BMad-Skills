.PHONY: install test test-unit lint validate dev clean help

help:
	@echo "BMAD Skills - Development Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install        Install all dependencies (Python + Node)"
	@echo "  make dev            Setup development environment"
	@echo ""
	@echo "Testing:"
	@echo "  make test           Run unit and integration tests"
	@echo "  make test-unit      Run unit tests only"
	@echo ""
	@echo "Quality:"
	@echo "  make lint           Run contract linter"
	@echo "  make validate       Validate all skills"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean          Remove temporary files and caches"

install:
	@echo "Installing Python dependencies..."
	pip3 install -r requirements.txt
	@echo "Installing Node dependencies..."
	npm install
	@echo "✅ All dependencies installed"

dev: install
	@echo "✅ Development environment ready"
	@echo ""
	@echo "Quick commands:"
	@echo "  make test          - Run tests"
	@echo "  make lint          - Lint skills"
	@echo "  make validate      - Validate skills"

test: install
	@echo "Running unit and integration tests..."
	npm test

test-unit: install
	@echo "Running unit tests only..."
	npm run test:unit

lint: install
	@echo "Linting skill contracts..."
	npm run lint

validate: install
	@echo "Validating all skills..."
	python3 .claude/skills/core-skill-creation/scripts/quick_validate.py .claude/skills/

clean:
	@echo "Cleaning temporary files..."
	rm -rf __pycache__ .pytest_cache htmlcov .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete"
