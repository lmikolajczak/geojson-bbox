# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP----------------------"
	@echo "To install the project type make install"
	@echo "To lint the project type make lint"
	@echo "To test the project type make test"
	@echo "-----------------------------------------"

# This generates the desired project file structure
install:
	@echo "Installing current project in editable mode..."
	poetry install

# This function uses flake8 to lint our source files
lint:
	@echo "Linting code..."
	flake8 . --count --show-source --statistics
	
# This function uses pytest to test our code
test:
	@echo "Tests are not implemented yet..."
