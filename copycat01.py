#!/usr/bin/env python3

#imports additional code
import shutil
import os


def main():

    """code to move files"""

    #move into working directory
    os.chdir("/home/student/mycode/")

    # copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copy entire DirectoryA to DirectoryB
    shutil.copytree("5g_research/", "5g_research_backup/")

    if __name__ == "__main__":
        main()

