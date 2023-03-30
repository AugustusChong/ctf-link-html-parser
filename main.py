from bs4 import BeautifulSoup
import re
import requests as req

html = req.get(input("Enter website link\n")).text
soup = BeautifulSoup(html, "html.parser")

pattern = [item for item in input("\nEnter the pattern of tags in order. For example: section, main, article, p\n"
                                  "Currently only works with 4 tags: \n")
           .strip().split(", ")]

tagClass = input("\nEnter the class to look for: \n")

parentTags = soup.select(pattern[0])

for parentTag in parentTags:
    firstChild = parentTag.find(pattern[1])
    secondChild = firstChild.find(pattern[2])
    thirdChild = secondChild.find(pattern[3], class_=tagClass, attrs={'value'})

    if firstChild and secondChild and thirdChild:
        print(thirdChild['value'], end="")

input("\n\nPress enter to proceed")

# html = """
#
#        """

# sections = soup.select('section')
#
# for section in sections:
#     main = section.find('main')
#     article = main.find('article')
#     p = article.find('p', class_='flag', attrs={'value'})
#
#     if main and article and p:
#         print(p['value'], end="")
