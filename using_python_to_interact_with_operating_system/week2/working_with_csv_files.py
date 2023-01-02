import csv
hosts = [["Denzel", "0714082283"], ["Junne", "0726151007"]] # The values to input in the csv file
# Open a csv file
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
#  cat hosts.csv -- open the file
