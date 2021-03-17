import RPY, requests
#Posting to discord with webhook

Limit = 1
Tags = "spaces_must_be_replaced_with_underscores"
PageNumber = 1

for i in RPY.GetPosts(limit=Limit,tags=Tags,pagenumber=PageNumber):
    DATA = {
        "content":i
    }
    A = requests.post("discord webhook",data=DATA)