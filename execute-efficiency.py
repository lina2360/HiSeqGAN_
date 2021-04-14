import os
import sys
import argparse
import csv 
import datetime
import logging

parser = argparse.ArgumentParser(description='manual to this script')
# parser.add_argument('--tau1', type=float, default = 0.1)
# parser.add_argument('--tau2', type=float, default=0.01)
parser.add_argument('--data', type=str, default=None)
# parser.add_argument('--target', type=str, default = None)
# parser.add_argument('--generated_num', type=int, default=960)
# parser.add_argument('--total_batch', type=int, default = 100)
# parser.add_argument('--batch_size', type=int, default=32)
# parser.add_argument('--seq_length', type=int, default = 96)
# parser.add_argument('--input_type', type=int, default = 96)


args = parser.parse_args()
prefix = args.data
# target = args.target
# generated_num = args.generated_num
# total_batch = args.total_batch
# batch_size = args.batch_size
# seq_length = args.seq_length
# input_type = args.input_type
current_path = os.getcwd()
print('Current:',current_path)

##############################
# RNN Settings
##############################
# Run RNN 
def rnn_all_wmse(name,input_type):
    try:
        # os.system('python ./programs/RNN/app_all.py --name=%s' % (name))
        os.system('python ./programs/RNN/app_all.py --name=%s --input_type=%s' % (name,input_type))
        # logging.info(output)
    except Exception as e:
        print('Error:',e)

def rnn_all_center(name,input_type):
    try:
        # os.system('python ./programs/RNN/app_all.py --name=%s' % (name))
        os.system('python ./programs/RNN/app_all_item_center_point_real.py --name=%s --input_type=%s' % (name,input_type))
        # logging.info(output)
    except Exception as e:
        print('Error:',e)

def rnn_all_week(name,input_type):
    try:
        # os.system('python ./programs/RNN/app_all.py --name=%s' % (name))
        os.system('python ./programs/RNN/app_all_week.py --name=%s --input_type=%s' % (name,input_type))
        # logging.info(output)
    except Exception as e:
        print('Error:',e)


rnn_all_wmse(prefix,'rnn')
# rnn_all_center(prefix,'rnn')
# rnn_all_wmse(prefix,'seqgan')
# rnn_all_center(prefix,'seqgan')

# rnn_all_week(prefix,'rnn')
# rnn_all_week(prefix,'seqgan')