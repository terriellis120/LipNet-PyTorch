gpu = '3'
random_seed = 0
trn_vid_path = '/ssd/GRID/lip_unseen/train'
val_vid_path = '/ssd/GRID/lip_unseen/val'
anno_path = '/ssd/GRID/GRID_align_txt'
vid_padding = 75
txt_padding = 200
base_lr = 1e-4
batch_size = 120
num_workers = 8
max_epoch = 10000
display = 10
test_step = 1000
save_prefix = 'weights/LipNet_unseen'
is_optimize = True
weights = 'pretrain/LipNet_unseen_loss_0.4092428684234619_wer_0.13634992458521872_cer_0.07181944359354399.pt'
