import argparse
import project0
from project0 import project0
import sqlite3
import pytest

url = "https://www.normanok.gov/sites/default/files/documents/2021-02/2021-02-02_daily_incident_summary.pdf"


def test_fetchincidents():
      assert project0.fetchincidents(url) is not None


def test_extractincidents():
      temp_file = project0.fetchincidents(url)
      result = project0.extractincidents(temp_file)
      for i in result:
            assert len(i) > 1

def test_createdb():
      assert project0.createdb() == 'normanpd.db'


def test_populatedb( ):
      temp_file = project0.fetchincidents(url)
      incidents = project0.extractincidents(temp_file)
      db = project0.createdb()
      project0.populatedb(db, incidents)
      database = sqlite3.connect(db)
      db = database.cursor()
      db.execute('select * from incidents;' )
      result = db.fetchall()
      for i in result:
         assert len(i) == 5


def test_status( ):
      temp_file = project0.fetchincidents(url)
      incidents = project0.extractincidents(temp_file)
      db = project0.createdb()
      project0.populatedb(db, incidents)
      result = project0.status(db)
      for i in result:
         assert len(i) > 0
