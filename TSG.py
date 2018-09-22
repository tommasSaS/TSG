#!/usr/bin/env python2.7
#
#
#

import os
import sys
d3=os.system("curl http://ipinfo.io/ip")
os.system("clear && clear && clear")
logo = '''\033[0m _/// _//////  _// //     _////
     _//    _//    _// _/    _//
     _//     _//      _//
     _//       _//    _//
     _//          _// _//   _////
     _//    _//    _// _//    _/
     _//      _// //    _///// \033[0m  \033[91m    \033[1m 
       }--{+} Coded By Manisso {+}--{
     }----{+}  fb.me/dzmanisso {+}----{
       }--{+} Greetz To IcoDz  {+}--{                               
     '''
menu = '''\033[0m
    {1}--Chi siamo                                                                                                                   
 '''
print logo
print menu
def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()
           
def  select():
  try:
    choice = input("Crips~# ")
    if choice == 1:
print logo                           
      """)

