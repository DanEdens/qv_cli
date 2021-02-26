echo 'Welcome to Scanner config'
read -r -p "Enter Mqtt Host:" SCANNER_IP 
echo export \"SCANNER_IP=\${SCANNER_IP}\" >> ~/.scannerrc
read -r -p "Enter Mqtt Port:" SCANNER_PORT
echo export "SCANNER_PORT=\${SCANNER_PORT}" >> ~/.scannerrc
read -r -p "Enter your Amp Username: " SCANNER_AMPUSER
echo export "SCANNER_AMPUSER=\${SCANNER_AMPUSER}" >> ~/.scannerrc
read -r -p "Enter your Amp Password: " SCANNER_AMPPASS
echo export "SCANNER_AMPPASS=\${SCANNER_AMPPASS}" >> ~/.scannerrc
read -r -p "Enter your QV Username: " SCANNER_QVUSER
echo export "SCANNER_QVUSER=\${SCANNER_QVUSER}" >> ~/.scannerrc
read -r -p "Enter your QV Password: " SCANNER_QVPASS
echo export "SCANNER_QVPASS=\${SCANNER_QVPASS}" >> ~/.scannerrc
echo Value exports appended to ~/.scannerrc.. Refreshing env..
source ~/.scannerrc && exit 0
#https://linuxhint.com/bash-heredoc-tutorial/
