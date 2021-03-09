
# Example main.py
import argparse
import project0
#from project0 import project0


def main(url):
    # Download data
    incident_data = project0.fetchincidents(url)

    # Extract Data
    incidents = project0.extractincidents(incident_data)

    # Create Database
    db = project0.createdb()

    # Insert Data
    project0.populatedb(db, incidents)

    # Print Status
    project0.status(db)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True,
                        help="The incidents summary url.")

    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
