export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/tsl/software/testing/gsl/1.16/x86_64/bin/lib; \
bsub -q TSL-Prod128 -We 1 "source python-2.7.4; python /usr/users/TSL_20/minottoa/model_scripts/plotting/scatter_version2.py ~/change_DT_Qi/DT5000/ ~/change_DT_Qi/DT10000/ ~/change_DT_Qi/DT15000/ ~/change_DT_Qi/DT20000/ ~/new/ 50"
