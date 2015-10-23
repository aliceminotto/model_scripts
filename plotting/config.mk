SRC=./clusterV.py

SRC_EXE_5000=export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/tsl/software/testing/gsl/1.16/x86_64/bin/lib; \
bsub -q TSL-Prod128 -We 1 "source python-2.7.4; python /usr/users/TSL_20/minottoa/change_DT_Qi/clusterV.py /usr/users/TSL_20/minottoa/change_DT_Qi/DT5000/ 20 40"

SRC_EXE_10000=export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/tsl/software/testing/gsl/1.16/x86_64/bin/lib; \
bsub -q TSL-Prod128 -We 1 "source python-2.7.4; python /usr/users/TSL_20/minottoa/change_DT_Qi/clusterV.py /usr/users/TSL_20/minottoa/change_DT_Qi/DT10000/ 20 20"

SRC_EXE_15000=export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/tsl/software/testing/gsl/1.16/x86_64/bin/lib; \
bsub -q TSL-Prod128 -We 1 "source python-2.7.4; python /usr/users/TSL_20/minottoa/change_DT_Qi/clusterV.py /usr/users/TSL_20/minottoa/change_DT_Qi/DT15000/ 20 13"

SRC_EXE_20000=export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/tsl/software/testing/gsl/1.16/x86_64/bin/lib; \
bsub -q TSL-Prod128 -We 1 "source python-2.7.4; python /usr/users/TSL_20/minottoa/change_DT_Qi/clusterV.py /usr/users/TSL_20/minottoa/change_DT_Qi/DT20000/ 20 10"

DATA_5000=./DT5000

DATA_10000=./DT10000

DATA_15000=./DT15000

DATA_20000=./DT20000
