from datetime import datetime

# tuples of minutes seperated into the respective decimal number. first item in each tuple is the actual value needed in the final time.
zero = (0.0,0,1,2)
one = (0.1,3,4,5,6,7,8)
two = (0.2,9,10,11,12,13,14)
three = (0.3,15,16,17,18,19,20)
four = (0.4,21,22,23,24,25,26)
five = (0.5,27,28,29,30,31,32)
six = (0.6,33,34,35,36,37,38)
seven = (0.7,39,40,41,42,43,44)
eight = (0.8,45,46,47,48,49,50)
nine = (0.9,51,52,53,54,55,56)
one_zero = (1.0,57,58,59)


# varibles used to test, delete if not req'd
start = '0900'
stop = '1756'

def conv_to_dec(mins):
    for x in zero,one,two,three,four,five,six,seven,eight,nine,one_zero:
        if mins in x:
            return x[0]

def time_calc(start,stop):
    t1 = datetime.strptime(start,"%H%M")
    t2 = datetime.strptime(stop,"%H%M")
    delta = t2 - t1
    delta_sec = delta.total_seconds()
    delta_mins = delta_sec / 60
    delta_hrs = delta_mins /60
    t_conv_hr = int(delta_hrs)
    t_conv_min = conv_to_dec(int(delta_mins % 60))
    a = t_conv_hr + t_conv_min
    print(a)

time_calc(start,stop)
