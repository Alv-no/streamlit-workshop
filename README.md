# Streamlit-workshop

Materials for the Streamlit Workshop on February 5th, as part of the monthly workshops hosted by D&A in Alv.

The current workshop is hosted by Øyvind and Fridtjof.

# Application Setup Instructions

## How to setup the application

1. Clone the repository:

    ```
    git clone https://github.com/Alv-no/streamlit-workshop.git 
    ```

2. Change directory to `streamlit-workshop`:

    ```
    cd streamlit-workshop
    ```

3. Create a virtual environment using Python 3.11:

    ```
    python3.11 -m venv venv
    ```

4. Activate the virtual environment:

Different shells and operating systems require different commands to activate a Python virtual environment. Here's a table with commands for some of the most common environments:

| Environment    | Activation Command                 |
|----------------|------------------------------------|
| Bash/Zsh (Linux, macOS) | `source venv/bin/activate`        |
| Fish Shell     | `source venv/bin/activate.fish`    |
| csh/tcsh       | `source venv/bin/activate.csh`     |
| PowerShell (Windows) | `venv\Scripts\Activate.ps1`         |
| Command Prompt (Windows) | `venv\Scripts\activate.bat`       |
| PowerShell (Linux, macOS) | `venv/bin/Activate.ps1`           |

Please make sure to replace `venv` with the name of your virtual environment directory if it's different.

5. Install `pip-tools`:

    ```
    pip install pip-tools
    ```

6. Synchronize the dependencies:

    ```
    pip-sync
    ```

## How to run the application

Run the Streamlit application:

```
streamlit run Home.py
```
