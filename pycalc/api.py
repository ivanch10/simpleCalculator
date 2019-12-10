from __future__ import print_function
from calc import add2nums
import sys
import zerorpc

class CalcApi(object):
    def sum2nums(self, strA, strB):
        """
            This function calls add2nums() to calculate the sum of the A and B.

            Parameters: string input A, string input B
            Return: return sum of A and B
        """
        try:
            return add2nums(strA, strB)
        except Exception as e:
            return "Exception Error!"
    def echo(self, text):
        """
            This function echos any text.
            The main purpose is for testing connection between Python backend and JavaScript frontend

            Return: same text as in input Parameter
        """
        return text

def parse_port():
    port = 4242
    try:
        port = int(sys.argv[1])
    except Exception as e:
        pass
    return '{}'.format(port)

def main():
    addr = 'tcp://127.0.0.1:' + parse_port()
    s = zerorpc.Server(CalcApi())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()

if __name__ == '__main__':
    main()
