'''
Created on Nov 11, 2018
@authors: Vincenzo Susi and Siddhanth Patel
Vincenzo CWID: 10436562
Siddhanth CWID: 10439244
usernames: vsusi and spate144
I pledge my honor that I have abided by the Stevens Honor System.
'''

pref_file = "musicrecplus.txt"

def main():
    """Main function of the file. First loads the users from the musicrecplus.txt file and then prompts
    the user for his/her name. Then, if the user is new, asks for their preferences"""
    usermap = load_users(pref_file)
    username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    if username not in usermap:
        enter_preferences(username, usermap, pref_file)
    menu(username, usermap)

def load_users(file_name):
    """Loads the users and their preferences from the text document"""
    try:
        file = open(pref_file, 'r')
    except:
        file = open(pref_file, 'w')
        usermap = {}
        file.close
        return usermap
    usermap = {}   
    for line in file:
        username, artists = line.strip().split(':')
        artists = artists.split(',')
        usermap[username] = artists
    file.close()
    return usermap

def enter_preferences(username, usermap, file_name):
    """Gets preferences from the user and then saves them. Will rewrite any preferences in the database for the user"""
    preferences = []
    new_pref = input("Enter an artist that you like (Enter to finish):")
    while new_pref != '':
        preferences.append(new_pref)
        new_pref = input("Enter an artist that you like (Enter to finish):")
    preferences.sort()
    save(username, usermap, file_name, preferences)
    
def save(username, usermap, file_name, prefs):
    """Saves the users and their preferences to the text document"""
    usermap[username] = prefs
    file = open(file_name, 'w')
    new_user_list = []
    for username in usermap:
        new_user_list.append(username)
        new_user_list.sort()
    for user in new_user_list:
        new_line = str(user) + ':' + ','.join(usermap[user]) + '\n'
        file.write(new_line)
    file.close
    
def menu(username, usermap):
    """Function for the menu of the program. Prints the menu and then proceeds based on the users choice"""
    while True:
        print('Enter a letter to choose an option:' + '\n' +
            'e - Enter preferences' + '\n' + 
            'r - Get recommendations' + '\n' +
            'p - Show most popular artists' + '\n' +
            'h - How popular is the most popular' +'\n' +
            'm - Which user has the most likes' + '\n' + 
            'q - Save and quit')
        choice = input()
        if choice == 'e':
            enter_preferences(username, usermap, pref_file)
        elif choice == 'r':
            recs = get_recs(username, usermap)
            print_recs(recs, username)
            prefs = usermap[username]
            save(username, usermap, pref_file, prefs)
        elif choice == 'p':
            best_artists(usermap)
        elif choice == 'h':
            how_artists(usermap)
        elif choice == 'm':
            most_likes(usermap)
        elif choice == 'q':
            try:
                save(username, usermap, pref_file, usermap[username])
                break
            except:
                break  

def num_matches(list1, list2):
    """Returns the number of elements that the two lists have in common"""
    list1.sort()
    list2.sort()
    matches = i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def drop_matches(list1, list2):
    """Returns a new list that contains only the elements in list 2
    that are not in list 1"""
    list1.sort()
    list2.sort()
    i = j = 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result

def remove_duplicates(lst):
    """Creates a new list without any duplicates"""
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

def get_recs(username, usermap):
    """Returns a list of artist recommendations for the user""" 
    users = usermap.keys()
    best_users = []
    best_score = 0
    for user in users:
        if user[-1] == '$':
            continue
        if usermap[user] == ['']:
            continue
        if usermap[user] != usermap[username]:
            current_prefs = usermap[user]
            main_prefs = usermap[username]
            matches = num_matches(current_prefs, main_prefs)
            if matches > best_score:
                best_score = matches
                best_users = [user]
            elif matches == best_score:
                best_users.append(user)
    new_list = []
    for user in best_users:
        new_list = new_list + drop_matches(usermap[username], usermap[user])
    rec_list = remove_duplicates(new_list)
    rec_list.sort()
    return rec_list

def print_recs(recs, username):
    """Prints each artist from the list of recommendations"""
    if len(recs) == 0:
        print('No recommendations available at this time')
    else:
        for artist in recs:
            print(artist)
            
def count_occurences(artist, lst):
    """Counts how many times an artist occurs in a list"""
    count = 0
    for artist_name in lst:
        if artist == artist_name:
            count += 1
    return count
 
def best_artists(usermap):
    """Returns the artist that is liked by the most users. If there is a tie, prints all artists
    with the most likes"""
    all_artists = []
    users = usermap.keys()
    for user in users:
        if user[-1] == '$':
            continue
        if usermap[user] == ['']:
            continue
        all_artists = all_artists + usermap[user]
    all_artists.sort()
    top_likes = 0
    top_artist = []
    for artist in all_artists:
        likes = count_occurences(artist, all_artists) 
        if likes > top_likes:
            top_likes = likes
            top_artist = [artist]
        elif likes == top_likes:
            top_artist.append(artist)
    top_artist.sort()
    best_artist = remove_duplicates(top_artist)
    if len(best_artist) == 0:
        print('Sorry, no artists found')
    else: 
        for artist in best_artist:
            print(artist)
                
def how_artists(usermap):
    """Prints the number of likes the most popular artist received"""
    all_artists = []
    users = usermap.keys()
    for user in users:
        if user[-1] == '$':
            continue
        if usermap[user] == ['']:
            continue
        all_artists = all_artists + usermap[user]
    all_artists.sort()
    top_likes = 0
    for artist in all_artists:
        likes = count_occurences(artist, all_artists) 
        if likes > top_likes:
            top_likes = likes
    if top_likes == 0:
        print('Sorry, no artists found')
    else: 
        print(top_likes)

def most_likes(usermap):
    """Prints the name(s) of the user(s) who likes the most artists"""
    users = usermap.keys()
    top_prefs = 0
    best_users = []
    for user in users:
        if user[-1] == '$':
            continue
        if usermap[user] == ['']:
            continue
        if len(usermap[user]) > top_prefs:
            top_prefs = len(usermap[user])
            best_users = [user]
        elif len(usermap[user]) == top_prefs:
            best_users.append(user)
    most_likes_users = remove_duplicates(best_users)
    if top_prefs == 0 or len(most_likes_users) == 0:
        print('Sorry, no user found')
    else:
        for user in most_likes_users:
            print(user)
    
if __name__ == '__main__':
    main()
    