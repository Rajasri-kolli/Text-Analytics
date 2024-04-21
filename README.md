
In this project we are trying to download the pdf from the norman police website using the url. The website consists of Public Records of Daily Incident Summary, Daily Case Summary and Daily Arrests Summary. In this project we will take into consideration only INCIDENTS summary.Using text ,This project is done with the use of Python and Linux command line tools.


**Directions and installation**

pipenv install re
pipnev install PyPDF2
pipenv install sqlite3
The above packages need not be installed in the pip environment you are working but should be available to import.

**Project Description**

The main function is written in main.py . Your code should take a url from the command line and perform each operation. After the code is installed, you should be able to run the code using the command below.
pipenv run python project0/main.py --arrests <url>
Using argparse the url given in the command line will be passed to main. All the functions defined in project0.py are imported in main.py.

**Download Data**
fetchincidents() uses the python urllib.request library to grab the pdf from the given url.
data = urllib.request.urlopen(url).read()
The data downloaded from the pdf is saved into a temporary file in any directory. This file should be available to read for the next method.

**Extract Data**
The function extractincidents() takes no parameters and it reads data from the above saved files and extract incidents.
To extract the data from the pdf files, use the PyPdf2.PdfFileReader class. It will allow you to extract pages and pdf file and search for the rows. Extract each row and add it to a list.

## Here is an example python script 

import tempfile
fp = tempfile.TemporaryFile()
 Write the pdf data to a temp file
fp.write(data.read())
 Set the curser of the file back to the begining
fp.seek(0)
 Read the PDF
pdfReader = PdfFileReader(fp)
pdfReader.getNumPages()
 Get the first page
page1 = pdfReader.getPage(0).extractText()
 This function can return a list of rows so another function can easily insert the data into a database. In this prooject we are only considering the first page of any pdf.
Create Database:
The createdb() function creates an SQLite database file named normanpd.db and inserts a table with the schema below.
Insert Data:
The function populatedb(db, incidents) function takes the rows created in the extractincidents() function and adds it to the normanpd.db database. Again, the signature of this function can be changed as needed.
Status Print:
The status() function prints to standard out, a random row from the database. 


## Running the tests
The test files test the different features of the code. This will allow us to test if the code is working as expected. There are several testing frameworks for python, for this project use the py.test framework.


Install the pytest in your current pipfile. You can install it using the command pipenv install pytest. To run test, you can use the command pipenv run python -m pytest. This will run pytest using the installed version of python. Alternatively, you can use the command pipenv run python setup.py test.

Test cases are written for all the five functions. For the purpose of testing a url link is already given and the tests are written based on this url only. The test cases are written for each function.


These files need to be added, commited and then pushed into git. The following code is followed:

git add file-name;
git commit -m "Message to be displayed in git";
git push origin master
