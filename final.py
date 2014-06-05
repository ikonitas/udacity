example_input = """John is connected to Bryant, Debra, Walter. John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner. Bryant is connected to Olive, Ollie, Freda, Mercedes. Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man. Mercedes is connected to Walter, Robin, Bryant. Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures. Olive is connected to John, Ollie. Olive likes to play The Legend of Corgi, Starfleet Commander. Debra is connected to Walter, Levi, Jennie, Robin. Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords. Walter is connected to John, Levi, Bryant. Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man. Levi is connected to Ollie, John, Walter. Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma. Ollie is connected to Mercedes, Freda, Bryant. Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game. Jennie is connected to Levi, John, Freda, Robin. Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms. Robin is connected to Ollie. Robin likes to play Call of Arms, Dwarves and Swords. Freda is connected to Olive, John, Debra. Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."""


def sanitize_names(names):
    names = names.replace('.', '')
    return names.split(', ')


def create_data_structure(string_input):
    network = {}
    elements = []
    start = 0
    end = string_input.find('.')
    while end != -1:
        elements.append(string_input[start:end + 1])
        start = end + 1
        end = string_input.find('.', start)
        start += 1
    connection = "is connected to "
    games = "likes to play "
    for element in elements:
        if connection in element:
            name = element[0:element.find(connection) - 1]
            names = element[element.find(connection):].replace(connection, '')
            connections_l = sanitize_names(names)
        else:
            name = element[0:element.find(games) - 1]
            names = element[element.find(games):].replace(games, '')
            games_l = sanitize_names(names)
        if name not in network:
            network[name] = {'connections': '', 'games': ''}
        else:
            network[name]['connections'] = connections_l
            network[name]['games'] = games_l

    return network


def get_connections(network, user):
    return []


def add_connection(network, user_A, user_B):
    return network


def add_new_user(network, user, games):
    return network


def get_secondary_connections(network, user):
    return []


def connections_in_common(network, user_A, user_B):
    return 0


def path_to_friend(network, user_A, user_B):
    # your RECURSIVE solution here!
    return None

#net = create_data_structure(example_input)
#print net
#print path_to_friend(net, 'John', 'Ollie')
#print get_connections(net, "Debra")
#print add_new_user(net, "Debra", [])
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_connections(net, "Mercedes")
#print add_connection(net, "John", "Freda")
#print get_secondary_connections(net, "Mercedes")
#print connections_in_common(net, "Mercedes", "John")

