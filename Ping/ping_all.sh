# Automation tool for Bulk_Ping

if [ -n "$1" ]; then 
	target=$1
		echo "\e[5m\e[41m\033[1;97m Make sure you have added new line in the ping file \033[0;37m"

	echo "Initiating Ping"	
	cat $target | while read domain
	do
		ping -c2 $domain >/dev/null
		if [ $? -eq 0 ]; then
		echo "\e[42m\033[1;97m [+] Host [$domain] is up \033[0;37m"
		output=$domain
		echo "$output" >> Pingstatus.md
		fi
	done
else
	echo "\e[5m\e[41m\033[1;97m No target supplied \033[0;37m"
fi
