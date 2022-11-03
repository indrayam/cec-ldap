# README

## Assumptions
- You are using Python 3.x
- You have the installed `pycryptodome` by running `pip install pycryptodome`
- You have `ldapsearch` installed. On a Mac, you can run `brew install openldap`
- You have a CEC account
- You have a CSV file `all.csv` with each line listing the first and last name of the user you want to run `ldapsearch` on

## Steps

- Make sure you create a file called `data/.cec` with your CEC password in it
- Open `2_ldapsearch.py` and make sure you enter your CEC Email ID (line 6. Search for `# CHANGEME`)
- Run `python3 1_cec-encrypt.py`: This will encrypt the password and the key used to encrypt it
- Run `python3 2_ldapsearch.py`: This will use the encoded password and key from previous step to run `ldapsearch` on each line of the `all.csv` file


