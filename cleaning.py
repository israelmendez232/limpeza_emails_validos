import re
import smtplib
import dns.resolver
import csv
import pandas as pd
import sys
import colorama
from colorama import Fore, Style

fromAddress = 'corn@bt.com'
regex = "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$"

def badSyntax(emailPreValidation):
    match = re.match(regex, emailPreValidation)
    if match == None:
    	return True

columns = ['Nome', 'Email', 'Telefone', 'Status']

# Abre a base original e faz uma cópia, trabalhando nela:
inFileSubscribers = pd.read_csv("./teste.csv", error_bad_lines=False)
inFileSubscribersDF = pd.DataFrame(inFileSubscribers, columns = columns)

# inFileSubscribersDF.to_csv('out.csv', index=False, columns = columns)

outFileSubscribers = pd.read_csv("./out.csv", error_bad_lines=False)
outFileSubscribersDF = pd.DataFrame(outFileSubscribers, columns = columns)

for index, row in inFileSubscribersDF.iterrows():
    # Configurações | Também copiamos a linha original no arquivo final, para depois substituir o status. 
    # Mantendo o arquivo original intacto.
    emailForValidation = 'Email'
    status = 'Status'
    statusColumn = outFileSubscribersDF[status].iloc[index]

    # 1. Validação por REGEX 
    emailPreValidation = inFileSubscribersDF[emailForValidation].iloc[index]

    if badSyntax(emailPreValidation):
        outFileSubscribersDF.at[index, status] = 'Unsubscribe'
        # outFileSubscribersDF[status].replace(statusColumn, 'Unsubscribe', inplace=True)

    # 2. Validação por DNS 

    # 3. Validação por SMTP 

print(outFileSubscribersDF)

# outFileSubscribersCSV.writerow(row)
# outFileSubscribersCSV.writerow(row)

# inFileSubscribers = open("./teste.csv", "r")
# inFileSubscribersCSV = csv.reader(inFileSubscribers, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

""" for row in inSubscribersFileRead:
    emailForValidation = str(row[3])
    status = str(row[6])
    resultBadSyntax = badSyntax(emailForValidation)
    if resultBadSyntax == "badEmail":
        row[6] = "Unsubscribe"
        outSubscribersFileRead.writerow(row[6])
    resultsmtpDnsValidtion = smtpDnsValidtion(emailForValidation)
    if resultsmtpDnsValidtion == "notExistingEmail":
        row[6] = "Unsubscribe"
        outSubscribersFileRead.writerow(row[6])


def smtpDnsValidtion(addressToVerify):
    splitAddress = addressToVerify.split('@')
    domain = str(splitAddress[1])

    records = dns.resolver.query(domain, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)

    server = smtplib.SMTP()
    server.set_debuglevel(0)

    server.connect(mxRecord)
    server.helo(server.local_hostname)
    server.mail(fromAddress)
    code, message = server.rcpt(str(addressToVerify))
    server.quit()

    if code == 250:
        return "existingEmail"
    else:
        return "notExistingEmail" """