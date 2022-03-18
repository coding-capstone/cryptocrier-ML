# Getting started (dev)
1. (Optional) Download VSCode and use their wonderful Python extension!
1. Ensure you have yarn installed
1. Run `yarn install`
1. Run the `yarn setup-venv` script
1. Activate your virtual environment
    1. Mac: `source ./venv/bin/activate`
    1. Windows: `.\venv\bin\activate.ps1`
1. Run the `yarn install-requirements` script

# About the virtual environment
The virtual environment allows you to download project-specific project libraries, similar to how we're using our package.json in our Next repo to manage project-specific npm packages. The advantage to using a virtual environment is that it allows you to easily modularise and share your python configurations (which we've chosen to put into `requirements.txt`).
