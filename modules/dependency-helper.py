# -*- coding: utf-8 -*-
#Written by Caleb C. in 2022 for Carthage Space Sciences | WSGC | NASA
#This script will get the dependencies for fossS/MPG related Python projects.
import subprocess
import sys
from formatmodule import bcolors, bsymbols

modules_base = ['wheel', 'halo']
modules_dependencies = ['struct', 'usb.core', 'pandas', 'matplotlib', 'statsmodels', 'ttkbootstrap', 'scipy', 'bitarray']
fail = False

def basic():
    global modules_base
    print(f"{bsymbols.info} {bcolors.HEADER}mpg-foss: Checking dependencies.{bcolors.ENDC}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", '--upgrade', 'pip'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT)
    except subprocess.SubprocessError:
        print(f"{bcolors.OKCYAN}mpg-foss: Could not update pip...{bcolors.ENDC}")

    for module in modules_base:
        try:
            __import__ (module)
        except ImportError:
            print(f"{bcolors.OKCYAN}mpg-foss: {module} not found...{bcolors.ENDC}")
            print(f"{bcolors.OKCYAN}mpg-foss: Installing {module}...{bcolors.ENDC}")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            except subprocess.SubprocessError:
                print(f"{bcolors.FAIL}mpg-foss: Could not acquire module named {module}. {bcolors.ENDC}")

def advanced():
    global modules_dependencies

    for module in modules_dependencies:
        try:
            __import__ (module)
        except ImportError:
            print(f"{bcolors.OKCYAN}mpg-foss: {module} not found...{bcolors.ENDC}")
            print(f"{bcolors.OKCYAN}mpg-foss: Installing {module}...{bcolors.ENDC}")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            except subprocess.SubprocessError:
                print(f"{bcolors.FAIL}mpg-foss: Could not acquire module named {module}.{bcolors.ENDC}")

def test():
    global modules_dependencies
    global modules_base
    global fail
    print(f"{bcolors.HEADER}mpg-foss: Verifying...{bcolors.ENDC}")

    for module in modules_dependencies:
        try:
            __import__ (module)
        except ImportError:
            fail = True
            print(f"{bcolors.FAIL}mpg-foss: {module} was not imported. Try manually installing it. {bcolors.ENDC}")
    for module in modules_base:
        try:
            __import__ (module)
        except ImportError:
            fail = True
            print(f"{bcolors.FAIL}mpg-foss: {module} was not imported. Try manually installing it. {bcolors.ENDC}")

def main():
    try:
        basic()
        from halo import Halo
        spinner = Halo(spinner='dots')
        spinner.start()
        advanced()
        test()
        if fail is not True:
            spinner.text_color = 'green'
            spinner.succeed("mpg-foss: Dependencies present & checked.")
            print(f"{bsymbols.info} {bcolors.OKGREEN}mpg-foss: Done.{bcolors.ENDC}")
        else:
            spinner.text_color = 'red'
            spinner.fail("mpg-foss: Some tests failed!")
            print(f"{bsymbols.info} {bcolors.OKGREEN}mpg-foss: Done.{bcolors.ENDC}")
    except (KeyboardInterrupt, SystemExit):
        spinner.stop()
    exit()

#Run the main function if this module is called directly.
if __name__ == '__main__':
   main()