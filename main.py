



from app import Find
import os

hello = Find()

url = r"C:\Users\Ishmeet\OpenAI\tools\texts\A Guide To Outdoor Living And Wilderness Survival.txt"
query = "Solar Navigation?"


# x = hello.structured_output(query)
# print(x)

hello.vectorDB_initialize(url)

