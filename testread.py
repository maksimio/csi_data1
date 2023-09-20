import csiread

csifile = './1_distortion_objects/1/empty.dat'
csidata = csiread.Atheros(csifile, nrxnum=5, ntxnum=5, tones=56)
print('Hi')
csidata.read(endian='big')
print(csidata.csi.shape)
print('Bye')
