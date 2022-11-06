def generateEdgeList(sheets):
    edges = []
    visted=set()
    for reg1 in sheets:
        for pt1 in sheets[reg1]:
            for reg2 in sheets:
                for pt2 in sheets[reg2]:
                    if pt1["id"]!=pt2["id"] and (pt2["id"],pt1["id"]) not in visted and reg1 != reg2:
                        edges.append((pt1,pt2))
                        visted.add((pt1["id"],pt2["id"]))

    with open("gedges.json","w+") as wf:
        json.dump(edges,wf,indent=4)
