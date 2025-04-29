# Capture all goals (targets) provided to make
ARGS := $(filter-out $@,$(MAKECMDGOALS))

setup:
	@echo "Installing python dependencies"
	pip install -r requirements.txt

run:
	@echo "Running main with arguments: $(ARGS)"
	python3 src/main.py $(ARGS)

# Prevent make from treating arguments as targets
%:
	@:
