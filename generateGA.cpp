#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <stdexcept>
#include <string>
#include <time.h>
#include <chrono>
#include <fstream>
using namespace std;

#define random(x) (rand()%x)


std::string exec(const char* cmd) {
    char buffer[128];
    std::string result = "";
    FILE* pipe = popen(cmd, "r");
    if (!pipe) throw std::runtime_error("popen() failed!");
    try {
        while (!feof(pipe)) {
            if (fgets(buffer, 128, pipe) != NULL)
                result += buffer;
            // else
            //     result += buffer;
        }
    } catch (...) {
        pclose(pipe);
        throw;
    }
    pclose(pipe);
    return result;
}

bool roll_dice(){
  if (random(2) == 1)
    return true;
  else
    return false;
}

int main()
{
  clock_t t1, t2;
  std::string res_build, res_run, res_build_base;
  system("python init.py");

  // res_build_base = exec("./make_cmd.sh");
  for (int i = 0; i < 1000; i++){
    std::cout << "building ..." << std::endl;
    res_build = exec("./make_cmd.sh");

    ofstream flagfile ("build_flag.txt");
    std::string build_success_info("[100%]");
    std::size_t found = res_build.find(build_success_info);

    if (found != std::string::npos)
    {
      std::cout << "build successful" <<std::endl;
      flagfile << 1;
    }
    else
    {
      std::cout << "abnormal build, raise a flag for python" << std::endl;
      flagfile << -1;
    }
    flagfile.close();

    std::cout << "running gemm ..." << std::endl;
    res_run = exec("./run_cmd.sh");
    system("python generateGA.py");
    std::cout << "This is the "<< i << " iteration"<< std::endl;
    std::cout << res_build << std::endl;
    std::cout << res_run << std::endl;
  }
  // t1 = clock();
  // t2 = clock();
  // std::cerr << " took "
  // 	          << (static_cast<double>(t2) - static_cast<double>(t1)) / static_cast<double>(CLOCKS_PER_SEC)
  // 	          << " seconds." << std::endl;
  // std::cout << finish <<" seconds" << std::endl;
  // duration = (double)(finish - start) / CLOCKS_PER_SEC;

  // res = exec("time ls");

  return 0;
}
