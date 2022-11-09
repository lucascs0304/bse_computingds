#
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#

CV = [{'user': 'lucas', 'jobs': ['analyst', 'finance']},
      {'user': 'giovanna', 'jobs': ['researcher', 'analyst']}]

#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

#def has_experience_as(a,b):

def has_experience_as(x,jt):
    valores = []
    for i in x:
        for j in i['jobs']:
            if j ==jt:
                valores.append(i['user'])
    return(valores)

print(has_experience_as(CV, 'analyst'))

# map from the list
# lopp over the k and v, if v = word than you get the key and store



#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.


def job_counts(cv_list):
    keys = []
    dic_fin = {}
    for cv in cv_list:
        for j in cv['jobs']:
            keys.append(j)
    

    for c in range(len(keys)):
        dic_fin[keys[c]] = keys.count(keys[c])
    return(dic_fin)

print(job_counts(CV))

#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#

def most_popular_job(x):
    x = job_counts(x)
    mvalue = max(x.values())
    kvalue = list(x.keys())[list(x.values()).index(mvalue)]
    tuple = (kvalue, mvalue)
    return(tuple)

print(most_popular_job(CV))


# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.
