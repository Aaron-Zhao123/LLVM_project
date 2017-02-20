import random
import subprocess
import os
import pickle
# stream = file('Users/aaron/llvm/tools/clang/lib/CodeGen/BackendUtil.cpp','w')
data_file_pkl = '/Users/aaron/Projects/L25_miniproject/test/data_for_ga/ga2/data_each_generation.pkl'
def main():
    '''Vary this depending on the location of your llvm'''
    stream = file('/Users/aaron/llvm/tools/clang/lib/CodeGen/BackendUtil.cpp','w')

    with open('code_first_part.txt', 'r') as myfile:
        read_one = myfile.read()

    with open('code_second_part.txt', 'r') as myfile:
        read_two = myfile.read()

    FPM_passes = {
    'Discriminator':        '  FPM.add(createAddDiscriminatorsPass());\n',
    'Verify':               '  if (CodeGenOpts.VerifyModule){FPM.add(createVerifierPass());}\n',
    'AndersAA':             '  FPM.add(createCFLAndersAAWrapperPass());\n',
    'SteensAA':             '  FPM.add(createCFLSteensAAWrapperPass());\n',
    'TypeBasedAA':          '  FPM.add(createTypeBasedAAWrapperPass());\n',
    'ScopedNoAA':           '  FPM.add(createScopedNoAliasAAWrapperPass());\n',
    'SimCFG':               '  FPM.add(createCFGSimplificationPass());',
    'SROAP':                '  FPM.add(createSROAPass());\n',
    'EarlyCSE':             '  FPM.add(createEarlyCSEPass());\n',
    'GVNHoist':             '  FPM.add(createGVNHoistPass());\n',
    'LowerEIP':             '  FPM.add(createLowerExpectIntrinsicPass());\n'
    }

    MPM_passes = {
    'LibraryInfo':                  '  MPM.add(new TargetLibraryInfoWrapperPass(*TLII));\n',
    'ForceSetFunctionAttributes':   '  MPM.add(createForceFunctionAttrsLegacyPass());\n',
    'AndersAA':                     '  MPM.add(createCFLAndersAAWrapperPass());\n',
    'SteensAA':                     '  MPM.add(createCFLSteensAAWrapperPass());\n',
    'TypeBasedAA':                  '  MPM.add(createTypeBasedAAWrapperPass());\n',
    'ScopedNoAA':                   '  MPM.add(createScopedNoAliasAAWrapperPass());\n',
    'InterproSparseCondConstProp':  '  MPM.add(createIPSCCPPass());\n',
    'GlobalVariableOpt':            '  MPM.add(createGlobalOptimizerPass());\n',
    'MemoryToReg':                  '  MPM.add(createPromoteMemoryToRegisterPass());\n',
    'DeadArgElim':                  '  MPM.add(createDeadArgEliminationPass());\n',
    'CombineRedundantInstru_ture':  '  MPM.add(createInstructionCombiningPass(true));\n',
    'CombineRedundantInstru_false': '  MPM.add(createInstructionCombiningPass(false));\n',
    'SimplifyCFG':                  '  MPM.add(createCFGSimplificationPass());\n',
    'IndirectCallPromotion':        '  MPM.add(createPGOIndirectCallPromotionLegacyPass());\n',
    'GlobalAliasAnalysis':          '  MPM.add(createGlobalsAAWrapperPass());\n',
    'RemoveDeadEHInfo':             '  MPM.add(createPruneEHPass());\n',
    'Inline':                       '  MPM.add(PMBuilder.Inliner);\n  PMBuilder.Inliner = nullptr;\n',
    'DeduceFunctionAttributes:':    '  MPM.add(createPostOrderFunctionAttrsLegacyPass());\n',
    'SROA':                         '  MPM.add(createSROAPass());\n',
    'EarlyCSE':                     '  MPM.add(createEarlyCSEPass());\n',
    'SpecuExecIfBranchDiverges':    '  MPM.add(createSpeculativeExecutionIfHasBranchDivergencePass());\n',
    'ThreadJump':                   '  MPM.add(createJumpThreadingPass());\n',
    'Value Propogaton':             '  MPM.add(createCorrelatedValuePropagationPass());\n',
    'LibCallSink':                  '  MPM.add(createLibCallsShrinkWrapPass());\n',
    'TailCallElim':                 '  MPM.add(createTailCallEliminationPass());\n',
    'ReassociateExpr':              '  MPM.add(createReassociatePass());\n',
    'LoopRotate':                   '  MPM.add(createLoopRotatePass(PMBuilder.SizeLevel == 2 ? 0 : -1));\n',
    'HoistLoopInvariants':          '  MPM.add(createLICMPass());\n',
    'LoopUnswitch':                 '  MPM.add(createLoopUnswitchPass(PMBuilder.SizeLevel || PMBuilder.OptLevel < 3));\n',
    'InductVarSimplify':            '  MPM.add(createIndVarSimplifyPass());\n',
    'RecognizeLoopIdioms':          '  MPM.add(createLoopIdiomPass());\n',
    'DeleteDeadLoops':              '  MPM.add(createLoopDeletionPass());\n',
    'UnrollSmallLoops':             '  MPM.add(createSimpleLoopUnrollPass());\n',
    'MergeLdStMotion':              '  MPM.add(createMergedLoadStoreMotionPass());\n',
    'SparseCondConstPropogate':     '  MPM.add(createSCCPPass());\n',
    'BitTrackingDeadCode':          '  MPM.add(createBitTrackingDCEPass());\n',
    'DeadStoreElem':                '  MPM.add(createDeadStoreEliminationPass());\n',
    'AggressiveDeadCodeElem':       '  MPM.add(createAggressiveDCEPass());\n',
    'BarrierNoOP':                  '  MPM.add(createBarrierNoopPass());\n',
    'ElimAvailableExternallyGloabl':'  MPM.add(createEliminateAvailableExternallyPass());\n',
    'GlobalOpt':                    '  MPM.add(createGlobalOptimizerPass());\n',
    'FloatToInt':                   '  MPM.add(createFloat2IntPass());\n',
    'LoopDistribute':               '  MPM.add(createLoopDistributePass(false));\n',
    'LoopVectorization':            '  MPM.add(createLoopVectorizePass(true, true));\n',
    'LoopVectorization_two':        '  MPM.add(createLoopVectorizePass(true, false));\n',
    'LoopVectorization_three':      '  MPM.add(createLoopVectorizePass(false, true));\n',
    'LoopVectorization_four':       '  MPM.add(createLoopVectorizePass(false, false));\n',
    'SLPVectorize':                 '  MPM.add(createSLPVectorizerPass());\n',
    'UnrollLoops':                  '  MPM.add(createLoopUnrollPass());\n',
    'AlignmentFromAssumptions':     '  MPM.add(createAlignmentFromAssumptionsPass());\n',
    'StripUnusedFuncProto':         '  MPM.add(createStripDeadPrototypesPass());\n',
    'DeadGlobalElem':               '  MPM.add(createGlobalDCEPass());\n',
    'MergeDupGlobalConstant':       '  MPM.add(createConstantMergePass());\n',
    'LoopSink':                     '  MPM.add(createLoopSinkPass());\n',
    'InstructSimplifier':           '  MPM.add(createInstructionSimplifierPass());\n',
    'MergeFunction':                '  MPM.add(createMergeFunctionsPass());\n',
    'FunctionInline':               '  IP.DefaultThreshold = 75;\n  IP.HintThreshold = 325;\n  MPM.add(createFunctionInliningPass(IP));\n',
    'FunctionInline_hs':            '  IP.DefaultThreshold = 200;\n  IP.HintThreshold = 325;\n  MPM.add(createFunctionInliningPass(IP));\n',
    'FunctionInline_sh':            '  IP.DefaultThreshold = 75;\n  IP.HintThreshold = 525;\n  MPM.add(createFunctionInliningPass(IP));\n',
    'FunctionInline_ls':            '  IP.DefaultThreshold = 20;\n  IP.HintThreshold = 325;\n  MPM.add(createFunctionInliningPass(IP));\n',
    'FunctionInline_sl':            '  IP.DefaultThreshold = 75;\n  IP.HintThreshold = 125;\n  MPM.add(createFunctionInliningPass(IP));\n',
    'ArgumentPromotion':            '  MPM.add(createArgumentPromotionPass());\n',
    'RerollLoops':                  '  MPM.add(createLoopRerollPass());\n',
    'BBVectorize':                  '  MPM.add(createBBVectorizePass());\n',
    'LoadCombine':                  '  MPM.add(createLoadCombinePass());\n',
    'MemcopyOpt':                   '  MPM.add(createMemCpyOptPass());\n',
    'LoopLoadElem':                 '  MPM.add(createLoopLoadEliminationPass());\n',
    'LowerIntrinsic':               '  MPM.add(createLowerExpectIntrinsicPass());\n',
    'Verifier':                     '  MPM.add(createVerifierPass());\n'
    }

    MPM_keys = MPM_passes.keys()
    FPM_keys = FPM_passes.keys()

    '''add an id info dict'''
    MPM_ID = {}
    index =  1
    for key in MPM_keys:
        MPM_ID[index] = key
        index += 1

    FPM_ID = {}
    for key in FPM_keys:
        FPM_ID[index] = key
        index += 1


    print('Number of passes in MPM is {}'.format(len(MPM_keys)))
    print('Number of passes in FPM is {}'.format(len(FPM_keys)))


    MPMpasses_info_path = "MPM_passes.pkl"
    FPMpasses_info_path = "FPM_passes.pkl"
    data_path = "data.pkl"
    data_generation_path = "data_each_generation.txt"


    # take the previous and basic pass
    if os.path.isfile(MPMpasses_info_path):
        with open(MPMpasses_info_path, 'rb') as f:
            MPM_index_list = pickle.load(f)

    if os.path.isfile(FPMpasses_info_path):
        with open(FPMpasses_info_path, 'rb') as f:
            FPM_index_list = pickle.load(f)



    # save old passes sequence, build time, runtime in a file
    # stores global data info
    data_info = []

    if os.path.isfile(data_path):
        with open(data_path, 'rb') as f:
            data_info = pickle.load(f)
        (run_time, build_time) = collect_time_info()
        with open(data_path, 'wb') as f:
            data_info.append((MPM_index_list, FPM_index_list, run_time, build_time))
            pickle.dump(data_info, f)
    else:
        with open(data_path, 'wb') as f:
            pickle.dump([],f)

    # randomly generate a pass

    MPM_index_list = []
    tmp = []
    FPM_index_list = [FPM_keys.index('Verify')]
    with open(data_file_pkl, 'rb') as f:
        tmp = pickle.load(f)
    MPM_index_list = tmp[0]
    tmp.pop(0)
    with open(data_file_pkl, 'wb') as f:
        pickle.dump(tmp,f)


    print('MPM list : {}'.format(MPM_index_list))
    print('FPM list : {}'.format(FPM_index_list))
    print('we have {} mutations'.format(len(data_info)))

    FPM_seleted_passes = index_to_passes(FPM_index_list, FPM_keys, FPM_passes)
    MPM_seleted_passes = index_to_passes(MPM_index_list, MPM_keys, MPM_passes)

    code_snippet = FPM_seleted_passes + MPM_seleted_passes

    stream.write(read_one+code_snippet+read_two)

    with open(MPMpasses_info_path, 'wb') as f:
        pickle.dump(MPM_index_list, f)
    with open(FPMpasses_info_path, 'wb') as f:
        pickle.dump(FPM_index_list, f)

    # for key in FPM_keys:
    #     code_snippet = code_snippet + FPM_passes[key]
    #
    # for key in MPM_keys:
    #     code_snippet = code_snippet + MPM_passes[key]
    #
    # for key in MPM_keys:
    #     if (key != 'Inline'):
    #         code_snippet = code_snippet + MPM_passes[key]
    #
    # print (code_snippet)

    # make_cmd = './make_cmd.sh'
    # out = subprocess.call(make_cmd, shell = True)
    # print (out)
def index_to_passes(index_list, keys, collections):
    Passes = ''
    for index in index_list:
        Passes = Passes + collections[keys[index]]
    return Passes

def collect_time_info():
    run_time_path = "runtime.txt"
    build_time_path = "buildtime.txt"
    run_time_error_path = "run_flag.txt"
    build_time_error_path = "build_flag.txt"
    with open(run_time_path, 'rb') as f:
        run_time_info = f.read()
    with open(build_time_path, 'rb') as f:
        build_time_info = f.read()
    # print (run_time_info)
    # print (build_time_info)
    # print (run_time_info.split())
    with open(run_time_error_path) as f:
        runtime_error = f.read()
    with open(build_time_error_path) as f:
        buildtime_error = f.read()
    if (len(runtime_error) > 10):
        print("there is a runtime error, set runtime info to dummy high value")
        run_time = 1000
    else:
        run_time = compute_cpu_time(run_time_info)
    if (int(buildtime_error) == -1):
        print("there is a build error, set runtime info to dummy high value")
        build_time = 1000
    else:
        build_time = compute_cpu_time(build_time_info)
    return (run_time, build_time)

def compute_cpu_time(info_str):
    cpu_time = 0
    flag_usr = 0
    flag_sys = 0
    usr_time = 0
    sys_time = 0
    for item in info_str.split():
        if (flag_usr == 1):
            flag_usr = 0
            # print('usr info is {}'.format(item))
            # print (item[0:1])
            # print (item[2:len(item)-1])
            usr_time = float(item[0:1])*60 + float(item[2:len(item)-1])
        if (flag_sys == 1):
            # print('sys info is {}'.format(item))
            flag_sys = 0
            sys_time = float(item[0:1])*60 + float(item[2:len(item)-1])
        if (item == 'user'):
            flag_usr = 1
        if (item == 'sys'):
            flag_sys = 1
            # cpu_time +=
    cpu_time = usr_time + sys_time
    return cpu_time

# def strip_time_in_seconds(str):


if __name__ == "__main__":
    main()
