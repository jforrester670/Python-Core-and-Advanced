lst=["USA","Canada","Korea"]
lst.append("United Kingdom")
del lst[1]
middle=len(lst)//2
lst = lst[0:middle] + ["Brazil"] + lst[middle:]

s={"USA","Canada","Korea"}
s.update(["United Kingdom"])
s.remove("Canada")
s.update(["Brazil"])
