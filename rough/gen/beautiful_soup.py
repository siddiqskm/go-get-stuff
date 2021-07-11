"""
Parser
"""
#!/usr/bin/python

from bs4 import BeautifulSoup

html_dict = {
    "split1": "/Users/shussian/Desktop/temp/jReports/split1/htmlreport/index.html",
    "sqlancer": "/Users/shussian/Desktop/temp/jReports/htmlreport/index.html"
}

def get_jreport(input_file):
    ret_dict = {}
    with open(input_file, 'r') as f:
        contents = f.read()

        soup = BeautifulSoup(contents, 'lxml')

        table = soup.find("table", {"id": "coveragetable"})
        for eachr in table.tbody.findAll('tr'):
            tds = eachr.findAll("td")
            c_name = tds[0].text
            c_percent = tds[2].text
            ret_dict.update({c_name: c_percent})
    # Return the sp dict now
    return ret_dict


sp1_dict = get_jreport(html_dict['split1'])
sqlancer_dict = get_jreport(html_dict['sqlancer'])
for each_key in sp1_dict:
    if each_key in sqlancer_dict:
        print("%s,%s,%s" % (each_key, sp1_dict.get(each_key), sqlancer_dict.get(each_key)))

