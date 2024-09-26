# Ficher de .txt à une array de données#
#Auteur : Philippe Arsenault
# Fonction solo qui prend un path et qui retourne les données dans un array

def get_data_txt(file_path):

    # Initialize a list to hold the data
    data = []
    error_counter =0

    # Open the file and read its contents
    with open(file_path, 'r') as file:
        for line in file:
            # Strip whitespace and split the line by tab characters
            parts = line.strip().split('\t')
            # Convert the string parts to a tuple of float values
            if len(parts) == 2:  # Ensure there are exactly two values
                try:
                    value1 = float(parts[0].replace(',', '.'))  # Convert to float, replace comma with dot
                    value2 = float(parts[1].replace(',', '.'))  # Convert to float, replace comma with dot
                    data.append((value1, value2))  # Append the tuple to the list
                except ValueError:
                    #print(f"Error converting line: {line.strip()}")
                    error_counter += 1
    # Now `data` contains the processed values
    # data a deux dimensions, data[0][0] va chercher la première valeur x et data[0][1] va chercher sa valeur y correspondante
    return data