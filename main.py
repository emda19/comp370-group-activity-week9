
from github import Github
import matplotlib.pyplot as plt
import matplotlib
from datetime import date
from operator import itemgetter
to_sort = []
#Add personal access token below
g = Github("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")
repo = g.get_repo("paholg/typenum")
#closed_issues = repo.get_issues(state='closed')
#Getting only closed issues so that how long the issue is open is defined for all elements
#print(closed_issues.totalCount)
#for issue in closed_issues:
#    to_sort.append((issue.closed_at.timestamp()-issue.created_at.timestamp(), issue.comments, len(issue.assignees)))
#to_sort - list of tuples (duration_open, num_comments, num_assignees)
#do issues with more comments stay open longer?  Let x axis be comments, y axis be duration open
#ordered = sorted(to_sort, key=itemgetter(1))
#print("Sort finished")
#x_axis = []
#y_axis = []
#or el in ordered: 
 #   print(el)
  #  x_axis.append(el[1])
    
  #  y_axis.append(el[0])
#fig, ax = plt.subplots()
#ax.plot(x_axis, y_axis)
#plt.scatter(x_axis, y_axis)
#plt.show()
commits = repo.get_commits()
print(commits.totalCount)
temp = []
for commit in commits:
    #print(commit)
    #statuses = commit.get_statuses()
    #print(statuses[0].created_at)
    info = (commit.commit.author.date.timestamp(), commit.stats.additions-commit.stats.deletions)
    #print(commit.commit.author.date)
    #print(commit.stats.additions - commit.stats.deletions)
    #print(commit.commit)
    temp.append(info)
commit_sequence = sorted(temp, key = itemgetter(0))
#print(type(commit_sequence))
#print(type(temp))
sequence_sized=[]
for i in range(0, len(commit_sequence)):
    if i != 0: 
        sequence_sized.append((commit_sequence[i][0], commit_sequence[i][1]+sequence_sized[i-1][1]))
    else: 
        sequence_sized.append((commit_sequence[i]))
x_new = []
y_new = []
for el in sequence_sized:
    x_new.append(el[0])
    y_new.append(el[1])
plt.scatter(x_new, y_new)
plt.show()
# repo = g.get_repo("Repo Name") ex.("emda19/comp370-group-activity-week9")
# open_issues = repo.get_issues(state='open')  # also need closed issues
# for issue in open_issues:
    # do something here, printing an issue gives the title and number


# /repos/{owner}/{repo}/issues
# github.Repository.Repository.get_issues()

# /repos/{owner}/{repo}/commits
# github.Repository.Repository.get_commits()

