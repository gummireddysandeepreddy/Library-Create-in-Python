# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 22:42:14 2022

@author: 21091A05H9
"""

def isPrime(num: int) -> bool:
    '''
    Prime : A number is divisible by 1 and itself
    Parameters
    ----------
    num : int
        To check Prime number or not.
    Returns
    -------
    bool
        True  <if n is Prime number>
        False <if n is not a Prime number>
    '''
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    return True
def nextPrime(num: int) -> int:
    '''
    Prime : A number is divisible by 1 and itself
    Parameters
    ----------
    num : int
    Returns
    -------
    x : int
        x is the first next Prime number after the n 
    '''
    x=num+1
    while True:
        if isPrime(x):
            return x
        x += 1
def n_Primes(n: int) -> list:
    '''
    Prime : A number is divisible by 1 and itself
    Parameters
    ----------
    n : int
    Returns
    -------
    list[l]
        Returns list of 'n' Prime numbers from 2.
    '''
    x=2
    li = []
    for i in range(n):
        x=nextPrime(x)
        li.append(x)
    return li
def isArmstrong(num: int) -> bool:
    '''
    Armstrong : sum of individual digits with power of number of digits in num
    Parameters
    ----------
    num : int
        To check Armstrong number or not.
    Returns
    -------
    bool
        True  <if n is Armstrong number>
        False <if n is not a Armstrong number>
    '''
    snum = str(num)
    li = [int(i) ** len(snum) for i in snum]
    return sum(li) == num
def nextArmstrong(num: int) -> int:
    '''
    Armstrong : sum of individual digits with power of number of digits in num
    Parameters
    ----------
    num : int
    Returns
    -------
    x : int
        x is the first next Prime number after the n.
    '''
    x=num+1
    while True:
        if isArmstrong(x):
            return x
        x += 1
def n_Armstrongs(n: int) -> list:
    '''
    Armstrong : sum of individual digits with power of number of digits in num
    Parameters
    ----------
    n : int
    Returns
    -------
    list[l]
        Returns list of 'n' Armstrong numbers from 1.
    '''
    x=1
    li = []
    for i in range(n):
        x=nextArmstrong(x)
        li.append(x)
    return li
def isPerfect(num: int) -> bool:
    '''
    Perfect number : sum of factors is equal to itself <num>
    Parameters
    ----------
    num : int
        To check Perfect number or not.
    Returns
    -------
    bool
        True  <if n is Perfect number>
        False <if n is not a Perfect number>
    '''
    sum = 0
    for i in range(1,num//2+1):
        if num % i == 0:
            sum += i
    return sum == num
def nextPerfect(num: int) -> int:
    '''
    Perfect number : sum of factors is equal to itself <num>
    Parameters
    ----------
    num : TYPE <int>

    Returns
    -------
    x : int
         x is the first next Perfect number after the n.
    '''
    x=num+1
    while True:
        if isPerfect(x):
            return x
        x += 1
def n_Perfect(n: int) -> list:
    '''
    Perfect number : sum of factors is equal to itself <num>
    Parameters
    ----------
    n : int
    Returns
    -------
    list[l]
        Returns List of 'n' Perfect numbers
    '''
    x=1
    li = []
    for i in range(n):
        x=nextPerfect(x)
        li.append(x)
    return li
def fact(n: int) -> int:
    '''
    Factorial : 1 * 2 * 3 * 4 * ...... * (n-1) * n
    Parameters
    ----------
    n : int
        To find the factorial(n)
    Returns
    -------
    int
        factorial of n
    '''
    if n<=1:
        return 1
    return n*fact(n-1)
def isNeon(num: int) -> bool:
    '''
    Neon : sum of individual digits of its square is equal to itself <num>
    Parameters
    ----------
    num : int
        To check Neon number or not.
    Returns
    -------
    bool
        True  <if n is Neon number>
        False <if n is not a Neon number>
    '''
    sq=num*num
    li = [int(i) for i in str(sq)]
    return sum(li) == num
def isSpy(n: int) -> bool:
    '''
    Spy : Product of individual digits is equal to itself <n>
    Parameters
    ----------
    n : int
        To check Spy number or not.
    Returns
    -------
    bool
        True  <if n is Spy number>
        False <if n is not a Spy number>
    '''
    li=[int(i) for i in str(n)]
    pro=1
    for i in li:
        pro *= i
    return sum(li) == pro
def isHappy(n: int) -> bool:
    '''
    Happy : if a number leads to 1 after a sequence of steps where in each step
    number is replaced by sum of squares of its digit
    Parameters
    ----------
    n : int
        To check Happy number or not.
    Returns
    -------
    bool
        True  <if n is Happy number>
        False <if n is not a Happy number>
    '''
    while n >9:
        li = [int(i) ** 2 for i in str(n)]
        n = sum(li)
        if n==1 or n == 7:
            return True
    return False
def isSunny(n: int) -> bool:
    '''
    Sunny : if 1 added to the given number, then the square root of it becomes a whole number
    Parameters
    ----------
    n : int
        To check Sunny number or not.
    Returns
    -------
    bool
        True  <if n is Sunny number>
        False <if n is not a Sunny number>
    '''
    from math import sqrt
    x = sqrt(n+1)
    return x==int(x)
def isDisarium(n: int) -> bool:
    '''
    Disarium : A number is a Disarium number if the sum of the digits powered with
    their respective positions is equal to the number itself.
    Parameters
    ----------
    n : int
        To check Disarium number or not.
    Returns
    -------
    bool
        True  <if n is Disarium number>
        False <if n is not a Disarium number>
    '''
    i=1
    Sum=0
    for j in str(n):
        Sum += int(j)**i
        i += 1
    return Sum == n
def isHarshad(n: int) -> bool:
    '''
    Harshad : if a number is divisible by the sum of its digits
    Parameters
    ----------
    n : int
        To check Hashad number or not.
    Returns
    -------
    bool
        True  <if n is Harshad number>
        False <if n is not a Harshad number>
    '''
    a=str(n)
    l = [int(i) for i in a]
    return n % sum(l) == 0
def isStrong(n: int) -> bool:
    '''
    Strong : if the sum of factorial of individual digit is equal to itself <n>
    Parameters
    ----------
    n : int
        To check Strong number or not.
    Returns
    -------
    bool
        True  <if n is Strong number>
        False <if n is not a Strong number>
    '''
    a = str(n)
    l = [fact(int(i)) for i in a]
    return sum(l) == n