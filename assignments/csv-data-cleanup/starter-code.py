import csv


def load_data(filename):
    """Open a CSV file and return the rows as a list of dictionaries."""
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)


def clean_row(row):
    """Clean one row of data before analysis."""
    cleaned = {}
    for key, value in row.items():
        if value is None:
            cleaned[key] = ""
        else:
            cleaned[key] = value.strip()

    # Convert numeric values here if needed
    return cleaned


def write_cleaned_data(rows, filename):
    """Write cleaned rows to a new CSV file."""
    fieldnames = rows[0].keys() if rows else []

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def make_summary(rows):
    """Return a short dictionary with summary statistics."""
    if not rows:
        return {
            "average_score": 0,
            "highest_score": 0,
            "lowest_score": 0,
            "total_students": 0,
        }

    scores = []
    for row in rows:
        if row.get('score'):
            scores.append(int(row['score']))

    return {
        "average_score": round(sum(scores) / len(scores), 2) if scores else 0,
        "highest_score": max(scores) if scores else 0,
        "lowest_score": min(scores) if scores else 0,
        "total_students": len(rows),
    }


def main():
    rows = load_data('data.csv')
    cleaned_rows = [clean_row(row) for row in rows]

    # TODO: Fix blank values and convert numeric data correctly
    # TODO: Save cleaned data to 'cleaned_data.csv'
    # TODO: Print a summary report

    write_cleaned_data(cleaned_rows, 'cleaned_data.csv')
    print(make_summary(cleaned_rows))


if __name__ == "__main__":
    main()
