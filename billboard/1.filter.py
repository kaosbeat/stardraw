


import re
import os
import io

def search_for_lines_containing_elements_of_list(search_terms):
    pattern = r"(?:" + "|".join([re.escape(term) for term in search_terms]) + ").*"
    return lambda text: '\n'.join(line for line in text.splitlines() if re.search(pattern, line, re.IGNORECASE))

# Example usage:
search_terms = ["Gent", "Ghent", "Afsnee", "Desteldonk", "Drongen", "Gentbrugge", "Ledeberg", "Mariakerke", "Mendonk", "Oostakker", "Sint-Amandsberg", "Sint-Denijs-Westrem", "Sint-Kruis-Winkel", "Wondelgem", "Zwijnaarde", "Sint Amandsberg", "Sint Denijs Westrem", "Sint Kruis Winkel"]
input_file = 'Belgium.csv'
output_file = 'Gent.csv'

text = '''
32460203482,100010822305994,Mafalda Pinho,Fonseca,female,Dublin, Ireland,,,,1/6/2016 12,00,00 AM,,
32460203501,100009589493628,Criss,Hodorowski,male,Kortrijk,Brussels, Belgium,,Crelan Bank,8/4/2015 12,00,00 AM,,
32460203510,100009864401618,Aya,Ahmed,female,,,,,1/1/0001 12,00,00 AM,,
32460203552,100010822260138,Eolanda,Bobrova,female,,,,,11/26/2015 12,00,00 AM,,
32460203616,100010259282016,Annton,Messenger,male,Gent, Belgium,Gent, Belgium,,Hilton Hotels & Resorts,8/4/2015 12,00,00 AM,,
32460203669,100009551934999,Nada,Ahmed,female,Cairo, Egypt,Moscow, Russia,,,1/12/2017 12,00,00 AM,,
32460203728,100010827853270,Romaine,Patry,female,Brussels, Belgium,Brussels, Belgium,,,12/14/2015 12,00,00 AM,,
32460204139,100021700673039,Lucas,Wellson,male,,,,,1/1/0001 12,00,00 AM,,
32460204651,100022189682110,지운,김,male,,,,,1/1/0001 12,00,00 AM,,
32460204742,100022984749782,Zehra,Zermo,female,,,,,1/1/0001 12,00,00 AM,,
32460204897,100010874823303,Dode,Lobiz,female,,,,,1/1/0001 12,00,00 AM,,
32460205490,100027224593569,رواء,السامرائي,female,Samarra',,,,7/12/2018 12,00,00 AM,,
32460205616,100026081676477,عبد الخالق,العبادي,male,Basra, Iraq,,,,1/1/0001 12,00,00 AM,,
32460205721,100015470508682,Leha,Skaf,male,,,,,1/1/0001 12,00,00 AM,,
32460205734,100012785986889,佳瑜,劉,female,,,,,1/1/0001 12,00,00 AM,,
32460205780,100010770765998,Mixail,Andreev,male,,,,,1/1/0001 12,00,00 AM,,
32460205781,100020893473415,Ron,Milan,male,,,,,1/1/0001 12,00,00 AM,,
32460205788,100023021771438,Jack,Smith,male,,,,,11/17/2017 12,00,00 AM,,
32460205854,100018754752016,Alex,Finorg,male,,,,,1/1/0001 12,00,00 AM,,
32460205862,100011797751434,Valentin,Meniaylo,male,,,,,4/12/2016 12,00,00 AM,,
32460205985,100000461362745,Serbest,Bilal,male,,,,,3/18/2018 12,00,00 AM,,
32460205987,100026490750118,Ergün,Barut,male,,,,,1/1/0001 12,00,00 AM,,
32460206094,100004111157101,Joseph,Brown,male,Washington, District of Columbia,Belgrade, Serbia,,,12/28/2016 12,00,00 AM,,
32460206097,100017874872372,Dav,SuGar,male,,,,,1/1/0001 12,00,00 AM,,
32460206099,100022017082906,Rachel,Gaskell,female,,,,,9/18/2017 12,00,00 AM,,
32460206109,100017743275920,Salvadir,Dvr,male,,,,Soper Market,5/20/2018 12,00,00 AM,,
32460206117,1561393923,الإله العظيم,الإله العظيم,male,,,Single,YBNL,6/15/2018 12,00,00 AM,,08/01/1948
32460206118,100022467573551,Alp,Şhn,male,Maasmechelen,Gent, Belgium,Divorced,Construction Technician,6/24/2018 12,00,00 AM,,
32460206132,100016213368052,Kimberly,Middleton,female,Leipzig-Wahren, Sachsen, Germany,Los Angeles, California,,World Health Organization (WHO),5/4/2017 12,00,00 AM,,
32460206142,100025458803903,Irish,Etchusetchus,female,,,,,1/1/0001 12,00,00 AM,,
32490432809,100015140821277,Annick,Byn,female,Sint-Amandsberg,,,,4/1/2018 12,00,00 AM,,
'''




def process_file(input_file, output_file, list):
    pattern = r"(?:" + "|".join([re.escape(term) for term in list]) + ").*"
    with open(input_file, 'r') as f_in:
        filtered_text = ''
        for line in f_in:
            if re.search(pattern, line, re.IGNORECASE):
                filtered_text += line
                # print(line)
        with open(output_file, 'w') as f_out:
            f_out.write(filtered_text)


def process_var(var, list):
        pattern = r"(?:" + "|".join([re.escape(term) for term in list]) + ").*"
        filtered_text = ''
        for line in io.StringIO(var):
            if re.search(pattern, line, re.IGNORECASE):
                filtered_text += line
                
        
        print(filtered_text)


process_file(input_file, output_file, search_terms)
# process_var(text,search_terms)