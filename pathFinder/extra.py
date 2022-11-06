import json
from main import generateJson

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


def transpose_ext(ext_edges):
    edges=[]
    for e in ext_edges:
        new_edge={
        "pt1": {
            "id": e["_Route__p1"]["_RoutePoint__id"],
            "name": e["_Route__p1"]["_RoutePoint__name"],
            "loc": e["_Route__p1"]["_RoutePoint__loc"]
        },
        "pt2": {
            "id": e["_Route__p2"]["_RoutePoint__id"],
            "name": e["_Route__p2"]["_RoutePoint__name"],
            "loc": e["_Route__p2"]["_RoutePoint__loc"]
        },
        "dist": e["_Route__distance"]["value"]/1000,
        "polyline": e["_Route__polyline"]
    }
        edges.append(new_edge)
        
    return edges

doors, N = generateJson("MapData-Buildings.csv")
generateEdgeList(doors)

with open("edges-appended.json","r") as rf:
    oedges=json.load(rf)

with open("ex_edges.json","w+") as wf:
    json.dump(transpose_ext(oedges),wf,indent=4)