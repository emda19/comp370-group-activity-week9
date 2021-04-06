
from github import Github
import matplotlib.pyplot as plt
import matplotlib
from datetime import date
from operator import itemgetter
to_sort = []
#Add personal access token below
g = Github("")
repo = g.get_repo("paholg/typenum")
closed_issues = repo.get_issues(state='closed')
#Getting only closed issues so that how long the issue is open is defined for all elements
print(closed_issues.totalCount)
for issue in closed_issues:
    to_sort.append((issue.closed_at.timestamp()-issue.created_at.timestamp(), issue.comments, len(issue.assignees)))
#to_sort - list of tuples (duration_open, num_comments, num_assignees)
#do issues with more comments stay open longer?  Let x axis be comments, y axis be duration open
ordered = sorted(to_sort, key=itemgetter(1))
print("Sort finished")
x_axis = []
y_axis = []
for el in ordered: 
    print(el)
    x_axis.append(el[1])
    
    y_axis.append(el[0])
#fig, ax = plt.subplots()
#ax.plot(x_axis, y_axis)
plt.scatter(x_axis, y_axis)
plt.show()

# repo = g.get_repo("Repo Name") ex.("emda19/comp370-group-activity-week9")
# open_issues = repo.get_issues(state='open')  # also need closed issues
# for issue in open_issues:
    # do something here, printing an issue gives the title and number


# /repos/{owner}/{repo}/issues
# github.Repository.Repository.get_issues()

# /repos/{owner}/{repo}/commits
# github.Repository.Repository.get_commits()

