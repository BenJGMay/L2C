users = {}
users['Kim'] = {'email' : 'kim@oreilly.com', 'gender': 'f', 'age': 27, 'friends': ['John', 'Josh']}
users['John'] = {'email' : 'john@abc.com', 'gender': 'm', 'age': 24, 'friends': ['Kim', 'Josh']}
users['Josh'] = {'email' : 'josh@wickedlysmart.com', 'gender': 'm', 'age': 32, 'friends': ['Kim']}

def average_age(name):
    user = (users[name])
    friends = []
    total_friend_ages = 0
    for friend in (user['friends']):
        friends.append(friend)
        friend_name = (users[friend])
        friend_age = friend_name['age']
        total_friend_ages += friend_age

    average_age = total_friend_ages / len(friends)

    print(name + "'s friends have an average age of", average_age)

average_age('Kim')
average_age('John')
average_age('Josh')
