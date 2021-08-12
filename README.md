# AUTOMATED ACCOUNTS RECONCILIATION SOFTWARE

This is a software program that performs Accounts Reconciliation for a Fintech. (The Fintech's name is reserved). Please
note that the data defined in the sample excel files aren't real data.


### Background of Study that birth the writing of this program

The Fintech in mention makes transactions everyday (both credits and debits). Money goes out on one side (debit) and
money comes in on the other (credit). The Fintech needs an in house solution that can reconcile debit and credit
transactions together.

### Problem Definition
Before the invention of this program, the means to reconciling debit transactions to credit transactions was through the
use of Excel formulas and personal review of records by the user which have certain limitations:

- Inputting the formula and cross-checking formula is time-consuming
- Prone to human errors of at least 1-3% either when inputting formula or visually cross-checking.
- Tedious work as making use of Excel would not give a perfect, one-size-fits-all result. The user would still
need to go through each record to filter reconciled and unreconciled records/transactions (provided Excel is even able
  to give sensible/reasonable results in the first place).
- Excel wouldn't give informative result as opposed to a tailored program that would give informative results as to which
records where reconciled and which weren't.
  
### Solution
The solution is to write a tailored program that would automate the process of reconciliation of records/transactions
for the user. 
The program provides a GUI that makes user interaction with it better and easier.
All the user needs to do is to upload both credit and debit transactions (as a csv file) for a time span (say for 24 hours) to the
program through the GUI; and the program handles the rest and OUTPUTS two (2) different files containing reconciled and unreconciled
records/transactions.

### Illustration of how program works and is used
<img src="https://github.com/the-pythonist/Accounts-Reconciliation-Software/blob/main/flow_chart.jpg" />



### IMPORTANT NOTES
This program is SPECIALLY tailored for this particular purpose as the program looks out for specific fields in the raw
data which must have been defined beforehand. 

As a result, this program cannot be used to automate another _Accounts Reconciliation_ problem if the files fed to the program
do not contain certain pre-defined fields.

However, this isn't really a problem as the program can be easily made adaptable to **ANY** Accounts Reconciliation program.
_Furthermore, I can personally help in doing that_

_Even better, I can create a _one-size-fits-all_ program that allows you to define the fields that the program will parse
(via its GUI) before the program runs the reconciliation._ Please not that in this situation, I didn't provide the Fintech with a _one-size-fits-all_
as the Fintech needed some special tailoring with short delivery timeline. Using the _one-size-fits-all_ route would have
taken more time to create.


For you have any questions, enquiries, improvements, or tailoring to the program that you might need,I am only an
_email_ away.
- Email: **gadawesome@gmail.com**
