@echo off
rmdir dist /S /Q
pip install --upgrade setuptools wheel twine
python setup.py sdist bdist_wheel
python -m twine upload dist/*
pause
exit