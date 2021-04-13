
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
#print("Sort finished")
x_axis = []
y_axis = []
for el in ordered: 
 #   print(el)
    x_axis.append(el[1])
    
    y_axis.append(el[0])
#fig, ax = plt.subplots()
#ax.plot(x_axis, y_axis)
#plt.scatter(x_axis, y_axis)
#plt.show()


#Code size over time
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
#sequence_sized: sorted list of pairs (timestamp of commit, locs post-commit)
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
#plt.scatter(x_new, y_new)
#plt.show()

#Issue density
#Fetch all closed issues, sort by created at
#Fetch all open issues, sort by created at
#Bin into periods of one week (604800000 ms)
open_issues = repo.get_issues(state='open')
ftemp=[]
stemp = []
for el in open_issues:
    ftemp.append(el.created_at.timestamp())
for el in closed_issues:
    stemp.append((el.created_at.timestamp(), el.closed_at.timestamp()))
open_sorted = sorted(ftemp)
closed_sorted = sorted(stemp, key = itemgetter(0))
first_created = min(open_sorted[0], closed_sorted[0][0])
last_created = max(open_sorted[len(open_sorted)-1], closed_sorted[len(closed_sorted)-1][0])
time_range = int((last_created-first_created)/86400)+1
count = []
code_size=[]
for i in range(0, time_range):
    count.append(0)
    code_size.append(0)
for el in open_sorted:
    day = int((el-first_created)/86400)
    count[day]=count[day]+1
for el in closed_sorted:
    day = int((el[0]-first_created)/86400)
    count[day]=count[day]+1
    close_day = int(el[1]-first_created/86400)
    if close_day < len(count):
        count[close_day] = count[close_day]-1
#Convert from change in count over time to absolute count over time
for i in range(1, len(count)):
    count[i]+=count[i-1]

for i in range(0, len(sequence_sized)):
    day_of =  int((sequence_sized[i][0] - first_created)/86400)
    if day_of >= 0 and day_of < len(count):
        code_size[day_of] = sequence_sized[i][1]
for i in range(1, len(code_size)):
    #Any day on which no commits occurred, code size remains same size as previous day
    if code_size[i] == 0:
        code_size[i]=code_size[i-1]
plt.scatter(code_size, count)
plt.show() 
#We have code size over time
# repo = g.get_repo("Repo Name") ex.("emda19/comp370-group-activity-week9")
# open_issues = repo.get_issues(state='open')  # also need closed issues
# for issue in open_issues:
    # do something here, printing an issue gives the title and number


# /repos/{owner}/{repo}/issues
# github.Repository.Repository.get_issues()

# /repos/{owner}/{repo}/commits
# github.Repository.Repository.get_commits()

