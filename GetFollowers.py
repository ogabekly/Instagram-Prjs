import instaloader
L = instaloader.Instaloader()
L.interactive_login('@username') 
 
profile = instaloader.Profile.from_username(L.context, "username")

# get_followers()
# get_followees()
for followee in profile.get_followers():
    username = followee.username
    print(username)
    # print(followee)
    
    
    




