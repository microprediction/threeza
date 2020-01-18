cd /Users/pcotton/github/threeza
rm /Users/pcotton/github/threeza/dist/*
python setup.py sdist bdist_wheel
twine upload dist/*
