# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rarayano <rarayano@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 22:42:02 by rarayano          #+#    #+#              #
#    Updated: 2026/04/18 22:42:02 by rarayano         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def helper(i, n):
    if i > n:
        print("Harvest time!")
    else:
        print(f"Day {i}")
        helper(i + 1, n)

def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))
    helper(1, n)