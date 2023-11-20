def roman_to_int(num: str) -> int:
    roman_numbers = {
        'I': 1,
        'II': 2,
        'III': 3,
        'IV': 4,
        'V': 5
    }
    return roman_numbers[num]

def champion_by_lane(lane):
    position = {
        'support': ['Galio', 'Poppy', 'Zac', 'Shen', 'Heimerdinger', 'Veigar', 'Ziggs', 'Twitch', 'Ashe', 'Miss Fortune', 'Teemo', 'Gragas', "Cho'Gath", 'Anivia', 'Annie', 'LeBlanc', 'Lissandra', 'Neeko', 'Zoe', 'Amumu', 'Fiddlesticks', 'Ivern', 'Nidalee', 'Tahm Kench', 'Seraphine', 'Swain', 'Zilean', 'Brand', 'Morgana', 'Malphite', 'Pantheon', 'Lux', "Vel'Koz", 'Xerath', 'Rell', 'Maokai', 'Shaco', 'Alistar', 'Bard', 'Blitzcrank', 'Braum', 'Janna', 'Karma', 'Leona', 'Lulu', 'Milio', 'Nami', 'Nautilus', 'Pyke', 'Rakan', 'Renata Glasc', 'Senna', 'Sett', 'Sona', 'Soraka', 'Taric', 'Thresh', 'Yuumi', 'Zyra'],
        'adc': ['Cassiopeia', 'Tahm Kench', 'Karthus', 'Heimerdinger', 'Akshan', 'Corki', 'Veigar', 'Lucian', "Kog'Maw", 'Seraphine', 'Tristana', 'Ziggs', 'Swain', 'Yasuo', 'Twitch', 'Aphelios', 'Ashe', 'Caitlyn', 'Draven', 'Ezreal', 'Jhin', 'Jinx', "Kai'Sa", 'Kalista', 'Miss Fortune', 'Nilah', 'Samira', 'Sivir', 'Varus', 'Vayne', 'Xayah', 'Zeri'],
        'mid': ['Nunu & Willump', 'Garen', 'Kled', 'Lucian', 'Zilean', 'Brand', 'Morgana', 'Singed', 'Teemo', 'Tryndamere', 'Gragas', 'Karthus', 'Xin Zhao', 'Gangplank', 'Heimerdinger', "K'Sante", 'Kayle', 'Kennen', "Kog'Maw", 'Nasus', 'Quinn', 'Riven', 'Seraphine', 'Tristana', 'Ziggs', "Cho'Gath", 'Malphite', 'Pantheon', 'Qiyana', 'Rumble', 'Sylas', 'Talon', 'Zed', 'Diana', 'Ekko', 'Taliyah', 'Ahri', 'Akali', 'Akshan', 'Anivia', 'Annie', 'Aurelion Sol', 'Azir', 'Cassiopeia', 'Corki', 'Fizz', 'Galio', 'Irelia', 'Jayce', 'Kassadin', 'Katarina', 'LeBlanc', 'Lissandra', 'Lux', 'Malzahar', 'Naafiri', 'Neeko', 'Orianna', 'Renekton', 'Ryze', 'Swain', 'Syndra', 'Twisted Fate', 'Veigar', "Vel'Koz", 'Vex', 'Viktor', 'Vladimir', 'Xerath', 'Yasuo', 'Yone', 'Zoe'],
        'jungla': ['Dr. Mundo', 'Olaf', 'Brand', "Cho'Gath", 'Gwen', 'Malphite', 'Malphite', 'Moderkaiser', 'Morgana', 'Pantheon', 'Qiyana', 'Rell', 'Rumble', 'Singed', 'Sylas', 'Talon', 'Teemo', 'Tryndamere', 'Twitch', 'Zed', 'Amumu', "Bel'Veth", 'Briar', 'Diana', 'Ekko', 'Elise', 'Evelynn', 'Fiddlesticks', 'Gragas', 'Graves', 'Hecarim', 'Ivern', 'Jarvan IV', 'Jax', 'Karthus', 'Kayn', "Kha'Zix", 'Kindred', 'Lee Sin', 'Lillia', 'Maokai', 'Master Yi', 'Nidalee', 'Nocturne', 'Nunu & Willump', 'Poppy', 'Rammus', "Rek'Sai", 'Rengar', 'Sejuani', 'Shaco', 'Shyvana', 'Skarner', 'Taliyah', 'Trundle', 'Udyr', 'Vi', 'Viego', 'Volibear', 'Warwick', 'Wukong', 'Xin Zhao', 'Zac'],
        'top': ['Aatrox','Akali', 'Akshan', 'Briar', 'Camille', 'Cassiopeia', "Cho'Gath", 'Darius', 'Dr. Mundo', 'Fiora', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Heimerdinger', 'Illaoi', 'Irelia', 'Jax', 'Jayce', "K'Sante", 'Kalista', 'Kayle', 'Kennen', 'Kled', 'Lillia', 'Malphite', 'Malzahar', 'Maokai', 'Mordekaiser', 'Naafiri', 'Nasus', 'Olaf', 'Ornn', 'Pantheon', 'Poppy', 'Quinn', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Sett', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Skarner', 'Swain', 'Sylas', 'Tahm Kench', 'Teemo', 'Trundle', 'Tryndamere', 'Udyr', 'Urgot', 'Vayne', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick', 'Zac']
    }

    lane = lane.lower()

    if lane in position:
        return position[lane]
    else:
        return "Te has equivocao poniendo la linea"
