export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/tsl/software/testing/gsl/1.16/x86_64/bin/lib
bsub -q TSL-Prod128 -We 1 "source python-2.7.4; python /usr/users/TSL_20/minottoa/model_scripts/second_model/MODELS/modello/check_newmodfigs.py"
