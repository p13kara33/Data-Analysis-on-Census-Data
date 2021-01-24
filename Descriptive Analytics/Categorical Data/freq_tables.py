import docx
import pandas as pd

regions = {'E12000001': 'North East', 'E12000002': 'North West',
           'E12000003': 'Yorkshire and the Humber', 'E12000004': 'East Midlands',
           'E12000005': 'West Midlands', 'E12000009': 'South West',
           'E12000006': 'East of England', 'E12000008': 'South East',
           'E12000007': 'London', 'W92000004': 'Wales'}

residence_type = {'H': 'Not resident in a communal establishment',
                  "C": 'Resident in a communal establishment'}

family_composition = {-9: 'No code required', 1: 'Not in a family',
                      2: 'Married/same-sex civil partnership couple family',
                      3: 'Cohabiting couple family', 4: 'Lone parent family (male head)',
                      5: 'Lone parent family (female head)', 6: 'Other related family'}

population_base = {1: 'Usual resident',
                   2: 'Student living away from home during term-time',
                   3: 'Short-term resident'}

sex = {1: 'Male', 2: 'Female'}

age = {1: '0 to 15', 2: '16 to 24', 3: '25 to 34', 4: '35 to 44', 5: '45 to 54',
       6: '55 to 64', 7: '65 to 74',
       8: '75 and over'}

marital_status = {1: 'Single', 2: 'Married', 3: 'Separated but still legally married',
                  4: 'Divorced ', 5: 'Widowed'}

student = {1: 'Student', 2: 'No Student'}

country_of_birth = {-9: 'No code required', 1: 'UK', 2: 'Non UK'}

health = {-9: 'No code required', 1: 'Very good health', 2: 'Good health',
          3: 'Fair health', 4: 'Bad health', 5: 'Very bad health'}

ethnic_group = {-9: 'No code required', 1: 'White', 2: 'Mixed',
                3: 'Asian and Asian British', 4: 'Black or Black British',
                5: 'Chinese or Other ethnic group'}

religion = {-9: 'No code required', 1: 'No religion', 2: 'Christian', 3: 'Buddhist',
            4: 'Hindu', 5: 'Jewish', 6: 'Muslim', 7: 'Sikh', 8: 'Other religion',
            9: 'Not stated'}

economic_activity = {-9: 'No code required', 1: 'Economically active: Employee',
                     2: 'Economically active: Self-employed',
                     3: 'Economically active: Unemployed',
                     4: 'Economically active: Full-time student',
                     5: 'Economically inactive: Retired',
                     6: 'Economically inactive: Student',
                     7: 'Economically inactive: Looking after home or family',
                     8: 'Economically inactive: Long-term sick or disabled',
                     9: 'Economically inactive: Other'}

occupation = {-9: 'No code required', 1: 'Managers, Directors and Senior Officials',
              2: 'Professional Occupations',
              3: 'Associate Professional and Technical Occupations',
              4: 'Administrative and Secretarial Occupations',
              5: 'Skilled Trades Occupations',
              6: 'Caring, Leisure and Other Service Occupations',
              7: 'Sales and Customer Service Occupations',
              8: 'Process, Plant and Machine Operatives', 9: 'Elementary Occupations'}

industry = {-9: 'No code required', 1: 'Agriculture, forestry and fishing',
            2: 'Mining and quarrying; Manufacturing;', 3: 'Construction',
            4: 'Wholesale and retail trade; Repair of motor vehicles and motorcycles',
            5: 'Accommodation and food service', 6: 'Transport and storage',
            7: 'Financial and insurance', 8: 'Real estate',
            9: 'Public administration and defence', 10: 'Education',
            11: 'Human health and social work activities',
            12: 'Other community, social and personal service activities'}

hw_per_week = {-9: 'No code required', 1: 'Part-time: 15 or less h.w.',
               2: 'Part-time: 16 to 30 hw', 3: 'Full-time: 31 to 48 hw',
               4: 'Full-time: 49 or more hw'}

approx_social_grade = {-9: 'No code required', 1: 'AB', 2: 'C1', 3: 'C2', 4: 'DE'}

colors = ["black", "#ff692e", "#2e5cff", "#ffd12e", "#ff2e5c", "#5cff2e", "#ff0000",
          "#8b4513", "#ff7f50", "#ffff80", '#9370db', '#ff581a', '#c75757']


def freq_dict_creator(my_data, col_name, dictionary, doc_name):
    """
    :param my_data: the data frame
    :param col_name: the attribute name
    :param dictionary: the name of the dictionary of the attribute
    :return: the frequency table as a dictionary
    :param doc_name: name of the docx file
    """

    freq_arr = my_data[col_name].value_counts(sort=True)
    perc_arr = my_data[col_name].value_counts(normalize=True, sort=True)
    percentages = []
    the_list = []

    for i in perc_arr.index:
        val = perc_arr[i] * 100
        val = round(val, 1)
        percentages.append(str(val) + '%')

    cnt = 0
    for i in freq_arr.index:
        col_descr = dictionary[i]
        the_list.append([[col_descr], [freq_arr[i]], [percentages[cnt]]])
        cnt += 1

    df = pd.DataFrame(the_list, columns=[col_name, 'Frequency', 'Percentages'])

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
    # doc.save(doc_name)

    return df
