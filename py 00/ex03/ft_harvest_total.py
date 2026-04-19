# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rarayano <rarayano@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 03:12:33 by rarayano          #+#    #+#              #
#    Updated: 2026/04/18 03:12:33 by rarayano         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	i = int(input("Day 1 harvest: "))
	j = int(input("Day 2 harvest: "))
	k = int(input("Day 3 harvest: "))
	print(f"Total harvest: {i + k + j}")