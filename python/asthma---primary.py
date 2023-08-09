# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"14B4.00","system":"readv2"},{"code":"173c.00","system":"readv2"},{"code":"173d.00","system":"readv2"},{"code":"1O2..00","system":"readv2"},{"code":"H33..00","system":"readv2"},{"code":"H33..11","system":"readv2"},{"code":"H330.12","system":"readv2"},{"code":"H330.14","system":"readv2"},{"code":"H331.11","system":"readv2"},{"code":"H332.00","system":"readv2"},{"code":"H333.00","system":"readv2"},{"code":"H334.00","system":"readv2"},{"code":"H33z.00","system":"readv2"},{"code":"H33z.11","system":"readv2"},{"code":"H33z000","system":"readv2"},{"code":"H33z200","system":"readv2"},{"code":"H33zz00","system":"readv2"},{"code":"106805.0","system":"med"},{"code":"11370.0","system":"med"},{"code":"1208.0","system":"med"},{"code":"12987.0","system":"med"},{"code":"14777.0","system":"med"},{"code":"15248.0","system":"med"},{"code":"1555.0","system":"med"},{"code":"16070.0","system":"med"},{"code":"18207.0","system":"med"},{"code":"18323.0","system":"med"},{"code":"185.0","system":"med"},{"code":"21232.0","system":"med"},{"code":"22752.0","system":"med"},{"code":"2290.0","system":"med"},{"code":"232.0","system":"med"},{"code":"233.0","system":"med"},{"code":"25796.0","system":"med"},{"code":"27926.0","system":"med"},{"code":"29325.0","system":"med"},{"code":"32727.0","system":"med"},{"code":"3665.0","system":"med"},{"code":"40823.0","system":"med"},{"code":"41017.0","system":"med"},{"code":"4442.0","system":"med"},{"code":"45073.0","system":"med"},{"code":"45782.0","system":"med"},{"code":"4606.0","system":"med"},{"code":"4892.0","system":"med"},{"code":"5267.0","system":"med"},{"code":"5627.0","system":"med"},{"code":"5798.0","system":"med"},{"code":"58196.0","system":"med"},{"code":"5867.0","system":"med"},{"code":"6707.0","system":"med"},{"code":"7146.0","system":"med"},{"code":"73522.0","system":"med"},{"code":"7731.0","system":"med"},{"code":"78.0","system":"med"},{"code":"8335.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["asthma---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["asthma---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["asthma---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
