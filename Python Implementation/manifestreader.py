import os

try:
    path = open("path.txt", "r").read() # Attempts to read path txt to get path
except FileNotFoundError:
    pathW = open("path.txt", "w") # If no file is found, creates a new file in write mode
    while True:
        newPath = input("Enter steamapps (e.g. C:\Program Files (x86)\Steam\steamapps) path> ") # Casts user's input as a new path
        if "steamapps" in newPath: # Flimsy valid path check
            if newPath[len(newPath) - 1] != "\\":
                newPath = newPath + "\\" # If no backslash is at the end, one is added
            pathW.write(newPath) # Writes path to path txt
            pathW.close() # Closes path txt
            path = open("path.txt", "r").read() # Reads path txt
            break
        print("Invalid path.")

# Initialises apps manifest list and steamapps contents list
steamapps = os.listdir(path)
apps = []

# Checks each file in steamapps if it is an app manifest to add to app manifest list
for x in range(len(steamapps)):
    if "appmanifest" in steamapps[x] and "tmp" not in steamapps[x]:
        apps.append(steamapps[x])

# Loops for every app manifest
for x in range(len(apps)):
    updated = True # Defaults to app being updated
    bytes_needed = None # Defaults to null bytes
    bytes_downloaded = None # Defaults to null bytes
    acf_n = path + apps[x] # Casts app manifest file path
    acf_f = open(acf_n, "r") # Opens app manifest file
    acf_l = acf_f.readlines() # Reads app manifest file
    for x in range(len(acf_l)): # Checks each line
        line = acf_l[x] # Casts line as string
        if "name" in line:
            app_name = line.split("		", -1)[1].strip() # Reads name off "name" line, casts value as string
        if "BytesToDownload" in line:
            bytes_needed = line.split("		", -1)[1] # Reads bytes to download off "BytesToDownload" line, casts value as string
        elif "BytesDownloaded" in line:
            bytes_downloaded = line.split("		", -1)[1] # Reads bytes downloaded off "BytesDownloaded" line, casts value as string
        else:
            updated = True # Resets to default if these keys aren't in file

    if bytes_needed == None and bytes_downloaded == None:
        updated = True
        print("The app", app_name, "is updated to the latest version.") # If values are default it should be updated
    elif bytes_needed == bytes_downloaded:
        updated = True
        print("The app", app_name, "is updated to the latest version.") # If all bytes have been downloaded it should be updated
    else:
        updated = False
        print("The app", app_name, "has an update.") # If all else is not true (Bytes are needed that have not been downloaded) then it has an update
    acf_f.close() # Closes app manifest file