import pandas as pd

#function that comparing two files,
# and then returning master database without duplicates ordered by 'cause'

def merging_without_dupliactes(file1, file2):
    frames = [file2, file1]
    result = pd.concat(frames)
    result = result.reset_index(drop=True)
    result.drop_duplicates(inplace=True)
    result = result.sort_values(by=['cause'])
    result.to_csv('company_db.csv', index=False)

#function that compares new file with master db,
# and then returning orginial records from a new file
# ordered by 'cause'

def og_output(file1):
    file1 = file1[~(file1['e-mail'].isin(cdb['e-mail']))].reset_index(drop=True)
    file1.to_csv('orginal_cp.csv', mode='a', index=False, header=False)


cdb = pd.read_csv('company_db.csv')
print("Działanie programu:\n"
      "Należy podać nazwę pliku w formie: nazwa.rozszerzenie\n"
      "[!]Pliki muszą być w tym samym folderze co skrypt[!]\n")
run = True
while(run):
    try:
        file_to_read = input("Podaj nazwę pliku do wczytania: ")
        ftr = pd.read_csv(file_to_read, sep=',',names=['c_name', 'e-mail', 'cause'])
        merging_without_dupliactes(cdb, ftr)
        og_output(ftr)
        og = pd.read_csv('orginal_cp.csv',names=['c_name', 'e-mail', 'cause'])
        og = og.sort_values(by=['cause'])
        og.to_csv('orginal_cp.csv', mode='w', index=False, header=False)
        run = False
    except:
        print("Plik nie znaleziony!")



