import pandas as pd
import crawler


def main():
    all_countries = []
    countries = crawler.read_countries()
    for country in countries:
        curr_country = []
        try:
            curr_country.append(country)
            url = crawler.set_url(country)
            data = crawler.read_html(url)
            try:
                capital = crawler.find_capital(data)
                curr_country.append(capital)
            except:
                curr_country.append('')
            try:
                languages = crawler.find_languages(data)
                curr_country.append(languages)
            except:
                curr_country.append('')
            try:
                ethnic_groups = crawler.find_ethnic_groups(data)
                curr_country.append(ethnic_groups)
            except:
                curr_country.append('')
            try:
                religion_groups = crawler.find_religion_groups(data)
                curr_country.append(religion_groups)
            except:
                curr_country.append('')
            all_countries.append(curr_country)
        except:
            continue
    my_data = pd.DataFrame(all_countries)
    my_data.columns = ['country', 'capital', 'languages', 'ethnic groups', 'religion groups']
    my_data.to_csv('myData.csv', sep='\t')


if __name__ == "__main__":
    main()
