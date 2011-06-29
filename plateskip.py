#/usr/bin/python
import pprint
plate_y_384 = [chr(65 + x) for x in range(16)]
plate_y_96 = [chr(65 + x) for x in range(8)]
plate_x_384 = range(1,25,1)
plate_x_96 = range(1,13,1)

masterdict = {}

# plate q1 coords
q1dict = {}
q1_y_map = [plate_y_384[i] for i in range(0,16,2)]
q1_x_map = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
print "Q1 map"
print q1_y_map
print q1_x_map
masterdict[1]=[q1_y_map,q1_x_map]


q2_y_map = [plate_y_384[i] for i in range(0,16,2)]
q2_x_map = range(2,25,2)
print "Q2 map"
print q2_y_map
print q2_x_map
masterdict[2] = [q2_y_map,q2_x_map]


q3_y_map = [plate_y_384[i] for i in range(1,16,2)]
q3_x_map = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
print "Q3 map"
print q3_y_map
print q3_x_map
masterdict[3] = [q3_y_map,q3_x_map]


q4_y_map = [plate_y_384[i] for i in range(1,16,2)]
q4_x_map = range(2,25,2)
masterdict[4] = [q4_y_map,q4_x_map]
print "Q4 map"
print q4_y_map
print q4_x_map


def print_plate(a_plate_dict):
    for yc in plate_y_96:
        for xc in plate_x_96:
            print "".join([str(x) for x in [yc,xc]]),a_plate_dict["".join([str(yc),str(xc)])]

def make_platemap_dict(qpos):
    myqdict = {}
    for xindex,xc in enumerate(plate_x_96):
        for yindex,yc in enumerate(plate_y_96):
            #print yc,xc,masterdict[qpos][0][yindex],masterdict[qpos][1][xindex]
            myqdict["".join([str(yc),str(xc)])] =  "".join([str(masterdict[qpos][0][yindex]),str(masterdict[qpos][1][xindex])])
    return myqdict

# for xindex,xc in enumerate(plate_x_96):
#     for yindex,yc in enumerate(plate_y_96):
#         #print yc,xc,q1_y_map[yindex],q1_x_map[xindex]
#         q1dict["".join([str(yc),str(xc)])] =  "".join([str(q1_y_map[yindex]),str(q1_x_map[xindex])])
# print_plate(q1dict)
# print "Total mapped" , len(q1dict.keys())

if __name__ == '__main__':
    for i in range(1,5,1):
        print "Q POSITION",i
        print_plate(make_platemap_dict(i))
