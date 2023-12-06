# Watermarking Took in Python
A simple watermarking tool that adds a text on the bottom left corner of images.

## Step 1: Ensure Python is Installed
Before creating a virtual environment, you need Python installed on your system. Most modern operating systems have Python installed by default. To check if Python is installed, open a terminal or command prompt and type:


`python --version``

or

`python3 --version``
If Python is installed, this command will return the version number. If not, you'll need to install it from python.org.

Step 2: Install virtualenv (Optional)
While Python (version 3.3 and newer) includes the venv module to create virtual environments, you can also use virtualenv, which is a third-party tool offering some additional functionality. To install virtualenv, run:


`pip install virtualenv`
Step 3: Create a Virtual Environment
Navigate to your project's directory in the terminal or command prompt. Then, create a virtual environment within that directory.

Using venv (built into Python 3):


`python -m venv myenv`
or, if your default Python version is 2.x:


`python3 -m venv myenv``
Using virtualenv:

`virtualenv myenv`
In both commands, myenv is the name of your virtual environment and can be anything you like.

Step 4: Activate the Virtual Environment
To start using the virtual environment, you need to activate it. The activation command differs based on your operating system:

On Windows:

`myenv\Scripts\activate`
On macOS and Linux:

`source myenv/bin/activate`
Once activated, your terminal prompt will usually change to indicate that you're inside the virtual environment.

Step 5: Install Dependencies
With the virtual environment activated, you can install Python libraries using pip, and they will be isolated to this environment. For example:


`pip install requests`
Step 6: Deactivate the Virtual Environment
When you're done working in the virtual environment, you can deactivate it by running:

`deactivate`