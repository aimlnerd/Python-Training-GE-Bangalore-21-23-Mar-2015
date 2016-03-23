
class Demo(object):
    def __init__(self):
        print "{}: am in constructor".format(self)

    def __del__(self):
        print "getting destroyed: {}".format(self)

d = Demo()
d2 = Demo()
del d2
print d

