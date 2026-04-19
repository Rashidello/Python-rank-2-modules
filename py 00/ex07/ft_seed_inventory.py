# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rarayano <rarayano@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 23:20:36 by rarayano          #+#    #+#              #
#    Updated: 2026/04/18 23:20:36 by rarayano         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize() + " seeds: "
    if unit == "packets":
        print(name + str(quantity) + " packets available")
    elif unit == "grams":
        print(name + str(quantity) + " grams total")
    elif unit == "area":
        print(name + "covers " + str(quantity) + " square meters")