# import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

regions = {'E12000001': 'North East', 'E12000002': 'North West',
           'E12000003': 'Yorkshire and the Humber', 'E12000004': 'East Midlands',
           'E12000005': 'West Midlands', 'E12000009': 'South West',
           'E12000006': 'East of England', 'E12000008': 'South East',
           'E12000007': 'London', 'W92000004': 'Wales'}

residence_type = {'H': 'Not resident in a \ncommunal establishment',
                  "C": 'Resident in a \ncommunal establishment'}

family_composition = {-9: 'No code required', 1: 'Not in a family',
                      2: 'Married/same-sex \ncivil partnership couple family',
                      3: 'Cohabiting couple family', 4: 'Lone parent family \n(male head)',
                      5: 'Lone parent family \n(female head)', 6: 'Other related family'}

population_base = {1: 'Usual resident',
                   2: 'Student living away from home \nduring term-time',
                   3: 'Short-term resident'}

sex = {1: 'Male', 2: 'Female'}

age = {1: '0 to 15', 2: '16 to 24', 3: '15 to 34', 4: '45 to 44', 5: '45 to 54',
       6: '55 to 64', 7: '65 to 74',
       8: '75 and over'}

marital_status = {1: 'Single', 2: 'Married', 3: 'Separated but \nstill legally married',
                  4: 'Divorced ', 5: 'Widowed'}

student = {1: 'Student', 2: 'No Student'}

country_of_birth = {-9: 'No code required', 1: 'UK', 2: 'Non UK'}

health = {-9: 'No code required', 1: 'Very good health', 2: 'Good health',
          3: 'Fair health', 4: 'Bad health', 5: 'Very bad health'}

ethnic_group = {-9: 'No code required', 1: 'White', 2: 'Mixed',
                3: 'Asian and \nAsian British', 4: 'Black or \nBlack British',
                5: 'Chinese or Other ethnic group'}

religion = {-9: 'No code required', 1: 'No religion', 2: 'Christian', 3: 'Buddhist',
            4: 'Hindu', 5: 'Jewish', 6: 'Muslim', 7: 'Sikh', 8: 'Other religion',
            9: 'Not stated'}

economic_activity = {-9: 'No code required', 1: 'Economically active: \nEmployee',
                     2: 'Economically active: \nSelf-employed',
                     3: 'Economically active: \nUnemployed',
                     4: 'Economically active: \nFull-time student',
                     5: 'Economically inactive: \nRetired',
                     6: 'Economically inactive: \nStudent',
                     7: 'Economically inactive: \nLooking after home or family',
                     8: 'Economically inactive: \nLong-term sick or disabled',
                     9: 'Economically inactive: \nOther'}

occupation = {-9: 'No code required', 1: 'Managers, Directors \nand Senior Officials',
              2: 'Professional Occupations',
              3: 'Associate Professional \nand Technical Occupations',
              4: 'Administrative and \nSecretarial Occupations',
              5: 'Skilled Trades \nOccupations',
              6: 'Caring, Leisure and \nOther Service Occupations',
              7: 'Sales and Customer \nService Occupations',
              8: 'Process, Plant and \nMachine Operatives', 9: 'Elementary Occupations'}

industry = {-9: 'No code required', 1: 'Agriculture, forestry \nand fishing',
            2: 'Mining and quarrying; \nManufacturing;', 3: 'Construction',
            4: 'Wholesale and retail trade; Repair \nof motor vehicles and motorcycles',
            5: 'Accommodation and food service', 6: 'Transport and storage',
            7: 'Financial and insurance', 8: 'Real estate',
            9: 'Public administration and defence', 10: 'Education',
            11: 'Human health and \nsocial work activities',
            12: 'Other community, \nsocial and personal service activities'}

hw_per_week = {-9: 'No code required', 1: 'Part-time: \n15 or less h.w.',
               2: 'Part-time: \n16 to 30 hw', 3: 'Full-time: \n31 to 48 hw',
               4: 'Full-time: \n49 or more hw'}

approx_social_grade = {-9: 'No code required', 1: 'AB', 2: 'C1', 3: 'C2', 4: 'DE'}

colors = ["black", "#ff692e", "#2e5cff", "#ffd12e", "#ff2e5c", "#5cff2e", "#ff0000",
          "#8b4513", "#ff7f50", "#ffff80", '#9370db', '#ff581a', '#c75757']


def freq_graph(figS, col_name, my_data, dictionary, Title, rotation, ha, pictName):
    """
    :param figS: tuple with the figures aspect
    :param col_name: the attribute name
    :param my_data: the data frame
    :param dictionary: the name of the dictionary of the attribute
    :param Title: the graph's title
    :param rotation: the rotation of the get_xticklabels
    :param ha: the position of the get_xticklabels
    :param pictName: saving the graph by the name of the value of this parameter
    :return: a countplot of the col_name's frequencies
    """

    # creating the figure
    plt.figure(figsize=figS)
    sns.set_style('whitegrid')
    # choosing the colors
    this_palette = []
    for i in range(0, len(dictionary)):
        this_palette.append(colors[i])

    # inserting the data of the graph
    ax = sns.countplot(x=col_name, data=my_data, palette=this_palette)

    # inserting the Title and the axis descriptions
    ax.set_xlabel(col_name, size=20, fontweight='bold')
    ax.set_ylabel('Number of occurrences', size=20, fontweight='bold')
    ax.set_title(Title, size=30, fontweight='bold')

    # Altering the x axis labels values' names
    ax.set_xticklabels(tuple(dictionary.values()))

    plt.setp(ax.get_xticklabels(), rotation=rotation, ha=ha, size=11)

    plt.tight_layout()
    sns.despine()

    plt.savefig(pictName)
