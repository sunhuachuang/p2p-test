# p2p-test
a tool for test p2p network in one machine.

### Usage
1. `chmod a+x start.py`
2. `chmod a+x stop.py`
3. `sudo ln -s %PATH%/test-p2p/start.py /usr/local/bin/test-p2p-start`
4. `sudo ln -s %PATH%/test-p2p/stop.py /usr/local/bin/test-p2p-stop`
5. `test-p2p-start $START-PORT $END-PORT $CMD`. example: `test-p2p-start 5000 5050 python run.py`
6. `test-p2p-stop`
