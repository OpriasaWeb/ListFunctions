# List Functions

Instructions: You are analyzing house prices. The given code declares a list with house prices in the neighborhood.
You need to calculate and output the number of houses that have a price that is above the average.

To calculate the average price of the houses, you need to divide the sum of all prices by the number of houses.

Pseudocode:





            BEGIN
              DECLARE prices equals to set of list [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]

              DECLARE sum_of_all equals to 0
              DECLARE average equals to 0
              DECLARE length_of_prices equals to 0
              DECLARE array_length equals to an empty list []

              FOR each of the prices
                sum_of_all plus each of the prices
                length_of_prices plus one each iteration # to get the length only
              ENDFOR

              average equals to sum_of_all / length_of_prices

              FOR each of the prices
                IF the current index is greater than the average
                  append this index to array_length
                ENDIF
              ENDFOR

              PRINT the length of the array_length

            END
