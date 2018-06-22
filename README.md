# README

Here are the python scripts I used to fetch all my solutions on [Codechef]
and store them locally with a well-structured manner.

[Codechef]: https://www.codechef.com/

## Setup

You can either clone the repository with 
`https://github.com/bansal1232/Codechef-Crawler.git`, or download
all the scripts and put them in the same directory.


Scripts are written in python3 syntax. If you don't have a python3
interpreter and want to use the scripts, you can either:
1. Download python 3.6
    * For debian distros, you may want to take a look at [here][linux_link]
    * For macintosh machines, [macpython][macos_link] 
    * For windows, refer to [using python on windows][windows_link] 
2. Modify the source code so that it works with the version you have
installed.
    * If you have a python2x interpreter, then I suggest you to switch over python3 interpreter.

[linux_link]: https://askubuntu.com/a/865569/595315
[macos_link]: https://docs.python.org/3/using/mac.html
[windows_link]: https://docs.python.org/3/using/windows.html

## Requirements

Before running any of above script, you must be assure that you have installed all python packages in default python directory. You can easily install all requirements by just using the following command-

`$ pip install -r requirements.txt`

## How to Use

Open `conf.py`. Assign your codechef **handle** and your **password** to `handle` and `pass_val` variables respectively. If you want to download other handle's solutions, then you don't need to assign anything in `pass_val` variable.

Now you can run the script `crawl.py`, and then wait until all problems are downloaded.

**Please push any changes or bug if you found while executing this script.**
