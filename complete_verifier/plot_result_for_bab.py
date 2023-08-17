# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:07:33 2023

@author: hsc
"""
import glob
import numpy as np
import matplotlib.pyplot as plt
import os
#ret.append([imag_idx, l, nodes, time_cost, new_idx, pidx, u, attack_margin[pidx] if attack_margin is not None else np.inf])

pidx_labels={-3: 'pgd attack ',-1:"incomplete success"}
for i in range(10):
    pidx_labels[i]=f'{i}'


imag_idx, l, nodes, time_cost, new_idx, pidx, u, attack_margin=[i for i in range(8)]


#ret 记录了对imag_idx:0-99图像，针对目标标签为0-9进行验证的结果
names=[

       'Verified_ret_Verified_ret_[mnist_9_200]_start=0_end=100_iter=20_b=1_timeout=40_branching=max_amb-max-3_lra-init=0.1_lra=0.01_lrb=0.05_PGD=skip_rtim=2023-05-30_175313.npy'
      ,'Verified_ret_Verified_ret_[mnist_9_200]_start=0_end=100_iter=20_b=1_timeout=40_branching=rlm-max-3_lra-init=0.1_lra=0.01_lrb=0.05_PGD=skip_rtim=2023-05-30_163526.npy' 
      ,'Verified_ret_Verified_ret_[mnist_9_200]_start=0_end=100_iter=20_b=1_timeout=40_branching=rlm-max-3_lra-init=0.1_lra=0.01_lrb=0.05_PGD=skip_rtim=2023-05-30_175231.npy'
      ,'Verified_ret_Verified_ret_[mnist_9_200]_start=0_end=100_iter=5_b=1_timeout=40_branching=random-max-3_lra-init=0.1_lra=0.008_lrb=0.05_PGD=skip_rtim=2023-05-30_154802.npy'
      ,'Verified_ret_Verified_ret_[mnist_9_200]_start=0_end=100_iter=5_b=1_timeout=40_branching=babsr-max-3_lra-init=0.1_lra=0.01_lrb=0.05_PGD=skip_rtim=2023-05-30_154417.npy'
    # ,'Verified_ret_[mnist_9_200]_start=0_end=100_norm=0.015_bIt=20_bat=1_timeout=40_branching=fsb_rdop=max_cndN=3_Alra=0.1_Blra=0.01_Blrb=0.05_PGD=skip_T=230531_121552.npy'
]
names=glob.glob(r'D:\wordspace\python\alpha-beta-CROWN\complete_verifier\Verified_ret*mnist_9_200*_T=230601_*.npy')

for ret_file in names:
  #  print(os.path.basename(ret_file))
    #'Verified_ret_[mnist_9_200]_start=0_end=100_iter=5_b=8_timeout=40_branching=random-max-3_lra-init=0.1_lra=0.01_lrb=0.05_PGD=skip_rtim=2023-05-22_233747.npy'
    ret = np.load(ret_file)
   # ret_file=ret_file.replace('-max-','_max=')

    methodstID = ret_file.find('branching=')
    strategy = ret_file[methodstID+len('branching='):ret_file.find('_rdop',methodstID)]
    t_ret=ret[ret[:,5]!=-1]
    
    #(1)证伪的
    falsified_idx = ret[:,0][ret[:,6]<0]
    #(2)总验证时间
    total_time =  ret[:,3][ret[:,1]>0].sum() #ret[:, 3][ret[:,6]<0].sum() +ret[:, 3][ret[:,1]>0].sum()
    average_time = total_time/len(ret[:,1]>0)
    
    #(4)总验证数量    
    attack_success = sum(ret[:,6]<0) #u<=0
    verified_success =  sum(ret[:,1]>0) #l>0    
    failed = sum([1 if ret[i,1]<0 and ret[i,6]>0 else 0 for i in range(len(ret))] )
    (4)
    total_p = 1000
    success_n = attack_success + verified_success
    #assert(total_p-timeout - attack_success - verified_success==0)
    print(f'{strategy:10s} totol: {len(ret)} verified: {verified_success}/{success_n/len(ret):0.3f}  falsified: {attack_success}  timeout: {failed}  runtime:{average_time:.3f},arracy:{success_n/len(ret) :0.3f}')
 
#[pidx_labels[int(i)] for i in ret[:,5]]


#for i in ret:
#    imag_idx, l, nodes, time_cost, new_idx, pidx, u, attack_margin = i
    
