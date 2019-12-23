import csv
import matplotlib.pyplot as plt
import numpy as np

with open('19_results_2.csv', 'r') as f:
    reader = csv.reader(f)
    result_list = list(reader)

results = np.array(result_list)
#dynamic decay
std_error=[]
dynamic_decay_std_error = [1.7096052099731722e-05, 0.00018880017215732218, 0.0002641244207957075, 0.0003175730744043212, 0.0003499835195835506, 0.00036911443182476716, 0.0004174487324847355, 0.00043214991540808614, 0.00043870392476544204, 0.0004545513855956168, 0.0004570949395508066, 0.00045661456150454505, 0.00045855730378891417, 0.0004489672403053533, 0.0004441186761574287, 0.0004255146253074154, 0.0004109172680079285, 0.00038974896155588573, 0.00037966036275345237, 0.0003672042448015846, 0.0003509656804921972, 0.0003430047009158667, 0.00032874078470422803, 0.00031819820291289623, 0.0003024554774982955, 0.00028831891198154906, 0.000275401711729501, 0.00026461787266661874, 0.00025793804216531137, 0.000246506868122444, 0.0002390434929849204, 0.00022960410086669638, 0.00022140836388899514, 0.00021663818118362608, 0.00020395952770227646, 0.00019840737582612182, 0.00019071935767408406, 0.00018368066686421194, 0.0001769730910760975, 0.00016906013901086078, 0.00016287779898841877, 0.00015605481630618916, 0.00014891202530705193, 0.0001425261949222708, 0.00013707469897021314, 0.0001331318970922725, 0.00012726313070120503, 0.0001208919009603316, 0.00011558959219462493, 0.00011136758180743833]
dynamic_decay_std_error = [2.58*i for i in dynamic_decay_std_error]
std_error.append(dynamic_decay_std_error)
#td_error_max
td_error_max_std_error = [1.3024061545359394e-05, 0.0001418781442025195, 0.00019865309608039337, 0.00023414512413019142, 0.00025395471762034084, 0.0002602954540316553, 0.00028532808752156145, 0.0002919982306920935, 0.00029812952015592474,
0.0003062349915906397, 0.00030451601497490165, 0.0003057353972941858, 0.00030817934927734674, 0.0003076283905114234, 0.00030450746231255416, 0.00029808662799086605, 0.0002953294774522048, 0.0002895961401306419, 0.00028357197742890576, 0.000278689533339603, 0.00027298497218797204, 0.0002657281437937526, 0.0002556659670010287, 0.0002511436653642231, 0.00024471983160357887, 0.00023890499381374396, 0.00023055311524850452, 0.0002222861042818232, 0.00021532224293651172, 0.00020688821756628242, 0.00019976277269736107, 0.0001928566918189937, 0.0001867012791610669, 0.00018239730922308138, 0.00017585942860569922, 0.00017082385375384566, 0.00016331066652568066, 0.00015812447548232964, 0.00015175649593607833, 0.00014499429918612356, 0.00013936781149761305, 0.0001332390031161699, 0.00012804416526514408, 0.0001227070544904873, 0.00011807187764927703, 0.00011396961078745474, 0.00010888230603668298, 0.00010366338829059653, 0.00010003432080544865, 9.654920984076808e-05]
td_error_max_std_error = [2.58*i for i in td_error_max_std_error]
std_error.append( td_error_max_std_error)
# colours = ['r--','b--','r-.','b-.','r-','b-','r:','b:','b--']
colours = ['b','g','b','y','m']

colour_index = 0

for i in range(0, results.shape[0]):
    plotx = np.arange(results.shape[1]-1)
    ploty = list(map(float, results[i,1:]))
    plt.plot(plotx, ploty, colours[colour_index], label = results[i,0])
    plt.fill_between(plotx, np.array(ploty)-std_error[i], np.array(ploty)+std_error[i], color=colours[colour_index], alpha=0.2)
    colour_index+=1

plt.xlabel('Episodes')
plt.ylabel('RMS Error')
plt.legend()
plt.show()