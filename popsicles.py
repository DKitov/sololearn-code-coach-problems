siblings = int(input())
popsicles = int(input())
# check if you can give even number of popsicles to each sibling

if popsicles % siblings == 0:
    print("give away")
# else eat the popsicles by yourself

else:
    print("eat them yourself")
