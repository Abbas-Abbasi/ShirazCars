import csv
import os

def extract_unique_links():
    # Load existing enrolled links from alreadyEnrolled.csv
    existing_enrolled_links = set()
    if os.path.exists('alreadyEnrolled.csv'):
        with open('alreadyEnrolled.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            existing_enrolled_links.update(row[0] for row in reader)

    # Load new links from new_courses_links.csv
    new_links = set()
    if os.path.exists('new_courses_links.csv'):
        with open('new_courses_links.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            new_links.update(row[0] for row in reader)

    # Extract unique links by removing the links that are already enrolled
    unique_links = new_links - existing_enrolled_links

    # Save the unique links to courses_links.csv
    with open('courses_links.csv', 'w', newline='', encoding='UTF8') as csvfile:
        writer = csv.writer(csvfile)
        for link in unique_links:
            writer.writerow([link])

if __name__ == "__main__":
    extract_unique_links()
