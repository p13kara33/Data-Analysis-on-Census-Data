import docx
import pandas as pd

age = {1: '0 to 15', 2: '16 to 24', 3: '15 to 34', 4: '45 to 44', 5: '45 to 54',
       6: '55 to 64', 7: '65 to 74',
       8: '75 and over'}

colors = ["black", "#ff692e", "#2e5cff", "#ffd12e", "#ff2e5c", "#5cff2e", "#ff0000",
          "#8b4513", "#ff7f50", "#ffff80", '#9370db', '#ff581a', '#c75757']


def descrtable_doc_creator(my_data, col_name, doc_name):
    """
    :param my_data: the data frame
    :param col_name: the attribute name
    :return: the frequency table as a dictionary
    :param doc_name: name of the docx file
    """

    mydf = pd.DataFrame(my_data[col_name])
    df = mydf.describe()

    doc = docx.Document()

    t = doc.add_table(df.shape[0] + 1, df.shape[1])

    # add the header rows.
    for j in range(df.shape[-1]):
        t.cell(0, j).text = df.columns[j]

    # add the rest of the data frame
    for i in range(df.shape[0]):
        for j in range(df.shape[-1]):
            t.cell(i + 1, j).text = str(df.values[i, j])

    # save the doc
    doc_name = doc_name + ".docx"
    doc.save(doc_name)


    return df
