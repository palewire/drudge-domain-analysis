Drudge domain analysis
======================

A simple example of using storytracker and the PastPages API to conduct a link analysis

Getting started
---------------

Create a virtualenv and activate it.

```bash
$ virtualenv drudge-domain-analysis
$ cd drudge-domain-analysis
$ . bin/activate
```

Clone the repository and jump into it.

```bash
$ git clone https://github.com/pastpages/drudge-domain-analysis.git repo
$ cd repo
```

Install the requirements.

```bash
$ pip install -r requirements.txt
```

Running the analysis
--------------------

Download the archived screenshots from PastPages.

```bash
$ python download.py
```

Extract the hyperlinks from each one.

```bash
$ python extract.py
```

Analyze the hyperlinks and spit out the results.

```bash
$ python analyze.py
```
