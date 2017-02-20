#!/bin/bash
cd /Users/aaron/Projects/L25_miniproject/test/polybench-c-3.2
# (~/llvm/build/bin/clang -O3 -I utilities -I linear-algebra/kernels/gemm utilities/polybench.c linear-algebra/kernels/gemm/gemm.c -DLARGE_DATASET -DPOLYBENCH_TIME -o gemm_time) 2> run_flag.txt
# (~/llvm/build/bin/clang -O3 -I utilities -I linear-algebra/kernels/3mm utilities/polybench.c linear-algebra/kernels/3mm/3mm.c -DPOLYBENCH_TIME -o 3mm_time) 2> run_flag.txt
# (~/llvm/build/bin/clang -O3 -I utilities -I linear-algebra/kernels/2mm utilities/polybench.c linear-algebra/kernels/2mm/2mm.c -DPOLYBENCH_TIME -o 2mm_time) 2> run_flag.txt
# (~/llvm/build/bin/clang -O3 -I utilities -I linear-algebra/kernels/gesummv utilities/polybench.c linear-algebra/kernels/gesummv/gesummv.c -DLARGE_DATASET -DPOLYBENCH_TIME -o gesummv_time) 2> run_flag.txt
# (~/llvm/build/bin/clang -O3 -I utilities -I linear-algebra/kernels/atax utilities/polybench.c linear-algebra/kernels/atax/atax.c -DLARGE_DATASET -DPOLYBENCH_TIME -o atax_time) 2> run_flag.txt
(~/llvm/build/bin/clang -O3 -I utilities -I linear-algebra/kernels/trmm utilities/polybench.c linear-algebra/kernels/trmm/trmm.c -DLARGE_DATASET -DPOLYBENCH_TIME -o trmm_time) 2> run_flag.txt
# (~/llvm/build/bin/clang -O3 -I utilities -I linear-algebra/kernels/syr2k utilities/polybench.c linear-algebra/kernels/syr2k/syr2k.c -DLARGE_DATASET -DPOLYBENCH_TIME -o syr2k_time) 2> run_flag.txt
# ./utilities/time_benchmark.sh ./gemm_time > runtime.txt
# ~/llvm/build/bin/clang -O3 -I utilities -I linear-algebra/kernels/gemm utilities/polybench.c linear-algebra/kernels/gemm/gemm.c -DPOLYBENCH_TIME -o gemm_time
# (time ./gemm_time) 2> runtime.txt
(time ./trmm_time) 2> runtime.txt
cp runtime.txt /Users/aaron/Projects/L25_miniproject/test
cp run_flag.txt /Users/aaron/Projects/L25_miniproject/test
rm runtime.txt
rm run_flag.txt
cd /Users/aaron/Projects/L25_miniproject/test
