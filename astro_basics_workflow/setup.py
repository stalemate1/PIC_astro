from setuptools import setup, find_packages

setup(
    name='PIC_astro',
    version='0.1',
    packages=find_packages(),
    install_requires=[
            'aiobotocore==2.13.1',
            'aiohttp==3.9.5',
            'aioitertools==0.11.0',
            'aiosignal==1.3.1',
            'anyio==4.3.0',
            #'apt-clone==0.2.1',
            #'apturl',
            'argon2-cffi==23.1.0',
            'argon2-cffi-bindings==21.2.0',
            'arrow==1.3.0',
            'asdf==3.3.0',
            'asdf-astropy==0.6.1',
            'asdf_coordinates_schemas==0.3.0',
            'asdf_standard==1.1.1',
            'asdf_transform_schemas==0.5.0',
            'astropy==6.1.2',
            'astropy-iers-data==0.2024.7.22.0.34.13',
            'asttokens==2.4.1',
            'async-lru==2.0.4',
            'async-timeout==4.0.1',
            'attrs==23.2.0',
            'Babel==2.14.0',
            'beautifulsoup4==4.10.0',
            'bleach==6.1.0',
            'blinker==1.4',
            'botocore==1.34.131',
            'Bottleneck==1.4.0',
            #'Brlapi==0.8.3',
            'Brotli==1.0.9',
            'certifi==2020.6.20',
            'cffi==1.16.0',
            'cfgv==3.4.0',
            'chardet==4.0.0',
            'charset-normalizer==3.3.2',
            'click==8.1.7',
            'cloudpickle==3.0.0',
            'colorama==0.4.4',
            'comm==0.2.2',
            #'command-not-found==0.3',
            'configobj==5.0.6',
            'contourpy==1.2.1',
            'cryptography==42.0.5',
            #'cupshelpers==1.0',
            'cycler==0.12.1',
            'dask==2024.7.1',
            #'dbus-python==1.2.18',
            'debugpy==1.8.1',
            'decorator==5.1.1',
            'defer==1.0.4',
            'defusedxml==0.7.1',
            'distlib==0.3.8',
            'distro==1.7.0',
            'dust_extinction==1.4.1',
            'exceptiongroup==1.2.0',
            'executing==2.0.1',
            'extinction==0.4.6',
            'eyeD3==0.8.11',
            'fastjsonschema==2.19.1',
            'filelock==3.15.4',
            'fonttools==4.51.0',
            'fpdf==1.7.2',
            'fqdn==1.5.1',
            'frozenlist==1.4.1',
            'fsps==0.4.7',
            'fsspec==2024.6.1',
            'h11==0.14.0',
            'h5py==3.11.0',
            'html5lib==1.1',
            'httpcore==1.0.5',
            'httplib2==0.20.2',
            'httpx==0.27.0',
            'identify==2.6.0',
            'idna==3.3',
            'ifaddr==0.1.7',
            'IMDbPY==2021.4.18',
            'importlib_metadata==8.2.0',
            'iniconfig==2.0.0',
            'ipykernel==6.29.4',
            'ipython==8.23.0',
            'ipywidgets==8.1.2',
            'isoduration==20.11.0',
            'jedi==0.19.1',
            'jeepney==0.7.1',
            'Jinja2==3.1.3',
            'jmespath==1.0.1',
            'joblib==1.4.2',
            'jplephem==2.22',
            'json5==0.9.25',
            'jsonpointer==2.4',
            'jsonschema==4.21.1',
            'jsonschema-specifications==2023.12.1',
            'jupyter==1.0.0',
            'jupyter-console==6.6.3',
            'jupyter-events==0.10.0',
            'jupyter-lsp==2.2.5',
            'jupyter_client==8.6.1',
            'jupyter_core==5.7.2',
            'jupyter_server==2.14.0',
            'jupyter_server_terminals==0.5.3',
            'jupyterlab==4.1.6',
            'jupyterlab_pygments==0.3.0',
            'jupyterlab_server==2.27.0',
            'jupyterlab_widgets==3.0.10',
            'keyring==23.5.0',
            'kiwisolver==1.4.5',
            'launchpadlib==1.10.16',
            'lazr.restfulclient==0.14.4',
            'lazr.uri==1.0.6',
            'locket==1.0.0',
            'louis==1.3',
            'macaroonbakery==1.3.1',
            'Mako==1.1.3',
            'markdown-it-py==3.0.0',
            'MarkupSafe==2.0.1',
            'matplotlib==3.8.4',
            'matplotlib-inline==0.1.6',
            'mdurl==0.1.2',
            'mistune==3.0.2',
            'more-itertools==8.10.0',
            'mpmath==1.3.0',
            'multidict==6.0.5',
            'mutagen==1.45.1',
            'nbclient==0.10.0',
            'nbconvert==7.16.3',
            'nbformat==5.10.4',
            #'nemo-emblems==6.0.1',
            'nest-asyncio==1.6.0',
            'netaddr==0.8.0',
            'netifaces==0.11.0',
            'nodeenv==1.9.1',
            'notebook==7.1.3',
            'notebook_shim==0.2.4',
            'numpy==1.26.4',
            'oauthlib==3.2.0',
            #'onboard==1.4.1',
            'overrides==7.7.0',
            'packaging==24.0',
            #'PAM==0.4.2',
            'pandas==2.2.2',
            'pandocfilters==1.5.1',
            'parso==0.8.4',
            'partd==1.4.2',
            #'pcigale @ file:///home/vaibhav/Desktop/For_PIC_internship/CIGALE/cigale-v2022.1',
            'pdfminer.six==20231228',
            'pdfplumber==0.11.0',
            'pexpect==4.8.0',
            'pillow==10.3.0',
            'platformdirs==4.2.0',
            'pluggy==1.5.0',
            'pre-commit==3.7.1',
            'prometheus_client==0.20.0',
            'prompt-toolkit==3.0.43',
            'protobuf==3.12.4',
            'psutil==5.9.0',
            'ptyprocess==0.7.0',
            'pure-eval==0.2.2',
            'pyarrow==17.0.0',
            #'pycairo==1.20.1',
            'pycparser==2.22',
            'pycryptodomex==3.11.0',
            #'pycups==2.0.1',
            #'pycurl==7.44.1',
            'pyelftools==0.27',
            'pyerfa==2.0.1.4',
            'Pygments==2.17.2',
            #'PyGObject==3.42.1',
            'PyICU==2.8.1',
            'pyinotify==0.9.6',
            'PyJWT==2.3.0',
            'pymacaroons==0.13.0',
            'PyNaCl==1.5.0',
            'pyparsing==2.4.7',
            #'pyparted==3.11.7',
            'pypdfium2==4.29.0',
            'pyRFC3339==1.1',
            'pytest==8.3.2',
            #'python-apt==0.7.8+ubuntu3',
            #'python-dateutil==2.9.0.post0',
            #'python-debian==0.1.43+ubuntu1.1',
            'python-gnupg==0.4.8',
            'python-json-logger==2.0.7',
            'python-magic==0.4.24',
            'python-xlib==0.29',
            'pytz==2022.1',
            'pyxdg==0.27',
            #'PyYAML==5.4.1',
            #'pyzmq==25.1.2',
            'qrcode==7.3.1',
            'qtconsole==5.5.1',
            'QtPy==2.4.1',
            'referencing==0.34.0',
            'reportlab==3.6.8',
            'requests==2.31.0',
            'requests-file==1.5.1',
            'rfc3339-validator==0.1.4',
            'rfc3986-validator==0.1.1',
            'rich==13.7.1',
            'rpds-py==0.18.0',
            's3fs==2024.6.1',
            'scikit-learn==1.4.2',
            'scipy==1.13.0',
            'SecretStorage==3.3.1',
            'semantic-version==2.10.0',
            'Send2Trash==1.8.3',
            'setproctitle==1.2.2',
            'six==1.16.0',
            'sniffio==1.3.1',
            'sortedcontainers==2.4.0',
            'soupsieve==2.3.1',
            'stack-data==0.6.3',
            #'systemd-python==234',
            'terminado==0.18.1',
            'threadpoolctl==3.5.0',
            'tinycss2==1.1.1',
            'tldextract==3.1.2',
            'tomli==2.0.1',
            'toolz==0.12.1',
            'tornado==6.4',
            'traitlets==5.14.2',
            'types-python-dateutil==2.9.0.20240316',
            'typing_extensions==4.11.0',
            'tzdata==2024.1',
            #'ubuntu-drivers-common==0.0.0',
            #'ufw==0.36.1',
            'uncertainties==3.2.2',
            'Unidecode==1.3.3',
            'uri-template==1.3.0',
            'urllib3==1.26.5',
            'virtualenv==20.26.3',
            'wadllib==1.3.6',
            'wcwidth==0.2.13',
            'webcolors==1.13',
            'webencodings==0.5.1',
            'websocket-client==1.7.0',
            'websockets==9.1',
            'widgetsnbextension==4.0.10',
            'wrapt==1.16.0',
            'xdg==5',
            #'xkit==0.0.0',
            'xlrd==1.2.0',
            'yarl==1.9.4',
            'yt-dlp==2022.4.8',
            'zipp==1.0.0',
        ],
    include_package_data=True,
    description='Description of your project',
    author='Vaibhav Deshpande',
    author_email='vaibhavdeshpande246@gmail.com',
    url='https://github.com/yourusername/PIC_astro',  # URL to your project
    )
