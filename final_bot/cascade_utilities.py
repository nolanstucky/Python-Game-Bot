import os



def generateNegativeDescriptionFile():

    with open('negative.txt', 'w') as f:

        for filename in os.listdir('negative_matches'):
            f.write('negative/' + filename + '\n')