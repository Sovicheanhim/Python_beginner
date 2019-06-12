def json_to_tsv(json_file, tsv_file):
    try:
        import json, csv
        json_fi = open(json_file, "r")
        json_data = json.load(json_fi)
        json_fi.close()

        tsv_fi = open(tsv_file, "w", newline = "")
        tsv_writer = csv.writer(tsv_fi, delimiter = '\t')
        tsv_writer.writerow(json_data[0].keys())
        for row in json_data:
            tsv_writer.writerow(row.values())
        tsv_fi.close()
        return 1
    except FileNotFoundError:
        return 0


# print(json_to_tsv("test_json.json", "hello.tsv"))