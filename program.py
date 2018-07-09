# Program    : File Searcher App
# Author     : David Velez
# Date       : 07/09/18
# Description: Created a File Searching App that allows a user to search for a term
#              through a host of files and folders within a specified location;
#              learned through Python Training Videos from Michael Kennedy
# Source     : https://training.talkpython.fm/courses/details/python-language-jumpstart-building-10-apps

import os
import collections

# Collection of Tuples
SearchResult = collections.namedtuple("SearchResult",
                                      "file, line, text")


# Main Function
def main():
    print_header()

    # Call Function to Get Folder from the User, if no entry, print error
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location.")
        return

    # Call Function to Search for Text from User, if no text, print error
    text = get_search_text_from_user()
    if not text:
        print("We can't search for nothing!")
        return

    # Call Function to Search through Folders for Text inputted; print match results
    matches = search_folders(folder, text)
    match_count = 0
    for m in matches:
        match_count += 1
        # print(m)
        # print("---------------- MATCH ----------------")
        # print("file: " + m.file)
        # print("line: {}".format(m.line))
        # print("match: " + m.text.strip())
        # print()

    print("Found {:,} matches.".format(match_count))


# Print the Header
def print_header():
    print("-------------------------")
    print("    FILE SEARCH APP")
    print("-------------------------")
    print()


# Get Folder from User Input
def get_folder_from_user():
    folder = input("What folder do you want to search? ")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


# Get Text from User for the Search Term
def get_search_text_from_user():
    text = input("What are you searching for [single phrases only]? ")
    return text.lower()


# Search through the Folders for the Text and explore recursively through Folders
# within the Folder specified by User
def search_folders(folder, text):
    # all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            matches = search_folders(full_item, text)
            # all_matches.extend(matches)

            # for m in matches:
                # yield m
            # yield from matches
            yield from search_folders(full_item, text)
        else:
            yield from search_file(full_item, text)
            # all_matches.extend(matches)
            # for m in matches:
                # yield m

    # return all_matches


# Search through Text Files
def search_file(filename, search_text):
    # matches = []
    with open(filename, "r", encoding="utf-8") as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                yield m

        # return matches


# Main
if __name__ == "__main__":
    main()
