import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import seaborn as sns
# import pandas.plotting

a = np.array([])
"""
Assign the dataset on the variable data, and creating dictionaries with key  the values of the csv file and
as values the description of every key accordingly to the Microdatateachingvariables.pdf file
"""
data = pd.read_csv(r"C:\\Users\\Giorgis\\Desktop\\Projects\\ADTA coursework\\partI\\Census.csv")

regions = {'E12000001': 'North East', 'E12000002': 'North West', 'E12000003': 'Yorkshire and the Humber',
           'E12000004': 'East Midlands', 'E12000005': 'West Midlands', 'E12000006': 'East of England',
           'E12000007': 'London', 'E12000008': 'South East', 'E12000009': 'South West', 'W92000004': 'Wales'}
residence_type = {"C": 'Resident in a communal establishment', 'H': 'Not resident in a communal establishment'}
family_composition = {1: 'Not in a family', 2: 'Married/same-sex civil partnership couple family',
                      3: 'Cohabiting couple family', 4: 'Lone parent family (male head)',
                      5: 'Lone parent family (female head)', 6: 'Other related family',
                      -9: "No code required (Resident of a communal establishment, students or schoolchildren "
                          "living away during term-time, or a short-term resident)"}
population_base = {1: 'Usual resident', 2: 'Student living away from home during term-time', 3: 'Short-term resident'}
sex = {1: 'Male', 2: 'Female'}
age = {1: '0 to 15', 2: '16 to 24', 3: '15 to 34', 4: '45 to 44', 5: '45 to 54', 6: '55 to 64', 7: '65 to 74',
       8: '75 and over'}
marital_status = {1: 'Single', 2: 'Married or in a registered same-sex civil partnership',
                  3: 'Separated but still legally married or separated, rated but still legally in a same-sex civil '
                     'partnership', 4: 'Divorced or formerly in a same-sex civil partnership which is now legally '
                                       'dissolved', 5: 'Widowed or surviving partner from a same-sex civil partnership'}
student = {1: 'Yes', 2: 'No'}
country_of_birth = {1: 'UK', 2: 'Non UK',
                    -9: 'No Code required (Students or schoolchildren living away during term-time)'}
health = {1: 'Very good health', 2: 'Good health', 3: 'Fair health', 4: 'Bad health', 5: 'Very bad health',
          -9: 'No code required (Students or school children living away during term-time)'}
ethnic_group = {1: 'White', 2: 'Mixed', 3: 'Asian and Asian British', 4: 'Black or Black British',
                5: 'Black or Black British',
                6: 'Chinese or Other ethnic group',
                -9: 'No code required (Not resident in England or Wales, students or schoolchildren living away '
                    'during term-time)'}
religion = {1: 'No religion', 2: 'Christian', 3: 'Buddhist', 4: 'Hindu', 5: 'Jewish', 6: 'Muslim', 7: 'Sikh',
            8: 'Other religion',
            9: 'Not stated',
            -9: 'No code required (Not resident in England orWales, students or school children living away during '
                'term-time)'}
economic_activity = {1: 'Economically active: Employee', 2: 'Economically active: Self-employed',
                     3: 'Economically active: Unemployed',
                     4: 'Economically active: Full-time student', 5: 'Economically inactive: Retired',
                     6: 'Economically inactive: Student',
                     7: 'Economically inactive: Looking after home or family',
                     8: 'Economically inactive: Long-term sick or disabled',
                     9: 'Economically inactive: Other',
                     -9: 'No code required (Aged under 16 or students or schoolchildren living away during term-time)'}
occupation = {1: 'Managers, Directors and Senior Officials', 2: 'Professional Occupations',
              3: 'Associate Professional and Technical Occupations',
              4: 'Administrative and Secretarial Occupations', 5: 'Skilled Trades Occupations',
              6: 'Caring, Leisure and Other Service Occupations',
              7: 'Sales and Customer Service Occupations', 8: 'Process, Plant and Machine Operatives',
              9: 'Elementary Occupations',
              -9: 'No code required (People aged under 16, people who have never worked and students or '
                  'schoolchildren living away during term-time)'}
industry = {1: 'Agriculture, forestry and fishing',
            2: 'Mining and quarrying; Manufacturing; Electricity, gas, steam and air conditioning system; Water supply',
            3: 'Construction', 4: 'Wholesale and retail trade; Repair of motor vehicles and motorcycles',
            5: 'Accommodation and food service activities', 6: 'Transport and storage; Information and communication',
            7: 'Financial and insurance activities; Intermediation',
            8: 'Real estate activities; Professional, scientific and technical activities; Administrative and support '
               'service activities',
            9: 'Public administration and defence; compulsory social security', 10: 'Education',
            11: 'Human health and social work activities',
            12: 'Other community, social and personal service activities; Private households employing domestic '
                'staff; Extra-territorial organisations and bodies', -9: 'No code required (People aged under 16, '
                                                                         'people who have never worked, and students '
                                                                         'or schoolchildren living away during '
                                                                         'term-time)'}
hrs_worked_per_weel = {1: 'Part-time: 15 or less hours worked', 2: 'Part-time: 16 to 30 hours worked ',
                       3: 'Full-time: 31 to 48 hours worked',
                       4: 'Full-time: 49 or more hours worked',
                       -9: 'No code required (People aged under 16, people not working, and students or '
                           'schoolchildren living away during term-time)'}
approx_social_grade = {1: 'AB', 2: 'C1', 3: 'C2', 4: 'DE',
                       -9: 'No code required (People aged under 16, people resident in communal establishments, '
                           'and students or schoolchildren living away during term time)'}

"""
class pies:
    def pie2v(col1_name, dict1, col2_name, dict2, val1):
        select_column1 = data[(data[col1_name] == val1)]
        # select_column2 = select_column1[(select_column1[col2_name] == val2)]
    
        labels = []
        sizes = []
        explode = []
    
        for size, label in dict2.items():
            labels.append(label)
            sizes.append(select_column1.groupby([col2_name]).get_group(size).count().iloc[0])
            # sizes.append(((data.groupby[col2_name]).get_group(size).count()).ilco[0])
            # ((data.groupby([interest_col])).get_group(dictI_code).count()).iloc[0]
            explode.append(0.03)
    
            explode = tuple(explode)
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()
    
    def pie_show(col1_name, dict1, col2_name, dict2):
        for dict1_code, dict1_description in dict1.items():
            # for dict2_code, dict2_desctiption in dict2.items():
            print('{}: {}'.format(col1_name, dict1_description))
            pie2v(col1_name, dict1, col2_name, dict2, dict1_code)

"""


def pie1v(col1_name, dict1):
    labels = []
    sizes = []
    explode = []

    for size, label in dict1.items():
        labels.append(label)
        sizes.append(data.groupby([col1_name]).get_group(size).count().iloc[0])
        explode.append(0.05)

    explode = tuple(explode)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


def pie1_1v(col1_name, val1, col2_name, dict2):
    select_column1 = data[(data[col1_name] == val1)]

    labels = []
    sizes = []
    explode = []

    for size, label in dict2.items():
        labels.append(label)
        sizes.append(select_column1.groupby([col2_name]).get_group(size).count().iloc[0])
        explode.append(0.03)

    explode = tuple(explode)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


def pie2v(col1_name, dict1, col2_name, dict2, val1):
    select_column1 = data[(data[col1_name] == val1)]
    # select_column2 = select_column1[(select_column1[col2_name] == val2)]
    """male = select_column2.groupby(['Sex']).get_group(1)
    female = select_column2.groupby(['Sex']).get_group(2)"""
    labels = []
    sizes = []
    explode = []

    for size, label in dict2.items():
        labels.append(label)
        sizes.append(select_column1.groupby([col2_name]).get_group(size).count().iloc[0])
        explode.append(0.03)

    explode = tuple(explode)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


def pie2v_show(col1_name, dict1, col2_name, dict2):
    for dict1_code, dict1_description in dict1.items():
        print('{}: {}'.format(col1_name, dict1_description))
        pie2v(col1_name, dict1, col2_name, dict2, dict1_code)


# a = pie1v('Age', age)
