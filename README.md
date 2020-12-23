# [xhls] sqrt_cordic

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Usage](#usage)
* [References](#References)
* [Contributing](#contributing)



<!-- ABOUT THE PROJECT -->
## About The Project
Using high level synthesis to accelerate square calculation by CORDIC method. 

**Directory structure**
```
README.md
code/
    cordic_defines.h
    cordic_isqrt.cpp
    cordic_sqrt.cpp
    float_sqrt.cpp
    top_magnitude.cpp
code_opt/
    cordic_defines.h
    cordic_isqrt.cpp
    cordic_sqrt.cpp
    float_sqrt.cpp
    top_magnitude.cpp
testdata/
    test_main.cpp
    pynq_python/
        cordic.py
script/
    run_sqrt_cordic_hls_script.tcl
impl/
    func1_process_magnit_csynth.rpt
    func2_process_magnit_csynth.rpt
    func3_process_magnit_csynth.rpt
    func4_process_magnit_csynth.rpt
    process_magnitude_co_csynth.rpt
    top_process_magnitude_csynth.rpt
```

<!-- USAGE EXAMPLES -->
## Usage

1. fpga board setup

We use **Xilinx ZedBoard Evaluation and Development Kit** to evaulate this project

2. using HLS vivado to simulation and synthesis

3. export RTL

4. generate .bit from vivado

3. python test
```shell 
 python cordic.py
```
## References
* https://github.com/Xilinx/HLx_Examples

<!-- CONTRIBUTING -->
## Contributing
* fix negtive slack
* experiment on different scale floating number and CORDIC
