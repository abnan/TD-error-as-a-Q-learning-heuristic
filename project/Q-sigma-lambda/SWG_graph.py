import csv
import matplotlib.pyplot as plt
import numpy as np

with open('SWG_results.csv', 'r') as f:
    reader = csv.reader(f)
    result_list = list(reader)

results = np.array(result_list)
#dynamic decay
std_error=[]
dynamic_decay_std_error =  [12.289108209141965, 8.796591589928454, 5.696464589199165, 5.037171958946812, 3.518294867545924, 3.1588448482000517, 2.877720934176903, 2.5836424086935885, 2.478891642448293, 2.823060115548376, 2.4596270024131703, 2.1517843012253812, 1.6063567222133455, 1.531649813436479, 1.650869952176729, 1.7696103932787008, 1.4337045828900732, 1.4165812475816562, 1.440081591785687, 1.447978582369229, 1.2744917669408469, 1.3381870885642253, 1.5100778758064075, 1.3512602354839087, 1.2888329911202612, 1.1807045180738494, 1.022493649858033, 1.0626614696129717, 0.9335644723317189, 1.1284659139734794, 1.7132166459616258, 1.2205853284387826, 0.9571666516338728, 1.0725209088870953, 1.0879098767820796, 0.8704329956981184, 1.0287651194514706, 0.7626690081549137, 0.8180108458938659, 0.6935461801495263, 0.7542292695195543, 0.746205966205042, 0.6658723413688242, 0.5298007465075908, 0.7936017735615263, 0.6249957687856775, 0.6443245641755416, 0.5654983421726372, 0.5701704297839377, 0.4961349655083786, 0.7135850643055806, 0.5252176682100471, 0.6139343409518656, 0.5886813866600511, 0.6042433938405933, 0.6158085384273267, 0.5600435375932875, 0.8413815965422587, 0.7045496604214623, 0.5423597735820758, 0.7147181479436491, 0.7024711915801248, 0.7048523072247123, 0.48353149225257114, 0.6169603479965309, 0.5115520501376163, 0.6924465726682459, 0.5811115891117644, 0.5284657642648197, 0.5839881471399917, 0.668940935359767, 0.6778817005938425, 0.5772996024595896, 0.8556674114397484, 0.6606439404096586, 0.5572416271241772, 0.5390284445184689, 0.4397625495651034, 0.5969752289668301, 0.5257858642070937, 0.5344622531105448, 0.5638890236562507, 0.43491082304306883, 0.5300820455363486, 0.5213280876760807, 0.6023789297443913, 0.5159556172773004, 0.5017802546932252, 0.5108075919561106, 0.45109544444607313, 0.49713531256590543, 0.4085118162305708, 0.4636990737536579, 0.4113453232990502, 0.38717452266387575, 0.40448568701500437, 0.4644073039907959, 0.5659740064702616, 0.4288662448829471, 0.4921388869008423]
dynamic_decay_std_error = [2.58*i for i in dynamic_decay_std_error]
std_error.append(dynamic_decay_std_error)
#td_error_max
td_error_max_std_error = [12.389200274271136, 8.296025910036679, 4.921531220971784, 3.138241290277089, 3.403432744156991, 2.560083387509087, 2.348349028360136, 2.429699052146172, 2.698432748096569, 2.170910085425004, 1.5815441792754328, 1.8956415249197303, 1.6360823255569998, 1.9135259473025172, 1.26685452953368, 1.4691532496645852, 1.5734786379229941, 1.5113859851143259, 1.4059094579666211, 1.0971862699651316, 1.434916051899902, 1.0444453149878175, 1.0308908303016373, 1.4403999097472902, 1.462114985560301, 1.132742088473807, 1.1910172421086105, 1.2856543979623751, 1.0417171165916392, 1.3390919755565704, 1.1023899781837645, 0.9016028122183292, 1.0719667863324873, 1.0746145560153189, 1.0011819335165812, 0.8577882903141086, 0.9459133020525718, 1.0596045130141722, 0.8922396264457202, 0.9809550320988198, 1.0865759632901886, 0.8538877437930588, 0.8998735638966138, 0.9086313658464577, 0.8677445499684808, 0.9096159167472821, 0.8408122971270108, 1.115347378622463, 0.9792129472183253, 0.783414421618596, 0.6717567052140224, 0.7284612934123538, 0.7319981530031343, 0.719312101941848, 0.8292851765225283, 1.0742556697546428, 0.7920105327582457, 0.6627492670686249, 0.8168720242485965, 0.8832003532607983, 0.6918338463822079, 0.9034242392143355, 0.7852945332803484, 0.7960520862355671, 0.8066827356526247, 1.07536947139111, 0.9188310829526821, 0.9002292102570322, 0.5888669043170959, 0.6275513556674068, 0.5946423429255605, 0.7816787677812419, 0.7316770592276353, 0.7512433101199634, 0.8423789355153655, 0.583751980724692, 0.5704654231414905, 0.6310885445006928, 0.6530434472529372, 0.6560682891285041, 0.5845253630083138, 0.6083345913229004, 0.5501183000046443, 0.6892112005764246, 0.8105946854007854, 0.7811771316417299, 0.6913868121391936, 0.7702023883369852, 0.8403119396985861, 0.890385183502062, 0.7885901540090333, 0.754835160150877, 0.7682341928084162, 0.7495712481145504, 0.672471839559101, 1.4483275858727553, 0.9054085464584496, 0.7505525298072099, 0.6819521090223268, 0.6821495429889265]
td_error_max_std_error = [2.58*i for i in td_error_max_std_error]
std_error.append(td_error_max_std_error)
# colours = ['r--','b--','r-.','b-.','r-','b-','r:','b:','b--']
colours = ['r','g','b','y','p']

colour_index = 0
truncate = 5
for i in range(results.shape[0]):
    plotx = np.arange(results.shape[1]-1)
    ploty = list(map(float, results[i, 1:]))
    plotx=plotx[truncate:]
    ploty=ploty[truncate:]
    # std_error[i]=std_error[i][truncate:]
    plt.plot(plotx, ploty, colours[colour_index], label = results[i,0])
    # plt.fill_between(plotx, np.array(ploty)-std_error[i], np.array(ploty)+std_error[i], color=colours[colour_index], alpha=0.3)
    colour_index+=1

plt.xlabel('Episodes')
plt.ylabel('Average Return')
plt.legend()
plt.show()