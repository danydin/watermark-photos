## Step 1: Install virtualenv (Optional)
While Python (version 3.3 and newer) includes the venv module to create virtual environments, you can also use virtualenv, which is a third-party tool offering some additional functionality. To install virtualenv, run:

`pip install virtualenv`

## Step 2: Create a Virtual Environment
Navigate to your project's directory in the terminal or command prompt. Then, create a virtual environment within that directory.

`python3 -m venv myenv`

## Step 3: Activate the Virtual Environment
To start using the virtual environment, you need to activate it. The activation command differs based on your operating system:

On Windows:
`myenv\Scripts\activate`

On macOS and Linux:
`source myenv/bin/activate`

Once activated, your terminal prompt will usually change to indicate that you're inside the virtual environment.

## Step 4: Install Dependencies
With the virtual environment activated, you can install Python libraries using pip, and they will be isolated to this environment. 

`pip install pillow`

## Step 5: Run the python script
`python3 main.py`