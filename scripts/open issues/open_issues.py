

from github import Github
import csv
import matplotlib.pyplot as plt
import matplotlib
from datetime import date
from operator import itemgetter

g = Github("access_token")
g = Github("")      #acess token here
repo = g.get_repo("paholg/typenum")
to_sort = []
closed_issues = repo.get_issues()
for issue in closed_issues:
    to_sort.append((issue.created_at.timestamp(),issue.comments,len(issue.assignees)))

ordered = sorted(to_sort,key = itemgetter(1))
print("sort finished")
print(ordered)

with open('openIssues.csv','w',newline ='') as file:
    writer = csv.writer(file)
    writer.writerow(["time created","number of comments","length assigney"])
    for e in ordered:
        writer.writerow(e)


# This is all the commits and when there were commited with there timestamp


    
