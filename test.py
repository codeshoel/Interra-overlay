import os
import subprocess
from pydub import AudioSegment
# path = os.path


my_files = []
peers_parent = []
peers = []

# index[13]
for file_in_dir in os.scandir("dir_st"):
    peers_parent.append(file_in_dir.name)


for idx in range(len(peers_parent)):
    if (peers_parent[idx] not in peers) and (len(peers) < 2):
        peers.append(peers_parent[idx])

        # if str(peers_parent[idx]).startswith(peers_parent[idx][0:13]) == str(peers[0]).startswith(str(peers[0][0:13])):
        #     print("parent:",peers_parent[idx][-13:-1])
        #     print("child:",peers[0][-13:-1])
        #     if str(peers_parent[idx]).endswith(peers_parent[idx][-13:-1]) != str(peers[0]).endswith(peers[0][-13:-1]):
        #         print("there are not the same..", peers[0][-13:-1])



print(peers)






            # print(peers_parent[idx] != peers[0])
            # peers.append(peers_parent[idx])
            # my_files.append(peers)
            # print(True)

            # pass
            # print(peers[peers_idex])
            # if str(peers_parent[idx]).startswith(peers_parent[idx][0:13]) == str(peers[peers_idex]).startswith(str(peers[peers_idex][0:13])) and str(peers_parent[idx]).endswith(peers_parent[idx][-13:-1]) != str(peers[0]).startswith(str(peers[peers_idex][-13:-1])):
                # peers.append(peers_parent[idx])









    # my_files.append(peers)
    # print("unique:", file.name[-13:-1])



# OMG
    # if (file.name not in peers) and (len(peers) < 2):
    #     peers.append(file.name)
    #     for i in range(len(peers)):
    #         print(peers[i])




            # if file.name.startswith(file.name[0:13]) == str(peers[0]).startswith(str(peers[0][0:13])) and file.name.endswith(file.name[-13:-1]) != str(peers[0]).startswith(str(peers[0][-13:-1])):
            #     pass
        #     peers.append(file.name)
        #     my_files.append(peers)
        #     print("peered...")

# print(my_files)





# if (os.path.isfile(audio_1) or os.path.isfile(audio_2)):
#     os.remove("./{:s}/{:s}".format(dir, audio_1))
#     os.remove("./{:s}/{:s}".format(dir, audio_2))
# else:
#     print("No such file in specified dir.")






