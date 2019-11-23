from math import log as ln
import numpy as np
from matplotlib import pyplot as plt
import random
dimention=2
percent_training_data=0.75
maximum_number_of_weight_update=100
learning_rate=0.1
number_of_classes=3
deepak=1000
def read_training_dataset(filename):
    file_object=open(filename,'r')
    file_data=file_object.readlines()
    data_vectors=[]#list of list
    for line in file_data:
        data_vectors.append([float(x) for x in line.split()])
    return data_vectors

def main():
     training_data=[[] for i in range(3)]
     # training_data_Y=[[] for i in range(3)]
     # testing_data_X=[[] for i in range(3)]
     testing_data=[[] for i in range(3)]
     # xmin=ymin=100;xmax=ymax=-100
     upper_limit=-100
     lower_limit=100
     for i in range(1,4):#because it is three class perceptron
         filename='data/Class'+str(i)+'.txt'
         data_vectors=read_training_dataset(filename)
         # print ('mini ===============================',data_vectors)
         # print
         lower_limit=min(lower_limit, np.amin(data_vectors));
         upper_limit=max(upper_limit, np.amax(data_vectors));
         # xmax=max(xmax, np.amax(data_vectors,axis=0)[0]);
         # ymax=max(ymax, np.amax(data_vectors,axis=1)[1]);

         # print('number of traning dataset === ',int(len(data_vectors)*percent_training_data))
         # training_data=data_vectors[]
         for item in data_vectors[:int(len(data_vectors)*percent_training_data)]:
             # print item
             training_data.append([item[0],item[1],i])
             # training_data_Y[i-1].append(item[1])
         for item in data_vectors[int(len(data_vectors)*percent_training_data):]:
             # print item
             testing_data.append([item[0],item[1],i])
             # testing_data_Y[i-1].append(item[1])
     training_data = [x for x in training_data if x != []]
     # print(training_data[0])
     weight=[0 for i in range(dimention)]
     bias=0
     # i think we should this number of input as all willl upadte the weght one time
     print(len(training_data))
     random.shuffle(training_data)
     for i in range(len(training_data)):
         # print(training_data[i])
         # print(weight[0],weight[1],bias)
         # for j in range(dimention):
         val=0
         val+=(training_data[i][0]*weight[0])
         val+=(training_data[i][1]*weight[1])
         val+=bias
         output=0
         #activation
         if val>deepak:
             output=1
         elif val>=-deepak:
             output=2
         else :
             output=3
         #weight update
         weight[0]=weight[0]+(learning_rate*(training_data[i][2]-output)*training_data[i][0])
         weight[1]=weight[1]+(learning_rate*(training_data[i][2]-output)*training_data[i][1])
         bias=bias+(learning_rate*(training_data[i][2]-output)*1)#bias can be assumed as input value 1


     X=[[] for v in range(number_of_classes)]
     Y=[[] for v in range(number_of_classes)]
     # # print X,Y
     # # print xmin,' == ',xmax
     # # print ymin,' == ',ymax
     for i in np.arange(lower_limit,upper_limit,0.1):
         for j in np.arange(lower_limit,upper_limit,0.1):
             val=0
             val+=(i*weight[0])
             val+=(j*weight[1])
             val+=bias
             output=0
             #activation
             if val>deepak:
                 output=1
             elif val>=-deepak:
                 output=2
             else :
                 output=3
             # print i,j,' belongs to class ',C
             X[output-1].append(i)
             Y[output-1].append(j)
     #             # print calculatingG(W[k],W0[k],X)
     print ('drawing graph...\n')
     # print X,Y
     #naming the x axis
     plt.xlabel('x - axis')
     # naming the y axis
     plt.ylabel('y - axis')
     plt.plot(X[0],Y[0],color='#76dc0a',label='class 1')
     plt.plot(X[1],Y[1],color='#aa2889',label='class 2')
     plt.plot(X[2],Y[2],color='#2391c8',label='class 3')
     testing_data = [x for x in testing_data if x != []]
     random.shuffle(testing_data)
     for i in range(len(testing_data)):
         # print(training_data[i])
         # print(weight[0],weight[1],bias)
         # for j in range(dimention):
         val=0
         val+=(testing_data[i][0]*weight[0])
         val+=(testing_data[i][1]*weight[1])
         val+=bias
         output=0
         #activation
         if val>deepak:
             output=1
         elif val>=-deepak:
             output=2
         else :
             output=3
     # for i in range(125):
         # if i==0:
         #     pass
         #     plt.plot(testing_data_X[0][i], testing_data_Y[0][i],marker='o', markersize=1, color="red",label='test class 1')
         #     plt.plot(testing_data_X[1][i], testing_data_Y[1][i],marker='o', markersize=1, color="green",label='test class 2')
         #     plt.plot(testing_data_X[2][i], testing_data_Y[2][i],marker='o', markersize=1, color="blue",label='test class 3')
         # else:
         if output==1:
             plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="green")
         elif output==2:
             plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="black")
         else:
             plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="blue")
             # plt.plot(testing_data_X[2][i], testing_data_Y[2][i],marker='o', markersize=1, color="blue")


     plt.legend()
     plt.savefig('result.png')
     # plt.savefig('result.pdf')
     # plt.show()
if __name__ == '__main__':
    main()
    # print("frist")
