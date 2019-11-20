# this reads out the information in data/gps*/superevent_groups and plots the events listed
# layout of file, assuming two events triggered under one superevent:
# name_of_superevent|pipeline1_triggeres,pipeline2_triggered|FAR1,FAR2|SNR1,SNR2

# Name of search. Layout style:
#         gps GPS time - before + after  far
#            v--------v v------v v------vv--v

search = "gps1246017618-91d12h0m0s+91d12h0m0s1e-4"
#search = "gps1242626773-1d0h0m0s+0d2h0m0s1e-4"

search_time = search[3:13]

superevent_list = []
pipeline_list = []
num_events = []
far_list = []
snr_list = []
num_pipelines = []

# open event search file and read out each line, splitting into catagories
with open("data/"+search+"/superevent_groups","r") as f:
        for line in f:
                # split line into catagories
                split_line = line.split('|')
                # read out superevent names
                superevent_list.append(split_line[0])
                # read out pipelines triggered, further splitting
                pipeline_list.append(split_line[1].split(','))
                # based on number of split pipeline names,
                # determine number of events and pieplines in superevent
                num_events.append(len(split_line[1].split(',')))
                # read out far for events, splitting
                far_list.append(split_line[2].split(','))
                # read of snr for events, splitting
                snr_list.append(split_line[3][:-1].split(','))

# set the list of interest
interest_list = far_list

num_pipelines = []
for event in pipeline_list:
    num_pipelines.append(len(set(event)))

# read in the names of the public superevents
public_events = []
with open("public_events.txt") as f:
    for line in f:
        public_events.append(line[:-1])

retracted_events = []
with open("retracted_events.txt") as f:
    for line in f:
        retracted_events.append(line[:-1])

public_set_list = list(set(public_events).intersection(superevent_list))
real_public_events = list(set(public_events) - set(retracted_events))


import numpy as np
#import matplotlib
#matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# separate into numbers of events
min_far_idx_list = []
far_plot_list = []
snr_plot_list = []

far_1d_list = []
far_2d_list = []
far_3d_list = []
far_4d_list = []
far_5d_list = []

snr_1d_list = []
snr_2d_list = []
snr_3d_list = []
snr_4d_list = []
snr_5d_list = []

public_far_list = []
public_snr_list = []
retracted_far_list = []
retracted_snr_list = []

# go through each superevent and split data based on number of pipelines triggered
for idx in range(len(superevent_list)):
        num = num_events[idx]
        pipes = num_pipelines[idx]
        # based on number of events within each superevent, find event with the best (minimum) FAR
        if pipes == 1:
                #interest_idx = 0
                temp_far = np.zeros(num)
                for temp_idx in range(num):
                        temp_far[temp_idx] = float(interest_list[idx][temp_idx])
                interest_idx = np.argmin(temp_far)
                far_1d_list.append(float(far_list[idx][interest_idx]))
                snr_1d_list.append(float(snr_list[idx][interest_idx]))
        elif pipes == 2:
                temp_far = np.zeros(num)
                for temp_idx in range(num):
                        temp_far[temp_idx] = float(interest_list[idx][temp_idx])
                interest_idx = np.argmin(temp_far)
                far_2d_list.append(float(far_list[idx][interest_idx]))
                snr_2d_list.append(float(snr_list[idx][interest_idx]))
        elif pipes == 3:
                temp_far = np.zeros(num)
                for temp_idx in range(num):
                        temp_far[temp_idx] = float(interest_list[idx][temp_idx])
                interest_idx = np.argmin(temp_far)
                far_3d_list.append(float(far_list[idx][interest_idx]))
                snr_3d_list.append(float(snr_list[idx][interest_idx]))
        elif pipes == 4:
                temp_far = np.zeros(num)
                for temp_idx in range(num):
                        temp_far[temp_idx] = float(interest_list[idx][temp_idx])
                interest_idx = np.argmin(temp_far)
                far_4d_list.append(float(far_list[idx][interest_idx]))
                snr_4d_list.append(float(snr_list[idx][interest_idx]))
        elif pipes >= 5:
                temp_far = np.zeros(num)
                for temp_idx in range(num):
                        temp_far[temp_idx] = float(interest_list[idx][temp_idx])
                interest_idx = np.argmin(temp_far)
                far_5d_list.append(float(far_list[idx][interest_idx]))
                snr_5d_list.append(float(snr_list[idx][interest_idx]))
        else:
                print("Invalid number of pipelines for superevent "+superevent_list[idx])
                pass
        if set([superevent_list[idx]]).intersection(real_public_events) != set([]):
                public_far_list.append(float(far_list[idx][interest_idx]))
                public_snr_list.append(float(snr_list[idx][interest_idx]))
        elif set([superevent_list[idx]]).intersection(retracted_events) != set([]):
                retracted_far_list.append(float(far_list[idx][interest_idx]))
                retracted_snr_list.append(float(snr_list[idx][interest_idx]))
        else:
                pass
        min_far_idx_list.append(interest_idx)
        far_plot_list.append(float(far_list[idx][interest_idx]))
        snr_plot_list.append(float(snr_list[idx][interest_idx]))

plt.rcParams.update({'font.size': 14})
#plt.semilogy(snr_plot_list, far_plot_list,'k,', label = "all events")
plt.semilogy(snr_1d_list, far_1d_list,'yo', label = "1 pipeline")
plt.semilogy(snr_2d_list, far_2d_list,'go', label = "2 pipelines")
plt.semilogy(snr_3d_list, far_3d_list,'ro', label = "3 pipelines")
plt.semilogy(snr_4d_list, far_4d_list,'bo', label = "4 pipelines")
#plt.semilogy(snr_5d_list, far_5d_list,'mo', label = "5+ pipelines")
plt.semilogy(public_snr_list, public_far_list, 'ko', mfc='none', label = "public event")
plt.semilogy(retracted_snr_list, retracted_far_list, 'kx', label = "retracted events")
plt.ylabel(r"$log_{10}(FAR)$")
plt.xlabel("SNR")
plt.title("Distribution of pipeline triggers in O3a")
plt.legend(loc=0)
plt.savefig("pipeline_distribution.png")
plt.clf()
#print(min_far_idx_list)
