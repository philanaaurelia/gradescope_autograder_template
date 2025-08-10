BINARIES= main
TESTS= main1 main2 main3 main4 main5

all:	main

main:
	$(foreach var,$(TESTS),g++ -std=c++17 $(var).cpp -o $(var);)

clean:
	/bin/rm -rf *.o ${BINARIES}