run:
	@echo "Enter venv test with:\n\t source test/bin/activate"
	@echo "Deactivate with:\n\t deactivate"

setup:
	python3 -m venv test
	@echo Finished. The new python enviroment is called <test>.