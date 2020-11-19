import requests
import xlrd
import re

def getIPsFromExcelFile():
    IPs = []
    IPCheck = re.compile(r'^([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)$')
    excelFile = (r"C:\Users\dkamalanathan\OneDrive - Intrinium\Documents\FilterIPsByCount\Children Hospital LA X-force Scanning IPs Categorization.xls")
    wb = xlrd.open_workbook(excelFile)
    sheet = wb.sheet_by_index(0)
    for x in range(sheet.ncols - 1):
        for y in range(sheet.nrows - 1):
            value = sheet.cell_value(y,x)
            if IPCheck.match(value):
                IPs.append(value)
    return IPs


def getIPsToBan(IPs):
    # IPs = []
    IPsWithCount = {}
    IPsToBan = []

    # fo = open("../IPList.txt", "r")
    # IPs = fo.readlines()

    for IP in IPs:
        if IP in IPsWithCount:
            IPsWithCount[IP]+=1
            
        if IP not in IPsWithCount:
            IPsWithCount[IP] = 1

    for IP in IPsWithCount:
        if IPsWithCount[IP] >= 10:
            IPsToBan.append(IP)
            
    return IPsToBan

def checkIfMalicious(IPsToCheck):
    apikey = "c59c8a2ac5998fce2a6d259cc431bb31b5485fef"
    MalIPs = []
    for IP in IPsToCheck:
        response = requests.get('https://endpoint.apivoid.com/iprep/v1/pay-as-you-go/?key='+apikey+'&ip='+IP)
        if response.status_code == 200:
            response_json = response.json()
            try:
                if response_json['data']['report']['blacklists']['detections'] >= 1:
                    MalIPs.append(IP)
            except:
                pass
                
    return MalIPs

if __name__ == "__main__":
    import sys
    IPs = getIPsFromExcelFile()
    IPsToBan = getIPsToBan(IPs)
    MaliciousIPs = checkIfMalicious(IPsToBan)
    for IP in MaliciousIPs:
        print(IP)