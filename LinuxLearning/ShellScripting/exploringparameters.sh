#$0 - shows the first parameter
#$1 - is the 2nd parameter
#$2 - is the 3rd parameter
#$@ - All the arguments are double quoted. If a script receives two arguments, $* is equivalent to $1 $2.
#$@ - All the arguments are individually double quoted. If a script receives two arguments, $@ is equivalent to $1 $2.
#$? - The exit status of the last command executed.

echo "File Name: $0"
echo "First Parameter : $1"
echo "Second Parameter : $2"
echo "Quoted Values: $@"
echo "Quoted Values: $*"
echo "Total Number of Parameters : $#"