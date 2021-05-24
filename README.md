# Amibroker Machine Learning Demo

This repository demonstrate how to run any machine learning model on top of Amibroker AFL. This can be made possible by using [pywin32](https://github.com/mhammond/pywin32) to register Python code to [Python COM server](http://timgolden.me.uk/pywin32-docs/html/com/win32com/HTML/QuickStartServerCom.html) and use it as [Amibroker Object](https://www.amibroker.com/guide/afl/createobject.html)

Our machine learning model is used to classify certain price action by using 30 days period OHLC data from Amibroker.

Method of connecting Amibroker with python is Heavily inspired by this [thread](https://forum.amibroker.com/t/is-it-possible-to-run-python-on-amibroker/1809)

# Tutorial

- Install same architrecture of Python (X86 or X64) as your Amibroker's architeccture
- `pip install -r requirements.txt`
- finish installation of pywin32 by running command `python Scripts/pywin32_postinstall.py -install` in your python Scripts directory
- Open new terminal as administrator and run `python server.py` to register COM server
- Run `demo.afl` on Amibroker

# Debugging

- `python server.py --debug`
- Open PythonWin (Automatically installed by pywin32)
- `Tools -> Trace Collector Debugging Tool`

# Known Constraint

- Python version used in this demo is 3.8.10 32 bit and is not tested on 64 bit version yet.
- Pleas note that model provided in this repository is dummy one. We do not and will not publish currently used our model. Please train one yourself.
- We have not tested the concept with more advanced model from [Tensorflow](https://www.tensorflow.org/), [Keras](https://keras.io/), and [Pytorch](https://pytorch.org/) yet, but it should work with slight modification.
- Not tested with [Virtual environment](https://docs.python.org/3/library/venv.html), [Anaconda](anaconda), or [Docker](https://hub.docker.com/_/python) yet.
