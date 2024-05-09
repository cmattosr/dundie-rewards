install:
	@echo "installing for dev environment"
	@.venv/Scripts/python -m pip install -e .[dev]

virtualenv:
	@.venv/Scripts/python -m venv .venv

clean:
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -delete
	@find . -name "*.pyo" -delete
	@find . -name "*.egg-info" -delete
	@find . -name "*.egg" -delete
	@find . -name "*.dist-info" -delete		
	@find . -name "*.so" -delete			
	@find . -name "*.pyd" -delete			
	@find . -name "*.py" -delete
	@find . -name "*.pyc" -delete
	@find . -name "*.pyo" -delete
	@find . -name "*.so" -delete
	@find . -name "*.pyd" -delete