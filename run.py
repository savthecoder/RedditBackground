import sys
import redditbackground

subredditName = sys.argv[1]

print("Setting your background as the top image of /r/" + subredditName + "...")

while True :
    print("Do you want to save the image (y/n) :")
    save = input()
    if save == "y" or save == "n" :
        image = redditbackground.setBackgroundFromSubreddit(subredditName,save)
        print("Done!")
        print("===== Image Details =====")
        print("Title: " + image["title"])
        exit()
    else:
        print("Error wrong input !!!\n######### Do you wanna 'continue' or 'exit' #########")
        save = input()
        if save == "exit" :
            exit()



