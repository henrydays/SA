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

            title = hit.title.rstrip() if hit.title != None else 'erro'
            date = hit.date.rstrip() if hit.date != None else 'erro'
            description = hit.desc.rstrip() if hit.desc != None else 'erro'

            spamwriter.writerow(
                [date, title, description])


# lista de noticias
write_to_csv("dataset_publico.csv", publico.search("economia", 30000))

write_to_csv("dataset_expresso.csv", expresso.search(
    date(2010, 1, 1), pd.to_datetime('today').date(), 0.5))

# implementar para o CM:
