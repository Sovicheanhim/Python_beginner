def tsv_to_json(tsv_file, json_file):
    try:
        import json, csv
        data = {}
        with open(tsv_file, "r") as tsv_fi:
            tsv_fi_reader = csv.DictReader(tsv_fi, delimiter='\t')
            data = list(tsv_fi_reader)
        with open(json_file, "w") as json_fi:
            json_fi.write(json.dumps(data, indent =4))
        return 1
    except FileNotFoundError:
        return 0


# print(tsv_to_json("bc_tsv.txt", "hello.txt"))