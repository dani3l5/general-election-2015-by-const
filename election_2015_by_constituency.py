import matplotlib.pyplot as plt

def graph_data(const='North East Bedfordshire'):
    fig = plt.figure()
    fig.subplots_adjust(right=0.87)

    source_code = open("data/general_election_results_2015.csv", "r")
    split_source = source_code.read().split('\n')
    commas = 0
    num_reached = False
    name_reached = False
    str_votes = ''
    str_parties = ''
    for line in split_source:
        if '"' in line:
            line.replace('"', '')
            is_split = True
        else:
            is_split = False
        if const in line and not is_split:
            for char in line:
                if num_reached:
                    str_votes += char
                if char == ',':
                    commas += 1
                if commas == 14:
                    num_reached = True
                else:
                    num_reached = False
            commas = 0
            for char in line:
                if name_reached:
                    str_parties += char
                if char == ',':
                    commas += 1
                if commas ==  7:
                    name_reached = True
                else:
                    name_reached = False
            commas = 0
        elif const in line and is_split:
            for char in line:
                if num_reached:
                    str_votes += char
                if char == ',':
                    commas += 1
                if commas == 15:
                    num_reached = True
                else:
                    num_reached = False
            commas = 0
            for char in line:
                if name_reached:
                    str_parties += char
                if char == ',':
                    commas += 1
                if commas ==  8:
                    name_reached = True
                else:
                    name_reached = False
            commas = 0

    str_votes = str_votes.replace('/', '')
    if str_votes == '' or str_parties == '':
        print("Constituency Not Found!")

    split_votes = str_votes.split(',')
    split_votes.remove('')
    votes = []
    for item in split_votes:
        votes.append(int(item))

    parties = str_parties.split(',')
    parties.remove('')

    colours = []

    for party in parties:
        if party == "Conservative":
            colours.append('b')
        elif party == "Labour" or party == "Labour and Co-operative":
            colours.append('r')
        elif party == "Liberal Democrat":
            colours.append('#FFC200')
        elif party == "Scottish National Party":
            colours.append('#ffff00')
        elif party == "UK Independence Party":
            colours.append('#660066')
        elif party == "Green":
            colours.append('#00ff00')
        elif party == "Plaid Cymru":
            colours.append("#006600")
        else:
            colours.append("#666666")

    plt.pie(votes, labels=parties, colors=colours, autopct='%1.1f%%')

    plt.title(const)

    plt.show()

print("Does NOT Work With Constituency Names That Are In Other Constiuency Names (ie. Bedford)!")
constituency = input("Constituency: ")
if constituency != '':
    graph_data(constituency)
else:
    graph_data()