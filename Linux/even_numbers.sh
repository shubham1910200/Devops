echo "\nOdd numbers from 1 to 100:"
#!/bin/bash
# even_odd_number.sh: Ask user for a number and print if it is even or odd

read -p "Enter a number: " num
if ! [[ $num =~ ^-?[0-9]+$ ]]; then
  echo "Invalid input. Please enter an integer."
  exit 1
fi

if (( num % 2 == 0 )); then
  echo "$num is even."
else
  echo "$num is odd."
fi
