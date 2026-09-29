vorm1_x1 = int(input())
vorm1_y1 = int(input())
vorm1_x2 = int(input())
vorm1_y2 = int(input())
vorm2_x1 = int(input())
vorm2_y1 = int(input())
vorm2_x2 = int(input())
vorm2_y2 = int(input())

def overlappen(x1, y1, x2, y2, x1_2, y1_2, x2_2, y2_2):
    linkerzijde = max(min(x1, x2), min(x1_2, x2_2))
    rechterzijde = min(max(x1, x2), max(x1_2, x2_2))
    onderzijde = max(min(y1, y2), min(y1_2, y2_2))
    bovenzijde = min(max(y1, y2), max(y1_2, y2_2))

    return linkerzijde < rechterzijde and onderzijde < bovenzijde


print("botsing" if overlappen(
    vorm1_x1, vorm1_y1, vorm1_x2, vorm1_y2,
    vorm2_x1, vorm2_y1, vorm2_x2, vorm2_y2
) else "geen botsing")