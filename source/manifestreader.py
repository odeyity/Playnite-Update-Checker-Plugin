import os
import json

roaming = os.getenv('APPDATA')
current_directory = os.getcwd()

#config_path = roaming + "\\Playnite\\ExtensionsData\\74fe180c-7038-4908-bec1-94194b73b2e4\\config.json"

# Define the two paths
config_path_1 = os.path.join(roaming, "Playnite", "ExtensionsData", "74fe180c-7038-4908-bec1-94194b73b2e4", "config.json")
config_path_2 = os.path.abspath(os.path.join(current_directory, "..", "Playnite", "ExtensionsData", "74fe180c-7038-4908-bec1-94194b73b2e4", "config.json"))

print(config_path_1);
print(config_path_2);

# Check which path exists
if os.path.exists(config_path_1):
    config_path = config_path_1
elif os.path.exists(config_path_2):
    config_path = config_path_2
else:
    raise FileNotFoundError("Neither path exists.")
    
path = open(config_path, "r") # Attempts to read path txt to get path
pathJ = json.load(path)
updateNotice = False

try:
    enableSteam = pathJ["EnableSteam"]
except KeyError:
    enableSteam = True

try:
    enableEpic = pathJ["EnableEpic"]
except KeyError:
    enableEpic = True

if enableSteam == True:

    pathNum = 1
    steamPath = pathJ["SteamPath"]
    steamPath2 = pathJ["SteamPath2"]
    steamPath3 = pathJ["SteamPath3"]
    steamPath4 = pathJ["SteamPath4"]
    steamPath5 = pathJ["SteamPath5"]
    if steamPath5 != "":
        pathNum = 5
    elif steamPath4 != "":
        pathNum = 4
    elif steamPath3 != "":
        pathNum = 3
    elif steamPath2 != "":
        pathNum = 2


    # Steam
    print("--------")
    print("Steam:")
    print("--------")
    print()

    if steamPath == "":
        print("Set up steamapps path in the addon settings.")
    elif "steamapps" not in steamPath:
        print("Invalid steamapps path.")
    else:
        for x in range(pathNum):
            pathNum = pathNum - x
            if pathNum == 5:
                steamPath = steamPath5
            elif pathNum == 4:
                steamPath = steamPath4
            elif pathNum == 3:
                steamPath = steamPath3
            elif pathNum == 2:
                steamPath = steamPath2
            elif pathNum == 1:
                steamPath = pathJ["SteamPath"]
            if steamPath[len(steamPath) - 1] != "/":
                steamPath = steamPath + "/"
            # Initialises apps manifest list and steamapps contents list
            steamapps = os.listdir(steamPath)
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
                acf_n = steamPath + apps[x] # Casts app manifest file path
		    
                # Attempts Unicode encoding, fallback to CP-1252
            	try:
                	acf_f = open(acf_n, "r", encoding="utf-8") # Opens app manifest file
            	except UnicodeDecodeError:
                	acf_f = open(acf_n, "r", encoding="cp1252")
			
                acf_l = acf_f.readlines() # Reads app manifest file
                for x in range(len(acf_l)): # Checks each line
                    line = acf_l[x] # Casts line as string
                    if "name" in line:
                        app_name = line.replace("			", "").split("		", -1)[1].strip().replace("â„¢", "™") # Reads name off "name" line, casts value as string
                        
                    if "BytesToDownload" in line:
                        bytes_needed = line.replace("			", "").split("		", -1)[1] # Reads bytes to download off "BytesToDownload" line, casts value as string
                    elif "BytesDownloaded" in line:
                        bytes_downloaded = line.replace("			", "").split("		", -1)[1] # Reads bytes downloaded off "BytesDownloaded" line, casts value as string
                    else:
                        updated = True # Resets to default if these keys aren't in file

                if bytes_needed == None and bytes_downloaded == None:
                    updated = True
                elif bytes_needed == bytes_downloaded:
                    updated = True
                else:
                    updated = False

                    # Converts ripped string from appmanifest to a float value
                    bytes_downloaded = bytes_downloaded.replace('"', "")
                    bytes_downloaded = float(bytes_downloaded.replace("\n", ""))

                    bytes_needed = bytes_needed.replace('"', "")
                    bytes_needed = float(bytes_needed.replace("\n", ""))

                    # Detects if bytes are big enough to be 1 GB, 1 MB or 1 KB
                    if bytes_needed >= 1000000000:
                        bytes_needed = str(f"{float(bytes_needed) / 1000000000:.2f}") + " GB" # Rounds to 2dp
                    elif bytes_needed >= 1000000 and bytes_needed < 1000000000:
                        bytes_needed = str(f"{float(bytes_needed) / 1000000:.2f}") + " MB"
                    else:
                        bytes_needed = str(f"{float(bytes_needed) / 1000:.2f}") + " KB"

                    if bytes_downloaded >= 1000000000:
                        bytes_downloaded = str(f"{float(bytes_downloaded) / 1000000000:.2f}") + " GB"
                    elif bytes_downloaded >= 1000000 and bytes_downloaded < 1000000000:
                        bytes_downloaded = str(f"{float(bytes_downloaded) / 1000000:.2f}") + " MB"
                    else:
                        bytes_downloaded = str(f"{float(bytes_downloaded) / 1000:.2f}") + " KB"
                    
                    
                    print("The app", app_name, "has an update. (" + bytes_downloaded + " / " + bytes_needed + ")")
                    updateNotice = True
                acf_f.close() # Closes app manifest file
if updateNotice == False:
	print("All Steam games are updated to the latest version.")
else:
	print("Steam game updates found in progress or awaiting download.")
if enableEpic == True:
    updateNotice = False
    # Epic Games
    print()
    print("-------------")
    print("Epic Games:")
    print("-------------")
    print()
    
    if os.path.exists("C:\\ProgramData\\Epic\\EpicGamesLauncher\\Data\\Manifests\\") == True:
        bytes_needed = None # Defaults to null bytes
        bytes_downloaded = None # Defaults to null bytes

        if os.path.exists("C:\\ProgramData\\Epic\\EpicGamesLauncher\\Data\\Manifests\\") == True:
            updated = False

            epic_path = "C:\\ProgramData\\Epic\\EpicGamesLauncher\\Data\\Manifests\\"
            epic_path_pending = "C:\\ProgramData\\Epic\\EpicGamesLauncher\\Data\\Manifests\\Pending\\"
            epic_m = os.listdir(epic_path)
            epic_p = os.listdir(epic_path_pending)

            epic_apps = []
            epic_apps_date = []

            for x in range(len(epic_m)):
                if epic_m[x] == "Pending":
                    pass 
                else:
                    epic_n = epic_path + epic_m[x] # Casts app manifest file epic_path
                    epic_f = open(epic_n, "r") # Opens app manifest file
                    epic_l = epic_f.readlines() # Reads app manifest file
                try:
                    epic_l
                except NameError:
                    print("No games to check.");
                else:
                    for x in range(len(epic_l)): # Checks each line
                        line = epic_l[x] # Casts line as string
                        if "DisplayName" in line:
                            app_name = line.split(": ", -1)[1].strip().replace(",", "").replace("Â", "") # Reads name off "name" line, casts value as string
                            break
                    epic_date = float(os.path.getmtime(epic_n))
                    if app_name in epic_apps:
                        order = epic_apps.index(app_name)
                        if epic_apps_date[order] < epic_date:
                            del epic_apps_date[order]
                            del epic_apps[order]
                        else:
                            epic_apps.append(app_name)
                            epic_apps_date.append(epic_date)
                    else:
                        epic_apps.append(app_name)
                        epic_apps_date.append(epic_date)

                    for x in range(len(epic_p)):
                        if epic_m[x] == "Pending":
                            pass 
                        else:
                            epic_n = epic_path_pending + epic_p[x] # Casts app manifest file epic_path
                            epic_f = open(epic_n, "r") # Opens app manifest file
                            epic_l = epic_f.readlines() # Reads app manifest file
                        for x in range(len(epic_l)): # Checks each line
                            line = epic_l[x] # Casts line as string
                            if "DisplayName" in line:
                                app_name = line.split(": ", -1)[1].strip().replace(",", "").replace("Â", "") # Reads name off "name" line, casts value as string
                            elif "StagingLocation" in line:
                                install_loc = line.split(": ", -1)[1].strip().replace(",", "").replace("\\\\", "\\").replace("/", "\\").replace('"', '')
                                if os.path.exists(install_loc) == True:
                                    def dir_size(path='.'):
                                        bytes = 0
                                        with os.scandir(path) as it:
                                            for tmp in it:
                                                if tmp.is_file():
                                                    bytes += tmp.stat().st_size
                                                elif tmp.is_dir():
                                                    bytes += dir_size(tmp.path)
                                        return bytes

                                    bytes_downloaded = float(dir_size(install_loc))
                            elif "InstallSize" in line:
                                bytes_needed = float(line.split(": ", -1)[1].strip().replace(",", "").replace('"', ''))

                        epic_date = float(os.path.getmtime(epic_n))
                        if app_name in epic_apps:
                            order = epic_apps.index(app_name)
                            if epic_apps_date[order] < epic_date:
                                updated = False
                                if bytes_needed == None:
                                    updated = True
                                else:
                                    if bytes_needed >= 1000000000:
                                        bytes_needed = str(f"{float(bytes_needed) / 1000000000:.2f}") + " GB" # Rounds to 2dp
                                    elif bytes_needed >= 1000000 and bytes_needed < 1000000000:
                                        bytes_needed = str(f"{float(bytes_needed) / 1000000:.2f}") + " MB"
                                    else:
                                        bytes_needed = str(f"{float(bytes_needed) / 1000:.2f}") + " KB"
                                
                                if bytes_downloaded == None:
                                    updated = True
                                else:
                                    if bytes_downloaded >= 1000000000:
                                        bytes_downloaded = str(f"{float(bytes_downloaded) / 1000000000:.2f}") + " GB"
                                    elif bytes_downloaded >= 1000000 and bytes_downloaded < 1000000000:
                                        bytes_downloaded = str(f"{float(bytes_downloaded) / 1000000:.2f}") + " MB"
                                    else:
                                        bytes_downloaded = str(f"{float(bytes_downloaded) / 1000:.2f}") + " KB"
                                    print("The app", app_name, "has an update. (" + bytes_downloaded + " / " + bytes_needed + ")")
	
    if updateNotice == False:
        print("All Epic games are updated to the latest version.")
    else:
	    print("Epic game updates found in progress or awaiting download.")
print()
print()
input("Press any key to exit.")
