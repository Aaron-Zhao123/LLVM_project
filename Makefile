bench=polybench-c-4.2.1-beta

cc=/usr/groups/acs-software/L25/llvm-release/bin/clang
opt=/usr/groups/acs-software/L25/llvm-release/bin/opt

ccflags=-Xclang -load -Xclang ./SimplePass/Debug/SimplePass.so -c
inc= -I$(bench)/utilities -I$(bench)/linear-algebra/kernels/atax $(bench)/utilities/polybench.c

file=$(bench)/linear-algebra/kernels/2mm/2mm.c
irfile=2mm.ll

all:
	$(cc)  $(ccflags) $(inc) $(file) -O3
opt:
$(opt) $(irfile) -debug-pass=Structure -o $(irfile) -dse -gvn -sink -instcombine -constprop -die -mergefunc -mergefunc -lowerswitch

ir:
	$(cc) -S -emit-llvm $(inc) $(file) -O0


f:
	$(cc) opt.ll -o opt

help:
	$(opt) --help
