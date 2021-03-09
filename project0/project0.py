
import urllib.request
import PyPDF2
import tempfile
import re
import sqlite3

def fetchincidents(url):

   #url = ("https://www.normanok.gov/sites/default/files/documents/"
      # "2021-02/2021-02-21_daily_incident_summary.pdf")

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()                                                                               
    #data = urllib.request.urlopen(url).read()
    fp = tempfile.TemporaryFile()
    fp.write(data)
    return fp

def extractincidents(fp):
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    pages = pdfReader.getNumPages()
    page1 = pdfReader.getPage(0).extractText()
    for i in range(1,pages,1):
        page1 += pdfReader.getPage(i).extractText()
    pagedata = re.sub(' \n', ' ', page1)
    pagedata = re.split(r"\s+(?=\d+/\d+/\d+\s)", pagedata)
    list = []
    for i in pagedata[1:-1]:
        pagedata = i.split('\n')
        if (len(pagedata)>6):
            pagedata.pop()
            pagedata.pop()
        if (len(pagedata)>5):
            pagedata.pop()
        if (len(pagedata)<5):
            pagedata.append('null')
            pagedata[3], pagedata[4] = pagedata[4], pagedata[3]
        list.append(pagedata)

    return list


def createdb():
    dbname = 'normanpd.db'
    database = sqlite3.connect(dbname)
    db = database.cursor()
    db.execute(" DROP TABLE IF EXISTS incidents")
    db.execute(""" CREATE TABLE IF NOT EXISTS incidents
                    (incident_time TEXT,
                    incident_number TEXT,
                    incident_location TEXT,
                    nature TEXT, 
                    incident_ori TEXT);""")
    database.commit()
    database.close()
    return dbname

def populatedb(db, incidents):
    database = sqlite3.connect(db)
    db = database.cursor()
    for i in range(len(incidents)):
        db.execute(" INSERT INTO  incidents VALUES (?,?,?,?,?);", (incidents[i]))
    db.execute("select * from incidents")
    database.commit()
    return 0

def status(db):
    database = sqlite3.connect(db)
    db = database.cursor()
    db.execute("""SELECT nature ||'|'|| count(*) FROM incidents
                  GROUP BY nature """)
    output = db.fetchall()
    for value in output:
        print (value[0])
    return output
