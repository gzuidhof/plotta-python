import plotta
import math
import time

if __name__ == '__main__':
    job = plotta.Job("Example job")

    #Communicate job to plotta server
    job.start()

    #Create streams
    sin_stream = job.add_stream('sin(x)')
    cos_stream = job.add_stream('cos(2x)')

    for x in xrange(200):
        y_sin = math.sin(0.1 * x)
        y_cos = math.sin(0.2 * x)

        sin_stream.append(x, y_sin)
        cos_stream.append(x, y_cos)

        print x, y_sin, y_cos
        time.sleep(.25)

    #Tell plotta the job is finished
    job.stop()
