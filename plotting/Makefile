include config.mk

all : o5000 o10000 o15000 o20000

.PHONY : o5000 o10000 o15000 o20000 clean

o5000 : $(SRC) $(DATA_5000)
	$(SRC_EXE_5000)

o10000 : $(SRC) $(DATA_10000)
	$(SRC_EXE_10000)

o15000 : $(SRC) $(DATA_15000)
	$(SRC_EXE_15000)

o20000 : $(SRC) $(DATA_20000)
	$(SRC_EXE_20000)

clean :
	rm ./DT5000/*.png
	rm ./DT5000/*.eps
	rm ./DT10000/*.png
	rm ./DT10000/*.eps
	rm ./DT15000/*.png
	rm ./DT15000/*.eps
	rm ./DT20000/*.png
	rm ./DT20000/*.eps
