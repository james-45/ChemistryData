import csv

quest1 = int(input('Voltametrias ciclicas? (1 = sim ou 0 = não): '))

if quest1 == 1:
    def tratar_volt():
        arquivo1 = input("Digite o nome do arquivo: ")
        nome_txt = arquivo1 + ".txt"
        nome_csv = arquivo1 + ".csv"
        ecsa = float(input('Digite o valor da área do {}: '.format(arquivo1)).replace(',', '.'))
        with open(nome_txt) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            csv_reader.__next__()

            with open(nome_csv, 'w', newline='') as csv__file:
                csv.writer(csv__file, delimiter=';').writerow(['WE(1).Potential (V)', 'WE(1).Current (A)'])

                for row in csv_reader:
                    if int(row[0]) == 5:
                        current = float(row[4].replace(',', '.'))
                        i_area = (str(current / ecsa)).replace('.', ',')  # densidade de corrente
                        csv.writer(csv__file, delimiter=';').writerow([row[3], i_area])
                print('Conversão de {} terminada!'.format(nome_csv))

        return tratar_volt()

    tratar_volt()


if quest1 == 0:
    quest2 = int(input("Eletrólise convencional (1) ou múltiplas (2)?"))
    
    if quest2 == 1:
        def tratar_elet():
            arquivo1 = input("Então eletrólise convencional. Digite o nome do arquivo: ")
            nome_txt = arquivo1 + ".txt"
            nome_csv = arquivo1 + ".csv"
            ecsa = float(input('Digite o valor da área do {}: '.format(arquivo1)).replace(',', '.'))

            with open(nome_txt) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                csv_reader.__next__()

                with open(nome_csv, 'w', newline='') as csv__file:
                    csv.writer(csv__file, delimiter=';').writerow(['WE(1).Potential (V)', 'WE(1).Current (A)'])

                    for row in csv_reader:
                        current = float(row[2].replace(',', '.'))
                        i_area = (str(current / ecsa)).replace('.', ',')  # densidade de corrente

                        csv.writer(csv__file, delimiter=';').writerow([row[3], i_area])
                    print('Conversão de {} terminada!'.format(nome_csv))

            return tratar_elet()

        tratar_elet()

    if quest2 == 2:
        def tratar_elet_multi():
            arquivo1 = input("Então eletrólise múltipla. Digite o nome do arquivo: ")
            time = int(input("Qual é esta eletrólise? "))
            nome_txt = arquivo1 + ".txt"
            nome_csv = arquivo1 + ".csv"
            ecsa = float(input('Digite o valor da área do {}: '.format(arquivo1)).replace(',', '.'))

            with open(nome_txt) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                csv_reader.__next__()

                with open(nome_csv, 'w', newline='') as csv__file:
                    csv.writer(csv__file, delimiter=';').writerow(['Time (s)', 'WE(1).Current (A)'])

                    for row in csv_reader:
                        current = float(row[2].replace(',', '.'))
                        i_area = (str(current / ecsa)).replace('.', ',')  # densidade de corrente

                        time_row = float(row[3].replace(',','.'))
                        time_axis = (str(time_row + (time*3600))).replace('.',',')

                        csv.writer(csv__file, delimiter=';').writerow([time_axis, i_area])
                    print('Conversão de {} terminada!'.format(nome_csv))

            return tratar_elet_multi()

        tratar_elet_multi()


elif quest1 != 0 or quest1 != 1:
    print('reinicie o código!')