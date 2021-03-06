# FilterReportIPsByCount
Script to read through a report containing IP addresses that are potentially malicious and require blacklisting, check if those IPs appear in the report a number of times (count), and check if those IPs have been blacklisted. Outputs list of IPs and the IPs' analysis to standard out or in a chosen file.

## How to Use
[Make sure that you have Python installed on your computer, and that it is updated to at least version 3.6 ](https://www.python.org/downloads/)

### Method 1: Install with pip from PyPi
    
1.  In the command line, navigate to the repository and enter the below command (Only required with first use)
    * `python -m pip install FilterReportIPsByCount`
	
3.  Enter the below command with the following arguments:
    * `python FilterReportIPsByCount -i "<input filename>" -o "<output filename>" -c <count>`
    > **-i [input filename]** : REQUIRED, the filename (with path, if not on the same directory) of the excel file you want to analyze
    >
    > **-o [output filename]** : Optional, the filename of the text file to which you would like to print the IP analysis information; if not specified, will output to stdout
    >
    > **-c [count]** : Optional, number of times an IP should appear in the report to be added to the list of IPs to analyze; if not specified, will default to 5
    >
    > **-h** : Shows the arguments and options required 
	> **Make sure you do not include the arrow brackets (<>) when entering the commands**
	
##### Example Commands
* With input filename and **no output filename** and **no count**
	`python -m FilterReportIPsByCount -i "BotReport.xls"`
	
* With input filename and output filename and **no count**
	`python -m FilterReportIPsByCount -i "BotReport.xls -o "ListOfIPs.txt"`

* With input filename and output filename and count
	`python -m FilterReportIPsByCount -i "BotReport.xls" -c 2`
	
### Method 2: No installation
1.  Download the zip file or clone the repository
3.  In the command line, navigate to the repository and enter the below command (Only required with first use)
    * `pip install -r requirements.txt`
3.  Enter the below command with the following arguments:
    * `python FilterReportIPsByCount\FilterReportIPsByCount.py -i <input filename> -o <output filename> -c <count>`
    > **-i [input filename]** : REQUIRED, the filename (with path, if not on the same directory) of the excel file you want to analyze
    >
    > **-o [output filename]** : Optional, the filename of the text file to which you would like to print the IP analysis information; if not specified, will output to stdout
    >
    > **-c [count]** : Optional, number of times an IP should appear in the report to be added to the list of IPs to analyze; if not specified, will default to 5
    >
    > **-h** : Shows the arguments and options required 
	> **Make sure you do not include the arrow brackets (<>) when entering the commands**
	
##### Example Commands
* With input filename and **no output filename** and **no count**
	`python -m FilterReportIPsByCount\FilterReportIPsByCount.py -i "BotReport.xls"`
	
* With input filename and output filename and **no count**
	`python -m FilterReportIPsByCount\FilterReportIPsByCount.py -i "BotReport.xls -o "ListOfIPs.txt"`

* With input filename and output filename and count
	`python -m FilterReportIPsByCount\FilterReportIPsByCount.py -i "BotReport.xls" -c 2`
	
### Method 3: Install with git 
1.	In the command line, install the repository by entering the below command (only required the first time)
	* `python -m pip install git+https://github.com/divyaaveerama/FilterReportIPsByCount.git#egg=FilterReportIPsByCount`
2.  Once installed, Enter the below command with the following arguments:
    * `python FilterReportIPsByCount -i "<input filename>" -o "<output filename>" -c <count>`
    > **-i [input filename]** : REQUIRED, the filename (with path, if not on the same directory) of the excel file you want to analyze
    >
    > **-o [output filename]** : Optional, the filename of the text file to which you would like to print the IP analysis information; if not specified, will output to stdout
    >
    > **-c [count]** : Optional, number of times an IP should appear in the report to be added to the list of IPs to analyze; if not specified, will default to 5
    >
    > **-h** : Shows the arguments and options required 
	> **Make sure you do not include the arrow brackets (<>) when entering the commands**
	
##### Example Commands
* With input filename and **no output filename** and **no count**
	`python -m FilterReportIPsByCount -i "BotReport.xls"`
	
* With input filename and output filename and **no count**
	`python -m FilterReportIPsByCount -i "BotReport.xls -o "ListOfIPs.txt"`

* With input filename and output filename and count
	`python -m FilterReportIPsByCount -i "BotReport.xls" -c 2`	
