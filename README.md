# robo-advisor


## Requirements

  + Python 3.7+
  + Anaconda 3.7+
  + GitHub and GitHub Desktop
  + Pip
  + VSCode or similar software (editors will be referred to simply as 'VSCode')
  + GitBash or another command line software (will simply be referred to as GitBash or the command line)

## Program Overview

This program allows you to enter a stock ticker symbol, and will recommend whether or not the user should invest based on the program's algorithm.

## Setup

Using this online Github repository, click "Fork" to copy this program's repository into your personal Github. Using GitHub Desktop, clone this version onto your desktop. 

Use the command-line to navigate into the local repository.
```sh
cd ~/Desktop/robo_advisor
```

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

```sh
conda create -n stocks-env python=3.8 # (first time only)
conda activate stocks-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```
---

Install Pandas and Seaborn from the command line if you haven't already:

```sh
pip install pandas
pip install seaborn
```
---

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify the following variables:
```sh
ALPHAVANTAGE_API_KEY="abc123" #change the contents of the API key to match your own API key
```
If you don't have an API key yet, go to the following website and follow the instructions:
https://www.alphavantage.co/support/#api-key


If you haven't already, make sure to install the requests package :
```sh
pip install requests
```

## Program Instructions 

Once you have completed the setup section above, you are ready to use the program. 

Make sure that you are still in the directory in the command line. You can then access the program by typing the following into your command line:

```sh
python app/robo_advisor.py
```

The following message should be displayed:
```
Please input your desired stock:

```

From there, please input your desired stock symbol and press enter. 

NOTE: If you enter something that does not resemble a stock symbol (such as numbers or a string longer than 5 characters), the program will ask you to input something else. IF you enter something that could potentially look like a stock symbol but that doesn't exists (such as a random string of 4 characters that don't correspond to a real stock), the problem will quit, and you will have to restart it to try again.

