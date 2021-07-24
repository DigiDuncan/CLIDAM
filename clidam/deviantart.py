import deviantart

with open("_CLIENT_SECRET.txt") as f:
    CLIENT_SECRET = f.readline().strip()

# Log in to DA
da = deviantart.Api("11505", CLIENT_SECRET)
