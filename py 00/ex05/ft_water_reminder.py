# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rarayano <rarayano@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 22:27:29 by rarayano          #+#    #+#              #
#    Updated: 2026/04/18 22:27:29 by rarayano         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	time = int(input("Days since last watering: "))
	if time > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")