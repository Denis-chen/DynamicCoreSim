# DynamicCoreSim
A research based project for ECE597: Adv. Computer Architecture at Rose-Hulman Inst. of Tech. Attempts to analyze the performance benefits of a dynamic processor core.


## Pre-Requisites
- You must have gcc
- You must create a file "splash2/codes/Makefile.dir" that includes the line "BASEDIR := <your base directory>" (this file is in the .gitignore)

---------------------------------------
David's Findings as of January 19, 2015
---------------------------------------
1. Tried using the "arm-linux-gnueabihf-gcc" compiler to compile OCEA to arm code was unable to get it working throws following error:
/usr/lib/gcc-cross/arm-linux-gnueabihf/4.8/../../../../arm-linux-gnueabihf/bin/ld: cannot find crt1.o: No such file or directory
/usr/lib/gcc-cross/arm-linux-gnueabihf/4.8/../../../../arm-linux-gnueabihf/bin/ld: cannot find crti.o: No such file or directory
/usr/lib/gcc-cross/arm-linux-gnueabihf/4.8/../../../../arm-linux-gnueabihf/bin/ld: cannot find -lm
/usr/lib/gcc-cross/arm-linux-gnueabihf/4.8/../../../../arm-linux-gnueabihf/bin/ld: cannot find -lpthread
/usr/lib/gcc-cross/arm-linux-gnueabihf/4.8/../../../../arm-linux-gnueabihf/bin/ld: cannot find -lc
collect2: error: ld returned 1 exit status
make: *** [OCEAN] Error 1

2. Help for se.py is very usefull and provides many parameters: build/X86/gem5.opt configs/example/se.py -h

3. The available CPU types such as InOrder or OutOfOrder can be seen with: build/X86/gem5.opt configs/example/se.py --list-cpu-types

4. Additional cpus can be specified when the simulator is being built with the CPU_MODELS flag

5. Usefull options to se.py
    --cpu-type=CPU_MODEL
    -o "String of parameters for benchmark"
        ->Pass paramaters to the benchmark code for ocean -p# specifies number of cores where # is a power of two
    -n "specify number of CPUS to be used by simulator"
    Example.) build/X86/gem5.opt configs/example/se.py --cpu-type=AtomicSimpleCPU -n 4 -o "-p4" -c ../DynamicCoreSim/splash2/codes/apps/ocean/non_contiguous_partitions/OCEAN
