import numpy, pylab, scipy.optimize

raw_accel = []

f=open("tummy.plist", "r")
for line in f:
    if "<real>" in line:
        raw_accel.append(float(line[7:-9]))

accel = raw_accel[125:145]
times = numpy.arange(0,2,0.1)
hd_times = numpy.arange(0,2,0.01)

def wave(times, a, b, c, d):
    return a * numpy.sin(b * times + c) + d

def errorfun((a, b, c, d), accel, times):
    return numpy.sum(numpy.power(wave(times,a,b,c,d)-accel, 2))

guess = ((numpy.max(accel)-numpy.min(accel))/2.0,
    20.0,
    1.0,
    numpy.median(accel))

result = scipy.optimize.fmin(errorfun, guess, args=(accel, times),
    maxiter=2000, maxfun=2000, xtol=1e-10)
print result


pylab.plot(times, accel, 'ko-')
pylab.plot(hd_times, wave(hd_times, guess[0], guess[1], guess[2], guess[3]), "b-")
pylab.plot(hd_times, wave(hd_times, result[0], result[1], result[2], guess[3]), "r-")
pylab.show()


