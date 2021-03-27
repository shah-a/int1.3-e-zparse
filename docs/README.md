# INT1.3: E-ZParse

Written in: Python 3.9.2

## Description

E-ZParse provides an automated bookkeeping experience for E-ZPass (toll collection system) customers who need to sort toll transactions by tag/plate number. E-ZParse will parse an invoice PDF for a list of search terms (i.e. tag/plate numbers), accumulate the total amount of transactions, and export the results as a .csv file.

## Getting Started

### Prerequisites

To use/demo this app in a meaningful way, a valid E-ZPass invoice in PDF form is needed.

### Installation

To install and run a local copy of the server:

1) Clone the repository

    `git clone git@github.com:shah-a/int1.3-e-zparse.git`

1) Install the requirements (preferably in a fresh [virtual environment][venv])

    1) `cd 1.3-e-zparse`
    1) `pip3 install -r requirements.txt`

1) Start the server

    `python3 app.py`

### Usage

**To use as a local/development server:**

1) Install and start the server (follow steps in [Installation](#Installation))
1) Navigate to [http://localhost:5000/](http://localhost:5000/)
1) Follow the on-screen instructions to upload an E-ZPass invoice and parse for tags

**To use the live-hosted app:**

1) Navigate to [E-ZParse][E-ZParse]
1) Follow the on-screen instructions to upload an E-ZPass invoice and parse for tags

## Acknowledgements

* [Pythonic Accountant][Pythonic Accountant] for help with regex & PDF parsing
* [Better Dev][Better Dev] for help with frontend design inspiration

[Pythonic Accountant]: https://www.youtube.com/channel/UCQN09g3-sWVRDQc93WRZKYg
[Better Dev]: https://www.youtube.com/channel/UCmXVXfidLZQkppLPaATcHag
[venv]: https://docs.python.org/3/library/venv.html
[E-ZParse]: https://e-zparse.herokuapp.com