
def run():

    import urllib3
    import csv
    from cmp.models import Country
    
    ref_data_url = "https://raw.githubusercontent.com/mledoze/countries/master/dist/countries.csv"
    http = urllib3.PoolManager()
    r = http.request('GET', ref_data_url)
    print(r.status)
    # load the response into a csv dictionary reader
    reader = csv.DictReader(r.data.decode('utf-8').splitlines())
    reader.fieldnames = [field.replace('.', '_') for field in reader.fieldnames]
    
    # add a country model for each row in the csv file
    for row in reader:
        print(row['name_common'])
        if row['name_common'] == 'Kosovo':
            row['ccn3'] = '999'
            row['independent'] = False
        try:
            Country.objects.create(
                name_common=row['name_common'],
                name_official=row['name_official'],
                tld=row['tld'],
                cca2=row['cca2'],
                ccn3=row['ccn3'],
                cca3=row['cca3'],
                cioc=row['cioc'],
                independent=row['independent'],
                status=row['status'],
                unMember=row['unMember'],
                currencies=row['currencies'],
                idd_root=row['idd_root'],
                idd_suffixes=row['idd_suffixes'],
                capital=row['capital'],
                alt_spellings=row['altSpellings'],
                region=row['region'],
                subregion=row['subregion'],
                languages=row['languages'],
                translations_ces_official=row['translations_ces_official'],
                translations_ces_common=row['translations_ces_common'],
                translations_deu_official=row['translations_deu_official'],
                translations_deu_common=row['translations_deu_common'],
                translations_est_official=row['translations_est_official'],
                translations_est_common=row['translations_est_common'],
                translations_fin_official=row['translations_fin_official'],
                translations_fin_common=row['translations_fin_common'],
                translations_fra_official=row['translations_fra_official'],
                translations_fra_common=row['translations_fra_common'],
                translations_hrv_official=row['translations_hrv_official'],
                translations_hrv_common=row['translations_hrv_common'],
                translations_hun_official=row['translations_hun_official'],
                translations_hun_common=row['translations_hun_common'],
                translations_ita_official=row['translations_ita_official'],
                translations_ita_common=row['translations_ita_common'],
                translations_jpn_official=row['translations_jpn_official'],
                translations_jpn_common=row['translations_jpn_common'],
                translations_kor_official=row['translations_kor_official'],
                translations_kor_common=row['translations_kor_common'],
                translations_nld_official=row['translations_nld_official'],
                translations_nld_common=row['translations_nld_common'],
                translations_per_official=row['translations_per_official'],
                translations_per_common=row['translations_per_common'],
                translations_pol_official=row['translations_pol_official'],
                translations_pol_common=row['translations_pol_common'],
                translations_por_official=row['translations_por_official'],
                translations_por_common=row['translations_por_common'],
                translations_rus_official=row['translations_rus_official'],
                translations_rus_common=row['translations_rus_common'],
                translations_slk_official=row['translations_slk_official'],
                translations_slk_common=row['translations_slk_common'],
                translations_spa_official=row['translations_spa_official'],
                translations_spa_common=row['translations_spa_common'],
                translations_swe_official=row['translations_swe_official'],
                translations_swe_common=row['translations_swe_common'],
                translations_urd_official=row['translations_urd_official'],
                translations_urd_common=row['translations_urd_common'],
                translations_zho_official=row['translations_zho_official'],
                translations_zho_common=row['translations_zho_common'],
                latlng=row['latlng'],
                landlocked=row['landlocked'],
                borders=row['borders'],
                area=row['area'],
                flag=row['flag'],
                demonyms_eng_f=row['demonyms_eng_f'],
                demonyms_eng_m=row['demonyms_eng_m'],
                demonyms_fra_f=row['demonyms_fra_f'],
                demonyms_fra_m=row['demonyms_fra_m'],
                callingCodes=row['callingCodes']
        )
        except Exception as e:
            print("Error with: " + row['name_common'])
            raise e


        


        



