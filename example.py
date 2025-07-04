from bs4 import BeautifulSoup

#read HTML content

with open("index.html", "r") as f:
    data = f.read()
print(data)

#Parse it with BeautifulSoup

soup = BeautifulSoup(data, 'html.parser')

#Grab elements

divs = soup.select(" ") # "." for class or "#" for ID and "[empty]" for element
print(len(divs), "sections found")

for d in divs:
    print()
    print(d)

#to get content of elements
print("content:", divs[0].get_text())

div2 = divs[1]

pps = div2.select("p")

print("PPS:")

#use IDs, Classes, Structure to grab information needed

for p in pps:
    print(p.get_text())

dailies = soup.select(".daily")
for d in dailies:
    print(d.get_text())


print(dailies[1].attrs)
print(dailies[1].attrs['data-value'])