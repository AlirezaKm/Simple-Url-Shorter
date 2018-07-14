### Installation

Lazy URL Shorter requires python 2 or python 3

Install the dependencies and devDependencies.

```sh
pip install -r requirements.txt
git clone https://gitlab.com/toys-projects/lazy-url-shorter.git
cd lazy-url-shorter
chmod +x ushorter.py
sudo cp ushorter.py /usr/local/bin/ushorter
```

For production environments...

```sh
$ ushorter --help
Usage: ushorter [OPTIONS]

  Lazy Method to Short a URL

Options:
  -u, --url TEXT  Enter Your URL
  --help          Show this message and exit.

```