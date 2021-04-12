

from github import Github
import csv
import matplotlib.pyplot as plt
import matplotlib
from datetime import date
from operator import itemgetter

g = Github("access_token")
g = Github("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")
repo = g.get_repo("paholg/typenum")
commits_issued = repo.get_commits()

with open('commits.csv','w',newline ='') as file:
    writer = csv.writer(file)
    writer.writerow(["time commited"])
    for commits in commits_issued:
        writer.writerow(str(commits.commit.author.date))



# This is all the commits and when there were commited with there timestamp


    
