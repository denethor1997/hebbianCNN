"""
Author: Raphael Holca-Lamarre
Date: 26/05/2015

This code creates a hebbian convolutional neural network object and trains it on the MNIST dataset. The network consists of four layers: a convolutional layer, a subsampling layer, a feedforward layer and a classification layer. Only three of these layers have modifiable weights: the convolution, feedforward and classification layers. The learning rule is a hebbian learning rule augmented with a learning mechanism inspired from dopamine signalling in animal cortex.
"""

import os
import matplotlib
if 'Documents' in os.getcwd():
	matplotlib.use('Agg') #to avoid sending plots to screen when working on the servers
import numpy as np
import helper
import hebbian_cnn
import time
import datetime

reload(helper)
reload(hebbian_cnn)

""" create hebbian convolution neural network """
net = hebbian_cnn.Network(	conv_dHigh			= 2.7,
							conv_dMid 			= 1.8,
							conv_dNeut 			= -0.07,
							conv_dLow 			= -1.8,
							feedf_dHigh			= 4.5,
							feedf_dMid 			= 0.02,
							feedf_dNeut 		= 0.01, 
							feedf_dLow 			= -2.0,
							name 				= 'test_lr_conv',
							n_epi_crit 			= 1,
							n_epi_dopa 			= 0,
							A 					= 900.,
							lr_conv				= 0.01,
							lr_feedf			= 0.01,
							t 					= 0.01,
							batch_size 			= 196,
							conv_map_num 		= 6,
							conv_filter_side	= 5,
							feedf_neuron_num	= 49,
							explore				= 'feedf',
							noise_explore		= 0.2,
							classifier			= 'neural_prob',
							init_file 			= '',
							seed 				= 952
							)

""" load and pre-process training and testing images """
images_train, labels_train, images_test, labels_test = helper.load_images(	
																			# classes 		= np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int),
																			classes 		= np.array([4, 7, 9], dtype=int),
																			dataset_train	= 'test',
																			dataset_path 	= '/Users/raphaelholca/Documents/data-sets/MNIST',
																			pad_size 		= (net.conv_filter_side-1)/2,
																			load_test 		= False
																			)

""" train network """
perf_train = net.train(images_train, labels_train)

""" test network """
perf_test = net.test(images_test, labels_test)

""" plot weights of the network """
plots = helper.generate_plots(net)

""" save network to disk """
save_name = helper.save(net, overwrite=False, plots=plots)

""" print run time """
print '\nrun name:\t' + save_name
print 'start time:\t' + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(net._train_start))
print 'end time:\t' + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(net._train_stop))
print 'train time:\t' +  str(datetime.timedelta(seconds=net.runtime))




