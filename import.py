# open file & create csvreader
import csv

# import the relevant model
from nysanitation.models import resturant

#loop:
f = open("export.csv")
for line in csv.reader(f):
    print(line)
    break
# foo = resturant(Zipcode=1)
# try:
#     foo.save()
# except:
#     # if the're a problem anywhere, you wanna know about it
#     print "there was a problem with line", i
