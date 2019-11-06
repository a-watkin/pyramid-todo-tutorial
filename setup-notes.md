setup.py is a python file, which usually tells you that the module/package you are about to install has been packaged and distributed with Distutils, which is the standard for distributing Python Modules.

This allows you to easily install Python packages. Often it's enough to write:

`pip install .`
pip will use setup.py to install your module. Avoid calling setup.py directly.


Install dependencies:

`python setup.py develop`



Above from stackoverflow
https://stackoverflow.com/questions/1471994/what-is-setup-py##targetText=setup.py%20is%20a%20python,%24%20pip%20install%20.