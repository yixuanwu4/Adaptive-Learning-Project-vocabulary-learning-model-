# Provide users with an Ebbinghaus curve to check on which date the learned words should be reviewed

from datetime import date, timedelta

# Review intervals, representing in days
# Days are picked according to the forgetting curve proposed by Hermann Ebbinghaus (2013)
# The user can adjust the review intervals by themselves
review_intervals = [2, 5, 8, 15, 30, 60] 

# The dates that should be reviewed
# The dates will be printed in the terminal
# The user can choose to review the words learned in the printed dates in the folder "oldwords"
for eachone in review_intervals:
    review_time = date.today() - timedelta(eachone)
    print(review_time.strftime("%Y/%m/%d"))


# Reference of picking the review_intervlas:
# Ebbinghaus, H. (2013). Memory: A contribution to experimental psychology. Annals of neurosciences, 20(4), 155.
