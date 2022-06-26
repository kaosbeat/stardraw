import csv_to_sqlite


options=csv_to_sqlite.CsvOptions(typing_style="full",encoding="windows-1250")

csv_to_sqlite.write_csv("Belgium.csv", "Belgium.sqlite", options)

