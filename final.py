example_input = """John is connected to Bryant, Debra, Walter. John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner. Bryant is connected to Olive, Ollie, Freda, Mercedes. Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man. Mercedes is connected to Walter, Robin, Bryant. Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures. Olive is connected to John, Ollie. Olive likes to play The Legend of Corgi, Starfleet Commander. Debra is connected to Walter, Levi, Jennie, Robin. Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords. Walter is connected to John, Levi, Bryant. Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man. Levi is connected to Ollie, John, Walter. Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma. Ollie is connected to Mercedes, Freda, Bryant. Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game. Jennie is connected to Levi, John, Freda, Robin. Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms. Robin is connected to Ollie. Robin likes to play Call of Arms, Dwarves and Swords. Freda is connected to Olive, John, Debra. Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."""


def sanitize_sentence(element, sentence):
    name = element[0:element.find(sentence) - 1].strip(' ')
    names = element[element.find(sentence):].replace(sentence, '')
    return name, names


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
    connection = "is connected to "
    games = "likes to play "
    for element in elements:
        if connection in element:
            name, names = sanitize_sentence(element, connection)
            connections_l = sanitize_names(names)
        else:
            name, names = sanitize_sentence(element, games)
            games_l = sanitize_names(names)
        if name not in network:
            network[name] = {'connections': '', 'games': ''}
        else:
            network[name]['connections'] = connections_l
            network[name]['games'] = games_l

    return network


def get_connections(network, user):
    if user in network:
        return network[user]['connections']
    return []


def add_connection(network, user_A, user_B):
    if user_A in network and user_B in network:
        network[user_A]['connections'].append(user_B)
        return network
    return False


def add_new_user(network, user, games):
    if user in network:
        network[user]['games'] = games
    else:
        network[user] = {'connections': [], 'games': games}
    return network


def get_secondary_connections(network, user):
    if user in network:
        results = []
        for u in network[user]['connections']:
            for con in network[u]['connections']:
                results.append(con)
        return list(set(results))
    return False


def connections_in_common(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    user_A_con = network[user_A]['connections']
    user_B_con = network[user_B]['connections']
    count = 0
    for connection in user_A_con:
        if connection in user_B_con:
            count += 1
    return count


def ex_path_to_friend(network, user_A, user_B, users=[]):
    if user_A not in network:
        return None
    if user_B in network[user_A]["connections"]:
        return [user_A, user_B]
    for connections in network[user_A]["connections"]:
        for con in connections:
            if user_A not in users:
                users.append(user_A)
                recursive = path_to_friend(
                    network, connections, user_B, users
                )
            if recursive is not None:
                return [user_A] + recursive
    return None


def path_to_friend(network, user_A, user_B, used=[]):
    return ex_path_to_friend(network, user_A, user_B, users=[])


net = create_data_structure(example_input)
print net
print path_to_friend(net, 'John', 'Ollie')
print get_connections(net, "Debra")
add_new_user(net, "Debra", [])
add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"])
print get_connections(net, "Mercedes")
print add_connection(net, "John", "Freda")
print get_secondary_connections(net, "Mercedes")
print connections_in_common(net, "Mercedes", "John")

