#!/bin/bash

display_help() {
   # Display Help
   echo "======================================"
   echo "  CUSTOMER SEGMENT "
   echo "======================================"
   echo "---commands---"
   echo "help                   Print CLI help"
   echo "start                  Generate Customer Segmentation"
   echo "generate_cust_data     Generate input data"
   echo "tst                    Test main code"
   echo "validate-prereqs       Validate pre-reqs installed (python3, pip3)"
}

validate_prereqs() {
   python3 --version >/dev/null 2>&1
   if [ $? -ne 0 ]; then
      echo -e "Python3 is not installed. \xE2\x9D\x8C"
   else
      echo -e "Python3 is Installed \xE2\x9C\x94"
   fi

   pip3 --version >/dev/null 2>&1
   if [ $? -ne 0 ]; then
      echo -e "Pip3 is not installed. \xE2\x9D\x8C"
   else
      echo -e "Pip3 is Installed. \xE2\x9C\x94"
   fi
}

install_libs() {
   pip3 install -r requirements.txt
}

case "$1" in
validate-prereqs)
   validate_prereqs
   ;;

generate_cust_data)
    install_libs
    python3 src/data_generator.py
    ;;

start)
    install_libs
    python3 main.py
    ;;

test)
    install_libs
    pytest tests/test_segment.py
    ;;

help)
   display_help
   ;;

esac