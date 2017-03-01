####
# This script demonstrates how to use the Tableau Server Client
# to interact with workbooks. It explores the different
# functions that the Server API supports on workbooks.
#
# With no flags set, this sample will query all workbooks,
# pick one workbook and populate its connections/views, and update
# the workbook. Adding flags will demonstrate the specific feature
# on top of the general operations.
####

import getpass
import logging
import os.path

import tableauserverclient as TSC


def main():

    url = "<SERVER URL>"
    username = "<DOMAIN IF APPLICABLE>" + getpass.getuser()
    #password = getpass.getpass("Password: ")
    password = "<PASSWORD>"
    path = "DIRECTORY PATH"

    # Set logging level based on user input, or error by default
    #logging_level = getattr(logging, args.logging_level.upper())
    #logging.basicConfig(level=logging_level)

    # SIGN IN
    tableau_auth = TSC.TableauAuth(username, password)
    server = TSC.Server(url)

    with server.auth.sign_in(tableau_auth):

        # Gets all project items 
        all_projects, pagination_item = server.projects.get()
        print("\nThere are {} projects on site: ".format(pagination_item.total_available))
        print([project.id for project in all_projects])
        print([project.name for project in all_projects])


        # Gets all workbook items
        all_workbooks, pagination_item = server.workbooks.get()
        print("\nThere are {} workbooks on site: ".format(pagination_item.total_available))
        print([workbook.id for workbook in all_workbooks])

        if all_workbooks:
            # Pick one workbook from the list
            sample_workbook = "e0f307dc-6ac4-11e4-ab41-d704caa29a1d"

            # Download
            path = server.workbooks.download(sample_workbook, path)
            print("\nDownloaded workbook to {}".format(path))

    # SIGN OUT
    server.auth.sign_out()

if __name__ == '__main__':
    main()