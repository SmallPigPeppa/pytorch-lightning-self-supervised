from pl_bolts.datamodules import ImagenetDataModule
import os
# IMAGENET_PATH='/data/datasets/imagenet'
IMAGENET_PATH='/share/datasets/torch_ds/imagenet/'
META_PATH='.'


# a=os.listdir(os.path.join(IMAGENET_PATH, 'train'))
# print(a)
# ,meta_dir=META_PATH
dm = ImagenetDataModule(data_dir=IMAGENET_PATH)
dm.prepare_data()
# loader=dm.train_dataloader()
# print(dm)
# print(loader)
# a=next(iter(loader))
# print(a)
print(dm)





# model = LitModel()
#
# Trainer().fit(model, datamodule=dm)