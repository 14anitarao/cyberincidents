
from PyPDF2 import PdfReader
import matplotlib.pyplot as plt

'''
This is a script that parses CSIS's list of Significant Cyber Incidents since 2006
https://csis-website-prod.s3.amazonaws.com/s3fs-public/2023-08/230804_Significant_Cyber_Events.pdf?VersionId=4gFwypzI2sLoxgX.9mUbuJfsIQDcV3is

Modify num_years_back and current_year to adjust the plot results accordingly.
'''


def main():
    num_years_back = 6
    current_year = 2023

    if (current_year-num_years_back+1 < 2006):
        print("Cannot go back before 2006")
        num_years_back = current_year-2006+1

    arr = [0] * num_years_back

    years = {}
    for i in range(num_years_back):
        yr = current_year-num_years_back+i+1
        str_yr = str(yr)
        years[str_yr] = i

    # years = {"2018":0, "2019":1, "2020":2, "2021":3, "2022":4, "2023":5}

    reader = PdfReader("230804_Significant_Cyber_Events.pdf")
    number_of_pages = len(reader.pages)
    for i in range(number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        if sum(map(text.count, tuple(list(years.keys())))) > 0:
            for x in list(years.keys()):
                arr[years[x]] += text.count(x)
        else:
            break

    x_axis = list(years.keys())
    y_axis = arr
    print("Reports",arr)

    plt.bar(x_axis, y_axis)
    plt.title('CSIS Reported Cyber Incidents')
    plt.xlabel('Year')
    plt.ylabel('Number of Cyber Incidents')
    plt.gcf().autofmt_xdate()
    plt.savefig('CyberIncidents.png')

if __name__ == '__main__':
    main()
