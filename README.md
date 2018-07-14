### Installation

Lazy URL Shorter works with python 2

Install dependencies and devDependencies.

```sh

# Clone The Program
git clone https://gitlab.com/toys-projects/lazy-url-shorter.git

# Move to Program Folder
cd lazy-url-shorter

# Install requirements
pip install -r requirements.txt

# Set executable the program
chmod +x ushorter.py

# Copy Program to /usr/local/bin
sudo cp ushorter.py /usr/local/bin/ushorter

# Remove folder
rm -rf lazy-url-shorter/
```
 
 
----
 
 
### Usage: 
 
```sh
$ ushorter --help
Usage: ushorter [OPTIONS]

  Lazy Method to Short a URL

Options:
  -u, --url TEXT  Enter Your URL
  --help          Show this message and exit.

```