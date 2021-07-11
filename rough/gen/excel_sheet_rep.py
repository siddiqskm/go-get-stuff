"""
Q.  Given an Integer return corresponding excel sheet column name
dict => {
    A : 1
    B :
    C :
    D :
    E :
    F :
    ...
    X: 24
    Y: 25
    Z : 26
}

1 - A
2 - B

26 - Z
27 - 27 % 26 => 1  =>  A + dict.get(1)

180 - 180 % 26 => 24 => FX => (6) + dict.get(24)
Remainder -> 6 => F
Quotient -> 24 < 26 => X

1800 - 1800 % 26 => 
                     => ZZ
                     => AAA
                     => AAB

Deduce => The number using 26
Remainder -> 6
Quotient -> 69

Deduce => 
Remainder -> 2
Quotient -> 17

dict.get(2) + dict.get(17) + dict.get(6)

[6, 2]

BQF
"""
alpha_dict = {}

def get_excel_rep(num):
    ret_list = []
    while num >= 26:
        ret_list.append(num % 26)
        num = num // 26
        if num <= 26:
            ret_list.append(num)

    print("Return list is: %s" % ret_list)


get_excel_rep(701)
