# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rarayano <rarayano@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 22:42:05 by rarayano          #+#    #+#              #
#    Updated: 2026/04/18 22:42:05 by rarayano         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	k = int(input("Days until harvest: "))
	for i in range(1, k + 1):
		print(f"Day {i}")
	print("Harvest time!")
