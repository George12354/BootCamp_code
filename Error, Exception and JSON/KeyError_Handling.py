facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
# try:
#     for post in facebook_posts:
#         total_likes = total_likes + post['Likes']
# except KeyError:
#     total_likes = 0
#     for post in facebook_posts:
#         for _ in post:
#             if _ == "Likes":
#                 total_likes = total_likes + post[_]

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0
        # pass
print(f"The total likes are: {total_likes}")
