In this example I will show how to add local allure reports to your python-pytest project.

Prerequisites:
1. Install Java (it's better to install an LTS version) - Allure requires Java installed on your machine. How to know Java is installed on your machine? Just open CMD and check Java version by the following command - $java -version
2. Install NodeJS - Allure requires NodeJS in your machine. How to know NodeJS installed you your machine? Just open CMD and check the node version by the following command - $ node -v
3. Install Allure command-line tool - open CMD and type the following command - $ npm install -g allure-commandline. In order to verify allure reports installed successfully type the following command - $ allure --version. (npm is the package manager that was installed together with nodejs).


Once you verify you installed all above you need to do the following:
1. Add allure to your environment variables - in your machine you need to find where the npm is installed, usually in Windows you will find npm installed inside the AppData folder (which is hidden folder) and inside the node_modules folder you'll find allure. Add the following path to the system variables path. The path should look like this "C:\Users\<Your-User>\AppData\Roaming\npm\node_modules\allure-commandline\bin"
2. Open powershell as administrator and type the following command - Get-ExecutionPolicy.
3. Open cmd and type - $ allure. the output should be like that -
Usage: allure [options] [command] [command options]
 Options:
   --help
     Print commandline help.
   -q, --quiet
     Switch on the quiet mode.
     Default: false
   -v, --verbose
     Switch on the verbose mode.
     Default: false
   --version
     Print commandline version.
     Default: false
4. Install allure-pytest as dependency in your project. Open CMD in your root project and type the following command - $ pip install allure-pytest. or just add it to the requirements.txt file like in my example.
5. In your root project open CMD and type the following command - $ pytest --alluredir="./reports". A new folder with the name "reports" will be created.
6. In your root project open CMD and type the following command - $ allure serve "./reports" than allure should be open automatically.


![image](https://github.com/eladSalti/allureReportLocal/assets/16322632/a712e049-8966-437b-bde4-316b58aa7f11)


