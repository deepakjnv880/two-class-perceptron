from math import log as ln
import numpy as np
from matplotlib import pyplot as plt
import random
dimention=2
percent_training_data=0.75
maximum_number_of_weight_update=100
learning_rate=0.1

def read_training_dataset(filename):
    file_object=open(filename,'r')
    file_data=file_object.readlines()
    data_vectors=[]#list of list
    for line in file_data:
        data_vectors.append([float(x) for x in line.split()])
    return data_vectors

def main():
     training_data=[]
     testing_data=[]
     # xmin=ymin=100;xmax=ymax=-100
     upper_limit=-100
     lower_limit=100
     for i in range(1,3):#because it is two class perceptron
         filename='data/Class'+str(i)+'.txt'
         data_vectors=read_training_dataset(filename)
         # print ('mini ===============================',data_vectors)
         # print
         lower_limit=min(lower_limit, np.amin(data_vectors));
         upper_limit=max(upper_limit, np.amax(data_vectors));

         for item in data_vectors[:int(len(data_vectors)*percent_training_data)]:
             # print item
             training_data.append([item[0],item[1],i-1])
             # training_data_Y[i-1].append(item[1])
         for item in data_vectors[int(len(data_vectors)*percent_training_data):]:
             # print item
             testing_data.append([item[0],item[1],i-1])
             # testing_data_Y[i-1].append(item[1])
     training_data = [x for x in training_data if x != []]
     weight = [0,0]
     bias=0
     # i think we should this number of input as all willl upadte the weght one time
     print(len(training_data))
     random.shuffle(training_data)
     number_of_wrongly_classified_point=len(training_data)
     converge_graph_x=[0]
     converge_graph_y=[number_of_wrongly_classified_point]
     itr=0
     while number_of_wrongly_classified_point!=0:
         itr+=1
     # for i2 in range(50):
         # print("=== wronlgy ",number_of_wrongly_classified_point)
         print(weight[0],weight[1],bias)
         number_of_wrongly_classified_point=0
         for i in range(len(training_data)):

             val=0
             val+=(training_data[i][0]*weight[0])
             val+=(training_data[i][1]*weight[1])
             val+=bias
             # print("val == ",val)
             output=0
             #activation
             if val>=0:
                 output=1
             else :
                 output=0

             number_of_wrongly_classified_point+=abs(output-training_data[i][2])
             #weight update
             weight[0]=weight[0]+(learning_rate*(training_data[i][2]-output)*training_data[i][0])
             weight[1]=weight[1]+(learning_rate*(training_data[i][2]-output)*training_data[i][1])
             bias=bias+(learning_rate*(training_data[i][2]-output)*1)#bias can be assumed as input value 1

         converge_graph_x.append(itr)
         converge_graph_y.append(number_of_wrongly_classified_point)


     # print("F")
     X=[[] for v in range(dimention)]
     Y=[[] for v in range(dimention)]

     for i in np.arange(lower_limit,upper_limit,0.1):
         for j in np.arange(lower_limit,upper_limit,0.1):
             val=0
             val+=(i*weight[0])
             val+=(j*weight[1])
             val+=bias
             output=0
             #activation
             if val>=0:
                 output=1
             else :
                 output=0
             # print i,j,' belongs to class ',C
             X[output].append(i)
             Y[output].append(j)

     print ('#### drawing graph...\n')
     # print X,Y
     #naming the x axis
     plt.xlabel('x - axis')
     # naming the y axis
     plt.ylabel('y - axis')
     plt.plot(X[0],Y[0],color='#76dc0a',label='class 0')
     plt.plot(X[1],Y[1],color='#aa2889',label='class 1')
     # plt.plot(X[2],Y[2],color='#2391c8',label='class 3')
     testing_data = [x for x in testing_data if x != []]
     random.shuffle(testing_data)
     check1=False
     check0=False
     total_error=0
     for i in range(len(testing_data)):

         val=0
         val+=(testing_data[i][0]*weight[0])
         val+=(testing_data[i][1]*weight[1])
         val+=bias
         output=0
         #activation
         if val>=0:
             output=1
         else :
             output=0
         total_error+=abs(output-testing_data[i][2])
         if output==1:
             if check1==False:
                 plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="red",label='class 1')
                 check1=True
             else:
                 plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="red")
         else:
             if check0==False:
                 plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="green",label="class 0")
                 check0=True
             else:
                 plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="green")

     plt.plot(marker='o', markersize=1, color="green",label="redkw")
     plt.legend()
     plt.savefig('result.png')
     # plt.savefig('result.pdf')
     plt.show()
     plt.close()
     print("### drawing convergence graph ###\n")
     plt.show()
     plt.plot(converge_graph_x,converge_graph_y,color='red',label='convergence')
     # plt.plot(X[1],Y[1],color='#aa2889',label='class 1')
     # print(converge_graph_x,converge_graph_y)
     plt.savefig('convergence.png')
     plt.show()
     plt.close()
     print("model Accuracy is ",float(((len(testing_data)-total_error)/len(testing_data))*100))
     # print(converge_graph_x,converge_graph_y)
if __name__ == '__main__':
    main()
    # print("frist")
