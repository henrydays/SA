import publico.search as publico
import csv
import expresso.search as expresso
import pandas as pd
from datetime import date


def write_to_csv(file_name, results):
    with open("./outputs/"+file_name, 'w', newline='', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='|',
                                quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for hit in results:
            spamwriter.writerow(
                [hit.date.rstrip(), hit.title.rstrip(), hit.desc.rstrip()])


# lista de noticias
write_to_csv("dataset_publico.csv", publico.search("economia", 5))

write_to_csv("dataset_expresso.csv", expresso.search(
    date(2020, 12, 14), pd.to_datetime('today').date(), 0.5))

#implementar para o CM:

