'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-12
    * Time : 5:53 p.m.
    * Question :(https://www.codechef.com/LP0TO101/problems/FLOW010)
        Write a program that takes in a letterclass ID of a ship and display the equivalent string class description
        of the given ID. Use the table below.
    * Example :
        Input
        3
        B
        c
        D


        Output
        BattleShip
        Cruiser
        Destroyer
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    id_dict={'b':'BattleShip','c':'Cruiser','d':'Destroyer','f':'Frigate'}
    for _ in range(t):
        id=sys.stdin.readline().rstrip('\n')
        id=id.lower()
        if id in id_dict:
            sys.stdout.write(id_dict[id]+'\n')