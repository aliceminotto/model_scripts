include config.mk

all : $(SRC)
	@while [ -z "$$OPTIONS" ]; do \
	echo "insert option for the simulation, mandatory path_to_main_directory number_of_runs number_of_jumps interval_between_jumps, n to exit" && read -r OPTIONS; \
	done; \
	if [ "$$OPTIONS" = "n" ]; then exit 0; else $(SRC_EXE); fi;
