import numpy
import matplotlib.pyplot
import glob

test=1

def check_data(data,file="test"):
  test=2
  print(test)
  max_inflammation_0=numpy.max(data,axis=0)[0]
  max_inflammation_20=numpy.max(data,axis=0)[20]
  sum_inflammation_min=numpy.sum(numpy.min(data,axis=0))
  print(file)
  
  if max_inflammation_0==0.0 and max_inflammation_20==20.0:
    print("suspcious looking max")
  elif sum_inflammation_min==0.0:
    print("all minima add up to zero")
  else:
    print("seems ok")
def make_plots(data):
  fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))
  
  axes1 = fig.add_subplot(1, 3, 1)
  axes2 = fig.add_subplot(1, 3, 2)
  axes3 = fig.add_subplot(1, 3, 3)
  
  axes1.set_ylabel('average')
  axes1.plot(numpy.mean(data, axis=0))
  
  axes2.set_ylabel('max')
  axes2.plot(numpy.max(data, axis=0))
  
  axes3.set_ylabel('min')
  axes3.plot(numpy.min(data, axis=0))
  
  fig.tight_layout()
  
  matplotlib.pyplot.show()
def main():
  files=glob.glob("inflammation*.csv")
  #files=sorted(files[:3])
  
  for file in files:
    
    data = numpy.loadtxt(fname=file, delimiter=',')
    
    check_data(data,file)
  
    #make_plots(data)
    
  print("all done")

if __name__=="__main__":
  main()